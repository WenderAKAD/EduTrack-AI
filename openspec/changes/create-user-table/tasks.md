# Tasks

## 1. Table definition

- [x] 1.1 Create `tables/user.xs` declaring `id` (auto), `name` (text), `email` (email), `password` (password), `is_active` (bool), `created_at` (timestamp) and `updated_at` (timestamp), and verify the file follows the XanoScript conventions used by `apis/autenticacao_edutrack_ia_est/`
- [x] 1.2 Set `auth = true` on the table, and verify the flag is present in the `.xs` definition
- [x] 1.3 Apply `filters=trim|lower` to `email` and `filters=min:8|minAlpha:1|minDigit:1` to `password`, mark `password` with `sensitive = true`, and verify `email` is not marked sensitive
- [x] 1.4 Default `is_active?=true` and `created_at?=now`, leave `updated_at` optional, and verify neither `updated_at` nor `name` carries a default
- [x] 1.5 Declare a primary index on `id` and a unique index on `email`, and verify both indexes are present
- [x] 1.6 Verify `git status` lists `tables/user.xs` as new and that no other table file was added

## 2. Push to Xano

- [x] 2.1 Run `xano workspace push --include "tables/user.xs" --dry-run` and verify the preview lists exactly one change, `CREATE table user`, with no other object
- [ ] 2.2 Run `xano workspace push --include "tables/user.xs"` and verify it completes with no error output
- [ ] 2.3 Verify the preview reported no unresolved reference for `table user`; if the table was pushed inside a larger push, report it and stop, because `tables/user.xs` sorts after `tables/subjects.xs`
- [ ] 2.4 Open the Xano dashboard and verify the `user` table exists with exactly the seven specified fields and that it is marked as the authentication table

## 3. Hand over to subjects

- [ ] 3.1 Mark every task above as completed with `- [x]` and verify no `- [ ]` checkbox remains in `tasks.md`
- [ ] 3.2 Run `openspec validate create-user-table` and verify it reports no errors
- [ ] 3.3 Run `xano workspace push --include "tables/subjects.xs" --dry-run` and verify the `user_id` relationship no longer appears under Unresolved References
- [ ] 3.4 Run `openspec archive create-user-table` and verify the change moved into `openspec/changes/archive/` and `openspec/specs/user/spec.md` was created from the delta
- [ ] 3.5 Update the `AGENTS.md` rule about the authentication table to state that `user` is created by this project, and verify the rule no longer claims the table ships with Xano