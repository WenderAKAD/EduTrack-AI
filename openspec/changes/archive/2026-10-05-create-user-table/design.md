# Design

## Context

See `proposal.md` — *Why* for motivation and `specs/user/spec.md` for the
requirements. Only the constraints that shape the approach are described here.

- The workspace has no tables. `addons/109599_user.xs` references `$db.user`
  but is broken (`table = ""`, `db.query ""`) and must not be treated as a table
  definition or as evidence one exists.
- `tables/` is currently empty and untracked, so `tables/user.xs` will be its
  first file.
- The CLI sends documents in alphabetical path order. `tables/subjects.xs`
  sorts before `tables/user.xs`, so a combined push would leave the
  `subjects.user_id` relationship unresolved.

## Goals / Non-Goals

**Goals:**

- Produce a table that satisfies the spec and that `subjects` can reference.
- Make the credential fields safe by construction rather than by convention.
- Land `user` on the server in a push that contains nothing else.

**Non-Goals:**

- Signup, login and `auth/me` endpoints — these belong to the authentication
  module, not here.
- Any role model, profile fields, avatar or preferences.
- Replacing or repairing `addons/109599_user.xs`; it is unrelated sample content
  and is out of scope for this change.

## Decisions

**`auth = true` on the table.**
This is what makes `user` the workspace's authentication table, which in turn is
what lets endpoints declare `auth = "user"` and read `$auth.id`. Without it the
table would be an ordinary table and the ownership rule in `AGENTS.md` would
have nothing to point at.
*Alternative considered:* a plain table plus application-level tokens. Rejected —
it duplicates what the platform already provides and weakens `$auth.id`.

**`email` unique, `password` not marked sensitive.**
`email` is what login looks a user up by, so it must be readable; it is
normalised with `filters=trim|lower` so uniqueness is case-insensitive.
`password` is marked `sensitive = true`, which is what excludes it from readable
query output.
*Alternative considered:* marking `email` sensitive as one documentation example
does. Rejected — it would make the login lookup impossible, and the field
reference treats `email` as a normal readable type.

**Password strength filters on the field.**
`filters=min:8|minAlpha:1|minDigit:1` puts the policy in the schema, so every
future path that writes a user is covered without repeating the check.
*Alternative considered:* validating only in the signup endpoint. Rejected — an
endpoint-level check is bypassed by any other writer.

**`is_active` defaults to `true` rather than being required.**
New accounts work without the caller thinking about it, while still allowing
deactivation.
*Alternative considered:* required with no default. Rejected — it pushes a
decision onto every caller for a field that has an obvious initial value.

**`created_at` is set, `updated_at` is left empty.**
There is no update path yet, so `updated_at` stays optional rather than
defaulting to `now`, which would falsely claim every row was just modified.

## Risks / Trade-offs

- **Single shared push cannot work** — alphabetical ordering puts `subjects`
  first → *Mitigation:* push `user` alone, confirm it exists, then push
  `subjects`. Task 2.3 exists to catch a combined push going in by mistake.
- **`auth = true` changes workspace-wide auth behaviour** — endpoints that later
  set `auth = "user"` will start requiring a bearer token → *Mitigation:* this
  change lands before any authentication endpoint is written, and no existing
  EduTrack AI endpoint references it yet.
- **Unique email migration** — adding the unique index to a populated table can
  fail if duplicates exist → *Mitigation:* the table is new, so it is created
  empty and cannot contain duplicates.
- **Password hashing is platform behaviour, not visible in the `.xs` file** →
  the spec pins the requirement so it can be verified in the dashboard rather
  than assumed from the definition.