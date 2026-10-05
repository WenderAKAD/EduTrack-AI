# Proposal

## Why

EduTrack AI has no database at all. The workspace *Wender's Workspace* (id
`148813`, branch `v1`) contains 194 objects — 176 API endpoints, 10 API groups,
5 functions, a tool, an agent and an addon — and **zero tables**. There is
nowhere to store a user, and therefore nowhere to store anything owned by one.

This blocks `create-subjects-table`: `subjects.user_id` is specified as a
relationship to the authentication table, and there is no such table to link
to. The `addons/109599_user.xs` file in this repo appears to reference `user`,
but it is itself broken — it carries `table = ""` and `db.query ""`, and the CLI
reports it as an unresolved reference. It is not a working table.

This change creates the authentication table the rest of the domain depends on.

## What Changes

- Add a `user` table to the Xano workspace, versioned as `tables/user.xs`
- `auth = true`, making it the authentication table for the workspace
- Fields: `id` (auto-generated), `name` (text), `email` (email, unique),
  `password` (password, sensitive), `is_active` (bool, default `true`),
  `created_at` (timestamp, default `now`), `updated_at` (timestamp, optional)
- Unique index on `email`; primary key on `id`
- No signup/login endpoints in this change — only the table. Those belong to the
  authentication module

## Capabilities

### New Capabilities

- `user`: the authentication table, its credential fields and the constraints
  that make an account usable — unique email, hashed password, active flag

### Modified Capabilities

None. `openspec/specs/` is still empty.

## Impact

- **Xano:** one new table `user` in workspace *Wender's Workspace* (id
  `148813`), branch `v1`, instance `x8ki-letl-twmt`
- **Unblocks:** `create-subjects-table`, whose `subjects.user_id` relationship
  is otherwise unresolvable
- **Repository:** new file `tables/user.xs`; `AGENTS.md` is corrected in the
  same series because it previously asserted that the authentication table
  already existed in Xano
- **Ordering constraint:** the CLI sends documents in alphabetical path order
  and `tables/subjects.xs` sorts before `tables/user.xs`, so `user` must be
  pushed on its own before `subjects` is pushed
- **Security:** `password` is marked `sensitive`, so it is excluded from
  readable query output. `email` is deliberately **not** marked sensitive —
  login requires reading it
- **Risk:** `auth = true` changes how the workspace handles authentication. Any
  API endpoint that later sets `auth = "user"` will require a bearer token, so
  this table must land before the authentication endpoints are written