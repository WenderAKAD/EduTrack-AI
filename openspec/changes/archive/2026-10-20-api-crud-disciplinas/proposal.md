# Proposal

## Why

The EduTrack AI backend stores the student's subjects (`subjects` table,
Tarefa 08) but exposes no API to read or manage them. The frontend cannot
create new subjects, cannot list the several subjects the student takes at the
same time, and cannot edit or remove them. Without those endpoints the app is a
backend with no door: the student's data exists in Xano but stays out of reach
of the client.

## What Changes

- Expose `GET /subjects`: list the authenticated user's subjects, filtered by
  `user_id` so one student never sees another student's data.
- Expose `POST /subjects`: create a subject owned by the authenticated user,
  forcing `user_id` from the JWT token — never from the request body.
- Expose `PATCH /subjects/{subject_id}`: update one of the user's subjects,
  refusing with `accessdenied` when the record belongs to another user.
- Expose `DELETE /subjects/{subject_id}`: delete one of the user's subjects,
  with the same ownership refusal as `PATCH`.
- Require authentication (`auth`) on all four endpoints, so the JWT token is
  validated before any database access.

Out of scope, because it was not requested: `GET /subjects/{id}` (reading a
single subject), pagination, filtering by name, and any endpoint for `user`,
`academic_tasks` or the progress calculation of Tarefa 12.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `subjects`: the existing capability gains a REST layer — four authenticated
  CRUD endpoints over the subjects table, each one scoped to the owning user.

## Impact

- **New files:** `apis/autenticacao_edutrack_ia_est/subjects_GET.xs`,
  `subjects_POST.xs`, `subjects_subject_id_PATCH.xs`,
  `subjects_subject_id_DELETE.xs`.
- **Reuses** the API group `AutenticacaoEduTrackIAEst` (Tarefa 07); no new API
  group and no new Base URL for the frontend.
- **Depends on:** the `subjects` table already existing in workspace `148813`,
  branch `v1` (created by the `create-subjects-table` change) and the `user`
  auth table feeding `$auth.id`.
- **Xano:** four new endpoints; no schema change.
- **No FlutterFlow change.** Consuming the endpoints is a later step.
