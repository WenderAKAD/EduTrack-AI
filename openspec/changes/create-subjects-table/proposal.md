# Proposal

## Why

EduTrack AI has no domain data yet. The Xano workspace currently contains no
application tables — the `tables/` folder in this repository is empty — so there
is nowhere to record the academic subjects a student is enrolled in. Without
subjects there is no foundation for tracking tasks, grades, or progress per
discipline, and no table to relate future entities to.

This change establishes the first domain table of the project. Following
Spec-Driven Development, the structure is specified and reviewed before any code
is written, so the contract for subject data is agreed on before the table is
created in Xano.

## What Changes

- Add a `subjects` table to the Xano workspace, versioned as
  `tables/subjects.xs`
- Fields: `id` (auto-generated), `name` (text), `teacher` (text), `hours`
  (integer), `user_id` (foreign key to the authentication table)
- `user_id` is required on every record, so each subject is scoped to exactly
  one authenticated user
- `hours` is validated as a positive integer and `name` is trimmed
- Nothing else: no API endpoints, no tests, and no frontend screens are part of
  this change

## Capabilities

### New Capabilities

- `subjects`: structure and ownership rules of the `subjects` table, the first
  domain entity of EduTrack AI

### Modified Capabilities

None. `openspec/specs/` is still empty, so there is no existing capability
being changed.

## Impact

- **Xano:** one new table `subjects` in the workspace *Wender's Workspace*
  (id `148813`), branch `v1`, instance `x8ki-letl-twmt`
- **Repository:** new file `tables/subjects.xs` — the folder is currently empty
  and therefore not tracked by Git, so this will be the first versioned table
- **OpenSpec:** new change `create-subjects-table`, consolidated into
  `openspec/specs/subjects/` when archived
- **Frontend:** unchanged. The FlutterFlow project is not touched by this change
- **API:** unchanged. The API Group `Xano Backend`
  (`https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC`) continues to expose only
  `GET /status`
- **Authentication table:** `user_id` references the `user` table, which already
  exists in the workspace. It is confirmed by `addons/109599_user.xs`, an addon
  that queries `$db.user.id` — the table exists in Xano, it simply has no
  versioned definition file under `tables/`, since XanoScript does not sync
  built-in tables there. The relationship can therefore be declared directly.