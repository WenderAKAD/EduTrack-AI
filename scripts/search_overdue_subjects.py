"""Busca hibrida: identificar disciplinas com tarefas atrasadas.

Script Python puro para suportar a integracao com Xano. Recebe lista de tarefas
e retorna os subject_id que possuem pelo menos uma tarefa nao concluida com
due_date < hoje.

Especificacao: openspec/changes/busca-avancada-inteligente/specs/subjects/spec.md
"""

from datetime import date
from typing import List, Dict, Set

COMPLETED_STATUS = "completed"


def is_overdue_task(task: Dict, today: date = None) -> bool:
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


def handle(payload, today: date = None):
    if isinstance(payload, str):
        import json
        payload = json.loads(payload)
    tasks = payload.get("tasks", []) if isinstance(payload, dict) else payload
    ids = sorted(list(find_overdue_subject_ids(tasks, today)))
    return {"overdue_subject_ids": ids}


if __name__ == "__main__":
    sample = [
        {"subject_id": 1, "status": "pending", "due_date": "2025-01-01"},
        {"subject_id": 2, "status": "completed", "due_date": "2025-01-01"},
        {"subject_id": 3, "status": "in_progress", "due_date": "2099-01-01"},
        {"subject_id": 1, "status": "pending", "due_date": "2025-12-01"},
    ]
    print(handle({"tasks": sample}))
