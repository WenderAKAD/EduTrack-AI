# Tarefa 11 – Adicionar Tabela Tarefas via XanoScript

[← Voltar ao índice](../../README.md#tarefas)

---

Aluno: Wender Araujo Santos
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code
Módulo: 2 – Integração Frontend-Backend

A tabela `academic_tasks` foi criada no backend do EduTrack AI seguindo o fluxo
do Spec-Driven Development: a mudança foi planejada, implementada em XanoScript,
validada, enviada ao Xano e arquivada.

---

1. O QUE FOI FEITO

- Change OpenSpec `create-academic-tasks-table` criada com os quatro artifacts do
  schema `spec-driven`: `proposal.md`, `specs/academic-tasks/spec.md`,
  `design.md` e `tasks.md`.
- Validada com `openspec validate create-academic-tasks-table --strict`
  (change válida) e `openspec validate --specs --strict` (3 specs, 0 falhas).
- Tabela implementada em `tables/academic_tasks.xs` com seis campos: `id`
  (chave primária auto-gerada), `title` (`text filters=trim`), `description`
  (`text`), `due_date` (`date`), `status` (`text filters=trim`) e `subject_id`
  (`int`, relationship para `subjects`).
- Index declarado: `primary` em `id` e `btree` em `subject_id`.
- Push enviado ao Xano (workspace `148813`, branch `v1`):
  `CREATE table academic_tasks`. O servidor gravou o `guid` de volta no arquivo
  local.
- Change arquivada com `openspec archive create-academic-tasks-table`, gerando a
  spec mestra `openspec/specs/academic-tasks/spec.md`.
- Branch de trabalho: `feat/tabela-tarefas`.

---

2. ENTREGÁVEIS

- [x] Tabela criada via XanoScript.
      Arquivo: `tables/academic_tasks.xs`
- [x] Fluxo OpenSpec completo (proposal → implementation → archive).
      `openspec/changes/archive/2026-10-15-create-academic-tasks-table/`
- [x] Spec mestra sincronizada.
      `openspec/specs/academic-tasks/spec.md`
- [x] Link do arquivo `.xs` no GitHub.
      https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est/blob/feat/tabela-tarefas/tables/academic_tasks.xs
- [ ] Print do painel do Xano com a tabela criada.
      `docs/evidencias/tarefa11/xano-academic-tasks.png`
- [ ] Material de entrega versionado.
      `docs/evidencias/tarefa11/Tarefa11-entrega.html`, `.pdf`

---

3. CRITÉRIOS DE AVALIAÇÃO

- [x] Uso correto do fluxo OpenSpec (proposal → implementation → archive).
- [x] Tabela criada no Xano com todos os campos solicitados.
- [x] Relacionamento entre tarefas e disciplinas (`subject_id` → `subjects`).
- [x] Commit na branch `feat/tabela-tarefas`.

---

4. OBSERVAÇÕES TÉCNICAS

- **Escopo respeitado (REGRA Nº 1).** A tabela tem somente os campos pedidos.
  Não foi adicionado `user_id` — a posse é herdada via `subjects.user_id`,
  evitando duas fontes de verdade para o mesmo dado. Também não foram adicionados
  enum de `status`, timestamps nem endpoints, por não terem sido pedidos.
- **Tipo da data.** `due_date` é do tipo `date` (um dia de prazo), e não
  `timestamp` — evita inventar um horário.
- **`guid` não declarado.** O XanoScript gera o `guid` no push; o arquivo local
  recebeu o valor do servidor após o envio.
- **Push isolado.** A tabela `subjects` já existia no workspace, mas o envio de
  `academic_tasks` foi feito isoladamente
  (`xano workspace push --branch v1 --include "tables/academic_tasks.xs"`)
  porque o CLI envia em ordem alfabética de caminho e `academic_tasks` viria
  antes de `subjects`.
- **Nenhum push automático pela IA (REGRA Nº 2).** O push ao Xano foi executado
  manualmente pelo desenvolvedor; a IA gerou e validou os arquivos.
- **Enunciado corrigido contra a realidade do repositório.** O enunciado cita
  `docs/*_guideline.md` e a Paleta de Comandos do XanoScript, que não existem
  neste repositório; o fluxo real usa o Xano CLI. A REGRA Nº 4 foi mantida, com a
  nota de que os guidelines são a documentação do XanoScript.

---

5. PRÓXIMO PASSO

O Módulo 2 continua: expor os endpoints REST (CRUD) para as tabelas do backend e
integrar o frontend ao Xano.

---

Aluno: Wender Araujo Santos · Faculdade Impacta · 2026
