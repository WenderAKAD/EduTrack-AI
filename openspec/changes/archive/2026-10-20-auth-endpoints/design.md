# Design

## Context

See `proposal.md` — Why and `specs/authentication/spec.md` for the
requirements. The constraints:

- The `user` table is the auth table (`auth = true` in `tables/user.xs`), so
  `security.create_auth_token` on it produces the token read later through
  `$auth.id`.
- The teamworkspace already has template endpoints (`auth/signup`, `auth/login`)
  in the `Authentication` group, but they point at an empty table name (`""`)
  and belong to a template that is not EduTrack AI. They are not reused.
- The protected `subjects` endpoints use `auth = ""`, expecting the token issued
  here.

## Decisions

**Two endpoints only: `signup` and `login`.** The task that needs them (the
end-to-end test of the `subjects` CRUD) requires only issuing a token. Logout,
refresh and password reset were not requested.

**They live in the `Autenticacao EduTrackIA Est` group.** The token must be
valid for the same group whose endpoints read `$auth` — the group already used
by `subjects`. A separate auth group would issue a token for a different scope.

**`signup` checks the e-mail before inserting.** A `db.get user` on the e-mail
plus a precondition (`accessdenied` when found) prevents duplicate accounts,
mirroring the unique btree index on `user.email`.

**`login` uses a single error message.** Both "user not found" and "wrong
password" answer `Invalid Credentials`, so the endpoint does not reveal which
field failed.

**Password hashing is delegated to Xano.** `security.create_auth_token` and the
`password` field filter (`min:8|minAlpha:1|minDigit:1`, `sensitive`) hold the
policy defined at the schema level; the endpoint does not reimplement it. On
signup the raw password is stored and Xano hashes it through the table's
`password` type behaviour; on login `security.check_password` compares them.

**Token expiry of 24h.** `expiration = 86400`, the value used by the workspace
templates and enough for a class session.

## Risks / Trade-offs

- **No rate limiting.** Brute-force protection is out of scope for this change.
- **The response returns only `authToken`.** The FlutterFlow client can call
  `auth/me` (future change) if it needs the profile; returning more now would be
  unrequested scope.
