# Design

## Context

See `proposal.md` — Why, for the motivation. The shape of this change: the
workspace `148813` (branch `v1`) currently holds no domain tables at all. This
is the first one.

Two constraints come from the platform, not from preference:

- The `user` table must exist before this one is pushed, because a relationship
  to a table that does not exist yet is stored as an unresolved reference.
- The Xano CLI orders documents by path, and `tables/subjects.xs` sorts before
  `tables/user.xs`. A combined push would send `subjects` first.

The XanoScript dialect is narrow: `text` has no length limit, `int` is the only
integer type, and validation is expressed through `filters` rather than through
endpoint code.

## Goals / Non-Goals

**Goals:**

- Express ownership and validation as schema constraints, so they hold for any
  endpoint that later touches the table.
- Keep the field list at exactly what the specification declares.
- Make the table safe to push in any order relative to `user`.

**Non-Goals:**

- No API endpoints. Those belong to Tarefa 09.
- No `created_at` / `updated_at`. The specification fixes five fields; timestamps
  are a separate change.
- No foreign key to anything other than `user`.

## Decisions

**`user_id` is a required relationship, not a loose integer.**
A relationship makes the database reject a row that points at no account.
A loose `int` would allow orphans, and the isolation requirement would then rest
on every endpoint remembering to filter.
*Alternative considered:* nullable `int` with ownership assigned at the
endpoint. Rejected — it makes unowned rows representable.

**`hours` is `int` with `filters=min:1`, not `numeric`.**
The domain counts whole hours per week. `numeric` would admit 2.5 without a
business rule to justify the fraction.
*Alternative considered:* `numeric` for half-hour subjects. Rejected as
speculative — the specification says integer.

**`name` and `teacher` are `text`, not `varchar(255)`.**
XanoScript's `text` has no length limit. A 255 cap would be an arbitrary
constraint invented here, and `filters=trim` already handles the real need.
*Alternative considered:* `varchar(255)`. Rejected as an invented limit.

**Validation lives in `filters`, not in the endpoint.**
`filters=trim` and `filters=min:1` apply to every writer, including a future
admin script. Endpoint-level validation would only cover endpoints that
remembered to call it.
*Alternative considered:* validate in Tarefa 09's endpoints. Rejected as
insufficient coverage.

**A btree index on `user_id`.**
Every read filters by `user_id` — that is the isolation rule. Without the index
each list degrades to a full table scan.
*Alternative considered:* no index, add it when the data grows. Rejected: the
access pattern is known now and is fixed by the spec, not by volume.

**A `description` on the table states the ownership rule.**
The specification requires the table to carry a description saying that each row
belongs to an authenticated user through `user_id`. It is the one place in the
schema where the rule survives being read by someone who does not read XanoScript
— a dashboard listing shows it.
*Alternative considered:* leave the rule in `design.md` and `AGENTS.md` only.
Rejected — both are read by maintainers; the description is read by whoever
opens the table.

**No `created_at`.**
The specification lists five fields. Adding timestamps would make the delivered
table diverge from the spec it claims to implement, and the difference is not
observable behavior anyone depends on yet.

## Risks / Trade-offs

**Relationship unresolved if `user` is missing at push time** → Push
`tables/user.xs` in a separate command before this table, and confirm the
dry-run no longer warns about the FK. Recorded as a task in `tasks.md`.

**The CLI sorts by path, so ordering cannot be forced with one command** →
Accept the two-command sequence as the documented deployment procedure. The
alternative (`--sync --delete`) rewrites the whole workspace and is destructive.

**`hours = min:1` rejects zero silently at the schema level** → Accept. A
subject with no weekly hours is not a state the domain has, and rejecting it at
write time is the point.

**The five-field list will need to change** → Accept as a future change. The
spec is the contract; extending it is a new proposal, not an edit here.