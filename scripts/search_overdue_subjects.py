"""Busca hibrida: identificar disciplinas com tarefas atrasadas.

Funcao customizada (custom function) em Python puro para suportar a integracao
com Xano. Recebe as tarefas e as disciplinas do usuario e devolve:

- ``overdue_subject_ids``: subject_id com pelo menos uma tarefa nao concluida
  com ``due_date`` < hoje;
- ``subjects``: apenas as disciplinas dessa lista (filtro aplicado no lado
  Python, combinado com a busca por nome feita pelo Xano).

Especificacao: openspec/changes/busca-avancada-inteligente/specs/subjects/spec.md
"""

from datetime import date
from typing import Dict, List, Set

COMPLETED_STATUS = "completed"


def is_overdue_task(task: Dict, today: date = None) -> bool:
    """Tarefa atrasada: status != completed e due_date < hoje."""
    if today is None:
        today = date.today()
    status = str(task.get("status", "")).strip().lower()
    if status == COMPLETED_STATUS:
        return False
    due = task.get("due_date")
    if not due:
        return False
    try:
        if isinstance(due, str):
            due_date = date.fromisoformat(due[:10])
        elif hasattr(due, 'year'):
            due_date = due
        else:
            return False
        return due_date < today
    except Exception:
        return False


def find_overdue_subject_ids(tasks: List[Dict], today: date = None) -> Set[int]:
    """Retorna os subject_id que possuem tarefa atrasada e nao concluida."""
    overdue_ids = set()
    for t in tasks or []:
        if is_overdue_task(t, today):
            sid = t.get("subject_id")
            if sid is not None:
                try:
                    overdue_ids.add(int(sid))
                except Exception:
                    pass
    return overdue_ids


def filter_overdue_subjects(subjects: List[Dict], tasks: List[Dict], today: date = None) -> List[Dict]:
    """Filtra a lista de disciplinas, mantendo as que tem tarefa atrasada."""
    overdue_ids = find_overdue_subject_ids(tasks, today)
    result = []
    for s in subjects or []:
        sid = s.get("id")
        if sid is None:
            continue
        try:
            if int(sid) in overdue_ids:
                result.append(s)
        except Exception:
            continue
    return result


def handle(payload: Dict, today: date = None) -> Dict:
    """Entrada/saida JSON: {"tasks": [...], "subjects": [...]}.

    Devolve {"overdue_subject_ids": [...], "subjects": [...]} — subjects ja
    filtrado para as disciplinas com tarefas atrasadas.
    """
    if isinstance(payload, str):
        import json
        payload = json.loads(payload)
    tasks = payload.get("tasks", []) if isinstance(payload, dict) else payload
    subjects = payload.get("subjects", []) if isinstance(payload, dict) else []
    ids = sorted(list(find_overdue_subject_ids(tasks, today)))
    return {
        "overdue_subject_ids": ids,
        "subjects": filter_overdue_subjects(subjects, tasks, today),
    }


if __name__ == "__main__":
    sample_tasks = [
        {"subject_id": 1, "status": "pending", "due_date": "2025-01-01"},
        {"subject_id": 2, "status": "completed", "due_date": "2025-01-01"},
        {"subject_id": 3, "status": "in_progress", "due_date": "2099-01-01"},
        {"subject_id": 1, "status": "pending", "due_date": "2025-12-01"},
    ]
    sample_subjects = [
        {"id": 1, "name": "Innovation Lab", "teacher": "Prof. Silva", "hours": 4},
        {"id": 2, "name": "Banco de Dados", "teacher": "Prof. Souza", "hours": 2},
        {"id": 3, "name": "Redes", "teacher": "Prof. Lima", "hours": 4},
    ]
    print(handle({"tasks": sample_tasks, "subjects": sample_subjects}))
