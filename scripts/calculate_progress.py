"""Calculo do progresso de uma disciplina do EduTrack AI.

Funcao customizada (custom function) em Python puro: recebe as tarefas de uma
disciplina em JSON e devolve o percentual de conclusao em JSON, com a chave
``percentage``.

Especificacao: openspec/specs/progress-calculation/spec.md
"""

import json

COMPLETED_STATUS = "completed"


def calculate_progress(completed_tasks, total_tasks):
    """Retorna {"percentage": x} de 0 a 100; 0 quando nao ha tarefas."""
    if total_tasks <= 0:
        return {"percentage": 0}
    return {"percentage": round(completed_tasks / total_tasks * 100, 2)}


def is_completed(task):
    """Uma tarefa conta como concluida quando o status e 'completed'."""
    status = str(task.get("status", "")).strip().lower()
    return status == COMPLETED_STATUS


def calculate_subject_progress(tasks):
    """Calcula o progresso a partir da lista de tarefas da disciplina."""
    tasks = tasks or []
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if is_completed(task))
    return calculate_progress(completed_tasks, total_tasks)


def handle(payload):
    """Entrada/saida JSON: {"tasks": [...]} -> {"percentage": ...}."""
    if isinstance(payload, str):
        payload = json.loads(payload)
    return calculate_subject_progress(payload.get("tasks", []))


if __name__ == "__main__":
    examples = [
        {"tasks": [{"status": "completed"}, {"status": "pending"}]},
        {"tasks": [{"status": "completed"}, {"status": "completed"}]},
        {"tasks": []},
        {"tasks": [{"status": " completed "}, {"status": "pending"}, {"status": "completed"}]},
    ]
    for example in examples:
        print(json.dumps(handle(example)))
