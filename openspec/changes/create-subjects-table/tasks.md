# Tasks

## 1. Table definition

- [x] 1.1 Create `tables/subjects.xs` declaring `id` (auto), `name` (text), `teacher` (text), `hours` (int) and `user_id`, and verify the file follows the XanoScript conventions used by `apis/autenticacao_edutrack_ia_est/`
- [x] 1.2 Declare `user_id` as a required relationship to the authentication table, and verify the relationship is defined in the file rather than left to application code
- [x] 1.3 Add the validation chosen in `design.md` — required on the four non-key fields, positive-integer filter on `hours`, and `trim` on `name` — and verify each rule is present in the `.xs` definition
- [x] 1.4 Verify `tables/subjects.xs` is the only table added and that `git status` lists it as a new tracked file

## 2. Apply to Xano

- [ ] 2.1 Authenticate XanoScript and confirm the active workspace is *Wender's Workspace* (id `148813`) on branch `v1`, and verify the reported workspace and branch match before pushing
- [ ] 2.2 Run `XanoScript: Push Stage Changes to Xano` and verify the command completes with no error output
- [ ] 2.3 Open the Xano dashboard and verify the `subjects` table exists with exactly the five specified fields, `id` marked auto-generated and `user_id` present as a relationship
- [ ] 2.4 If the push is rejected on the `user_id` relationship, record the exact XanoScript error message and report it instead of altering the authentication schema, since that change is out of scope for this proposal

## 3. Consolidate the specification

- [ ] 3.1 Mark every task above as completed with `- [x]` and verify no `- [ ]` checkbox remains in `tasks.md`
- [ ] 3.2 Run `openspec validate create-subjects-table` and verify it reports no errors
- [ ] 3.3 Run `openspec archive create-subjects-table` and verify the change moved into `openspec/changes/archive/` and `openspec/specs/subjects/spec.md` was created from the delta