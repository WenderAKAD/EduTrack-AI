# Proposal

## Why

The EduTrack AI app already has `subjects` and `academic_tasks`. Students need a way to find subjects quickly by typing part of the name, and also to surface subjects that have overdue tasks so they can prioritize what to do first. The request asks for a hybrid search that combines Xano (database) filtering with intelligent processing in Python, exactly the pattern the course wants to practice.

## What Changes

- Add a new authenticated endpoint to search subjects for the logged-in user.
- Support search by **name** (partial match, case-insensitive) using Xano filtering.
- Support search by **overdue tasks** using Python to analyze `academic_tasks` due dates against the current date and flag subjects that have at least one task not completed and past due.
- Expose the new behavior in an API that can be consumed by the frontend.
- Add a small Python helper script for the overdue calculation to keep the logic reusable/testable.

Out of scope, because not requested: full-text search across tasks/descriptions, pagination, fuzzy search ranking, changes to existing CRUD endpoints, or modifications to the Flutter app.

## Capabilities

### New Capabilities

- `subject-search`: advanced hybrid search over `subjects` scoped to the authenticated user, with filters by name and by overdue tasks.

### Modified Capabilities

None.

## Impact

- **New files:** `apis/autenticacao_edutrack_ia_est/subjects_search_GET.xs`, `scripts/search_overdue_subjects.py`
- **Reuses** the API group `Autenticacao EduTrackIA Est` and `$auth.id` for user scoping
- **Depends on:** `subjects` and `academic_tasks` tables already existing
- **Xano:** one new endpoint; Python runs as a custom function/integration as implemented
- **No schema changes**
