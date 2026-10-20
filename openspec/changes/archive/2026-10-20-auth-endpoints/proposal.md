# Proposal

## Why

The EduTrack AI exposes CRUD endpoints for `subjects` (Tarefa 13), all protected
by `auth = ""`. The group `Autenticacao EduTrackIA Est` has only the `status`
health check — there is no endpoint that issues a JWT token. Without signup and
login, no client (FlutterFlow or a test tool) can obtain the token required to
call the protected endpoints, so the CRUD layer cannot be exercised end to end.

## What Changes

- Expose `POST /auth/signup`: register a user in the `user` table and return an
  authentication token.
- Expose `POST /auth/login`: validate e-mail and password against the `user`
  table and return an authentication token.
- Both endpoints live in the existing group `Autenticacao EduTrackIA Est`, so
  the token they issue is the same `$auth.id` the `subjects` endpoints read.
- `signup` rejects an e-mail already in use with `accessdenied`; `login`
  rejects wrong credentials without revealing which field failed.

Out of scope, because it was not requested: password reset, refresh token,
logout, e-mail verification, profile endpoints and any change to the `user`
schema.

## Capabilities

### New Capabilities

- `authentication`: issuing JWT tokens for the EduTrack AI backend — user
  registration and login.

### Modified Capabilities

None.

## Impact

- **New files:** `apis/autenticacao_edutrack_ia_est/auth_signup_POST.xs`,
  `auth_login_POST.xs`.
- **Reuses** the API group `Autenticacao EduTrackIA Est` (Tarefa 07/13); no new
  group.
- **Depends on:** the `user` table (auth table) already existing in workspace
  `148813`, branch `v1`.
- **Xano:** two new endpoints; no schema change.
- **Unblocks:** the end-to-end test of the `subjects` CRUD (Tarefa 13).
