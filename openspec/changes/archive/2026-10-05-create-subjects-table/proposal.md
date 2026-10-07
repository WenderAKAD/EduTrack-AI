# Proposal

## Why

The EduTrack AI backend has no table for the subjects a student tracks — the
first domain entity of the project. Without it there is nothing for the API
layer of Tarefa 09 to read or write, and the security rule that every query
filters by the authenticated `user_id` has no table to apply to.

## What Changes

- Create the `subjects` table with exactly five fields: `id` (auto-generated
  primary key), `name`, `teacher`, `hours` and `user_id`.
- Make `user_id` a required relationship to `user`, so every row is owned by an
  authenticated account and no row can exist unowned.
- Add a btree index on `user_id`, because the isolation rule makes it the filter
  column of every read.
- Enforce `hours >= 1` and trim whitespace from `name` at the schema level, so
  invalid rows are rejected by the database rather than by each endpoint.
- Declare a table `description` stating that each row belongs to an
  authenticated user through `user_id`, so the ownership rule is readable from
  the table itself and not only from this proposal.
- Document that `created_at` is deliberately absent: the specification fixes the
  field list, and adding timestamps is a separate change.

## Capabilities

### New Capabilities

None. Both tables involved already have specs from the previous changes.

### Modified Capabilities

- `subjects`: The `user` capability is referenced here as an existing
  dependency — `subjects.user_id` is a relationship against the `user` table
  already specified in `openspec/specs/user/spec.md`. No requirement in the
  `user` spec changes, so `user` is not listed as modified. The delta in
  `specs/subjects/spec.md` re-states the ownership and isolation requirements
  from the `subjects` point of view, and declares `user` as a prerequisite
  rather than as a pre-existing table.

## Impact

- **New file:** `tables/subjects.xs`.
- **Depends on:** the `user` table (Xano id `904016`) must exist before this
  table is pushed, otherwise the `user_id` relationship is stored as an
  unresolved reference. See `design.md`.
- **Xano:** one new table in workspace `148813`, branch `v1`, pushed with
  `xano workspace push --include "tables/subjects.xs"`.
- **No API changes.** Endpoints are out of scope; this change creates the table
  the Tarefa 09 endpoints will read.