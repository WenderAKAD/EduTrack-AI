# Proposal

## Why

The EduTrack AI backend stores the student's subjects (`subjects`) but not the
academic obligations — homework, exams and assignments — the student must track.
Without a table for those tasks there is nowhere to persist what each subject
requires, and no data for the frontend to display or for the intelligence layer
(Tarefa 12) to consume.

## What Changes

- Create the `academic_tasks` table with `id` (auto-generated primary key),
  `title`, `description`, `due_date`, `status` and `subject_id`.
- Make `subject_id` a required relationship to `subjects`, so every task belongs
  to an existing subject.
- Add a btree index on `subject_id`, because listing tasks by subject is the
  expected access path.
- Validate at the schema level that `title` and `status` are trimmed of
  surrounding whitespace.

Out of scope, because it was not requested: a direct `user_id` column (ownership
is inherited via `subjects.user_id`), timestamps, a status enum and any API
endpoint.

## Capabilities

### New Capabilities

- `academic-tasks`: the table of the student's academic obligations and its link
  to a subject.

### Modified Capabilities

None. `subjects` and `user` already exist and do not change; `subjects` enters
only as a prerequisite of the relationship.

## Impact

- **New file:** `tables/academic_tasks.xs`.
- **Depends on:** the `subjects` table must exist in Xano before the push,
  otherwise `subject_id` stays as an unresolved reference. Because the CLI orders
  by path and `tables/academic_tasks.xs` sorts before `tables/subjects.xs`,
  `academic_tasks` must be pushed separately, after `subjects`.
- **Xano:** one new table in workspace `148813`, branch `v1`.
- **No API change.** Endpoints belong to another change.
