# Tasks

## 1. Schema da tabela

- [x] 1.1 Criar `tables/academic_tasks.xs` com `auth = false` e o schema de seis campos: `id`, `title` (`text filters=trim`), `description` (`text`), `due_date` (`date`), `status` (`text filters=trim`) e `subject_id` (`int`, relationship para `subjects`)
- [x] 1.2 Declarar `index` com `{type: "primary", field: [{name: "id"}]}` e `{type: "btree", field: [{name: "subject_id"}]}`
- [x] 1.3 Rodar `openspec validate create-academic-tasks-table --strict` e conferir que a change passa

## 2. Push para o Xano (passo manual do desenvolvedor)

- [x] 2.1 Confirmar que a tabela `subjects` já existe no workspace antes do push
- [x] 2.2 Enviar `tables/academic_tasks.xs` (`xano workspace push --branch v1 --include "tables/academic_tasks.xs"`)
- [x] 2.3 Conferir no painel do Xano que a tabela tem os seis campos e que `subject_id` aponta para `subjects`

## 3. Arquivar

- [x] 3.1 Arquivar com `openspec archive create-academic-tasks-table` e confirmar que `openspec/specs/academic-tasks/spec.md` foi gerado
