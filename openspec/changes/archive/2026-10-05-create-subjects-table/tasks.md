# Tasks

## 1. Schema da tabela

- [x] 1.1 Criar `tables/subjects.xs` com `auth = false` e o schema de 5 campos: `id`, `name` (text, `filters=trim`), `teacher` (text), `hours` (int, `filters=min:1`) e `user_id` (relationship para `user`) — verificar com `grep -c` que o bloco `schema` declara exatamente 5 campos
- [x] 1.2 Declarar `index` com `{type: "primary", field: [{name: "id"}]}` e `{type: "btree", field: [{name: "user_id"}]}` — verificar que ambos os índices estão presentes no arquivo
- [x] 1.3 Confirmar que a tabela NÃO declara `created_at` nem `updated_at` — verificar por `grep` que nenhum dos dois aparece no arquivo
- [x] 1.4 Rodar `openspec validate create-subjects-table --strict` e confirmar que a change é válida

## 2. Push ao Xano

- [x] 2.1 Autenticar no Xano CLI com `xano auth` — verificar que o comando conclui sem erro
- [x] 2.2 Confirmar que a tabela `user` já existe no servidor (id `904016`) ANTES de enviar `subjects` — verificar que um dry-run de `tables/subjects.xs` não reporta `table (FK) -> table "user" does not exist`
- [x] 2.3 Enviar com `xano workspace push --include "tables/subjects.xs"` — verificar que a saída confirma o push de 1 documento e que o erro `Push blocked` não aparece
- [x] 2.4 Rodar o dry-run novamente e confirmar `No changes to push` — se o CLI propuser `DROP_FIELD` ou `CREATE` sobre `user`, abortar e reportar em vez de sincronizar

## 3. Validação e arquivamento

- [x] 3.1 Confirmar no dashboard do Xano que a tabela `subjects` existe com os 5 campos e que o relationship `subjects.user_id` aponta para `user` — verificar visualmente e registrar o id da tabela
- [x] 3.2 Confirmar que a tabela está na branch `v1` do workspace `148813` — verificar no dashboard ou via `xano workspace pull --dry-run` que não há divergência em `tables/subjects.xs`
- [x] 3.3 Arquivar a change com `openspec archive create-subjects-table` e confirmar que `openspec/specs/subjects/spec.md` foi gerado com os 4 requirements do delta — verificar com `openspec validate --specs --strict`