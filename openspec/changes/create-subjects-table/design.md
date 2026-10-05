# Design

## Context

See `proposal.md` — *Why* for motivation and `specs/subjects/spec.md` for the
requirements. Only the constraints that shape the approach are described here.

- `tables/` in this repository is empty and untracked, so `tables/subjects.xs`
  will be the first versioned table and there is no in-repo precedent to copy.
  The closest reference is the versioned API Group at
  `apis/autenticacao_edutrack_ia_est/`.
- The workspace *Wender's Workspace* (id `148813`, branch `v1`) already has a
  `user` table. It is confirmed by `addons/109599_user.xs`, which is an addon
  (`addon user { ... }`) querying `$db.user.id`. Built-in tables are not synced
  into `tables/`, so the absence of a file there is expected and not a gap.
- Per `AGENTS.md`, the agent generates and reviews files; the push to Xano is
  performed manually by the developer.

## Goals / Non-Goals

**Goals:**

- Define the field-level XanoScript representation that satisfies the spec.
- Decide how `user_id` is declared so the ownership rule is enforced by the
  database rather than only by application code.
- Keep the change reversible and reviewable in a single commit.

**Non-Goals:**

- Endpoints, queries, tests, or FlutterFlow screens.
- Any change to the existing API Group or to `GET /status`.
- Any change to the authentication schema — that is a separate change with its
  own proposal, if it turns out to be needed.

## Decisions

**`user_id` as a required relationship, not a loose integer.**
The spec requires that every subject has exactly one owner and that reads are
scoped to that owner. A relationship makes the database enforce both: the
foreign key rejects orphans, and the join enables `WHERE user_id = :current`.
A bare integer column would rely entirely on application code to populate and
filter it, which is exactly the rule that gets forgotten.
*Alternative considered:* plain `int` + application-level filtering. Rejected —
it moves an integrity guarantee out of the database.

**`hours` as `int` with a positive-integer filter.**
Weekly contact hours are whole numbers in every subject model; storing them as
`int` avoids float formatting and lets the database reject `0` and negatives.
*Alternative considered:* `numeric` to allow half-hours. Rejected for now — it
would loosen validation for a case the spec does not require.

**`name` and `teacher` as plain `text` with `trim`.**
No length cap and no enum: subject and teacher names vary too much across
institutions to constrain safely at this stage.
*Alternative considered:* `varchar(255)`. Rejected — an arbitrary cap would be
a decision to revisit, and Xano's `text` has no practical limit at this scale.

**Filename `tables/subjects.xs`.**
Follows the project convention of one XanoScript file per table, named after
the table.

## Risks / Trade-offs

- **Relationship target is unversioned** — `user` exists in Xano but has no
  file under `tables/`, so the foreign key cannot be cross-checked in the repo
  → *Mitigation:* rely on the push to validate it; if Xano rejects the
  relationship, report the error rather than changing the authentication
  schema.
- **`trim` behaviour differs between Xano and a future non-Xano backend** → the
  rule lives in the spec, not only in the `.xs` file, so it survives a backend
  change.
- **First table sets the convention** — later tables will copy whatever is done
  here → *Mitigation:* the field-level decisions above are written down so the
  convention is explicit rather than accidental.

## Migration Plan

1. Add `tables/subjects.xs` and commit it.
2. Developer pushes with `XanoScript: Push Stage Changes to Xano`.
3. Verify `subjects` exists in the Xano dashboard with the five fields.
4. Rollback: the table holds no data yet, so reverting means dropping it in the
   Xano dashboard and reverting the commit. No data migration is involved.