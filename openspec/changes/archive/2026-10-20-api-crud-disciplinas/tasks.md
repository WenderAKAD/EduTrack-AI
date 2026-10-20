# Tasks

## 1. Endpoints CRUD de subjects

- [x] 1.1 Criar `apis/autenticacao_edutrack_ia_est/subjects_GET.xs` — `GET /subjects` com `auth = ""` e `where = $db.subjects.user_id == $auth.id`, retornando a lista do usuário autenticado
- [x] 1.2 Criar `apis/autenticacao_edutrack_ia_est/subjects_POST.xs` — `POST /subjects` com `auth = ""`, inputs `name`, `teacher` e `hours` obrigatórios e `user_id = $auth.id` gravado no `db.add` (nunca vem do body)
- [x] 1.3 Criar `apis/autenticacao_edutrack_ia_est/subjects_subject_id_PATCH.xs` — `PATCH /subjects/{subject_id}` com `auth = ""`, `db.get` + preconditions `notfound` e `accessdenied` (dono) e merge parcial via `util.get_raw_input`
- [x] 1.4 Criar `apis/autenticacao_edutrack_ia_est/subjects_subject_id_DELETE.xs` — `DELETE /subjects/{subject_id}` com `auth = ""`, `db.get` + preconditions `notfound` e `accessdenied` (dono) e `db.del`
- [x] 1.5 Conferir os quatro arquivos com o parser da extensão XanoScript (sem erros de sintaxe no editor)

## 2. Validação OpenSpec

- [x] 2.1 Rodar `openspec validate api-crud-disciplinas --strict` e conferir que a change passa

## 3. Push para o Xano (passo manual do desenvolvedor)

- [ ] 3.1 Confirmar que a tabela `subjects` e a tabela de auth `user` já existem no workspace antes do push
- [ ] 3.2 Enviar os quatro endpoints (`xano workspace push --branch v1 --include "apis/autenticacao_edutrack_ia_est/subjects*"`)
- [ ] 3.3 Testar no Run & Debug / Swagger do Xano: criar, listar, alterar e deletar com dois usuários distintos, confirmando que cada um só vê as próprias disciplinas

## 4. Arquivar

- [ ] 4.1 Arquivar com `openspec archive api-crud-disciplinas` e confirmar que `openspec/specs/subjects/spec.md` foi atualizado com os requirements de API
