# Design

## Context

The task says "desenvolver uma funcionalidade de busca que utiliza tanto o banco de dados (Xano) quanto um processamento inteligente (Python) para filtrar disciplinas por relevância ou status de atraso." 
- We already have `subjects` (owned by `user_id`) and `academic_tasks` (linked to `subject_id`, have `due_date` and `status`).
- Tarefa 12 showed we can use pure Python scripts in `scripts/`.

## Decisions

**Hybrid approach.** 
- **Xano side:** query `subjects` filtered by `user_id = $auth.id`. If `q` (name search) is provided, apply case-insensitive partial match on `name` (e.g. `contains`/`ilike` style). 
- **Python side:** when searching for overdue subjects or to compute "has_overdue", load related `academic_tasks` (or receive them from Xano), determine if a subject has any task where `status != 'completed'` and `due_date < today`. Return the filtered/annotated list.

**Endpoint shape.** Add `GET /subjects/search` (or `GET /subjects_search`) in the existing group `Autenticacao EduTrackIA Est`. Accept query params like `q` (name) and/or `overdue=true`. Keep it authenticated (`auth = ""`).

**Python script.** Create `scripts/search_overdue_subjects.py` with functions like `find_overdue_subject_ids(tasks, today)` returning subject_ids that have overdue incomplete tasks. Keep it simple and testable locally with `python3`.

**Security.** Always filter by `$auth.id`. Never leak other users' data.

**Simplicity over perfection.** Follow "exactly what was asked" - filter by name OR by overdue tasks (integrating Python). Don't add complex ranking algorithms.

## Risks / Trade-offs

- **Xano/Python integration details:** exact way depends on Xano UI, but we provide the script and endpoint structure that fits the project patterns.
- **Date comparison:** use ISO date strings or Xano date type consistently.
- **Performance:** fine for course exercise.
