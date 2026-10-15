# Design

## Context

See `proposal.md` — Why and `specs/academic-tasks/spec.md` for the
requirements. Two constraints come from the platform:

- The `subjects` table must exist before the push, because a relationship to a
  missing table stays as an unresolved reference. `subjects` was created by the
  `create-subjects-table` change (Tarefa 08).
- The Xano CLI orders by path, and `tables/academic_tasks.xs` sorts before
  `tables/subjects.xs`. A combined push would send `academic_tasks` first.

## Decisions

**`due_date` is type `date`, not `timestamp`.** A task stores a due day, not an
instant. A `timestamp` would force a made-up time of day.

**No `user_id` on the table.** Ownership is inherited from `subjects.user_id`;
duplicating `user_id` would create two sources of truth for the same fact.
Isolation still holds because a task only exists inside a subject, and the
subject is already scoped by user.

**No `guid`.** XanoScript generates the table's `guid` on push; declaring an
invented local value adds no benefit and risks divergence. The `user` and
`subjects` tables only carry a `guid` because they were downloaded from the
server.

**`status` is plain `text`.** The requirement asks for `status (text)` and no
closed set of values is defined, so an enum would be unrequested scope.

**Btree index on `subject_id`.** Listing tasks by subject is the expected access
pattern; without the index every read scans the table.

## Risks / Trade-offs

- **Unresolved reference if `subjects` is missing.** Mitigation: push
  `tables/academic_tasks.xs` separately, after confirming `subjects` exists in
  the workspace.
