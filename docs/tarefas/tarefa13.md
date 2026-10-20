# Tarefa 13 – APIs CRUD para Disciplinas

[← Voltar ao índice](../../README.md#tarefas)

---

Aluno: Wender Araujo Santos
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code
Módulo: 2 – Ciclo de Mudança com IA, Python e XanoScript

Os endpoints REST da tabela `subjects` foram criados para que o cliente consiga
cadastrar novas disciplinas e trabalhar com várias delas ao mesmo tempo, sempre
restringido ao usuário autenticado via JWT.

---

1. O QUE FOI FEITO

- Change OpenSpec `api-crud-disciplinas` criada com os quatro artifacts do
  schema `spec-driven`: `proposal.md`, `specs/subjects/spec.md` (delta
  `## ADDED Requirements` na capability existente), `design.md` e `tasks.md`.
- Validada com `openspec validate api-crud-disciplinas --strict` (change
  válida) e arquivada com `openspec archive`, atualizando a spec mestra
  `openspec/specs/subjects/spec.md`.
- Quatro endpoints criados em `apis/autenticacao_edutrack_ia_est/`, reusando o
  grupo de API da Tarefa 07 (mesma Base URL do FlutterFlow):
  - `subjects_GET.xs` — `GET /subjects` com `auth = ""` e
    `where = $db.subjects.user_id == $auth.id`;
  - `subjects_POST.xs` — `POST /subjects` com `user_id = $auth.id` gravado no
    `db.add` (nunca vem do body);
  - `subjects_subject_id_PATCH.xs` — `PATCH /subjects/{subject_id}` com
    `db.get` + preconditions `notfound`/`accessdenied` e merge parcial;
  - `subjects_subject_id_DELETE.xs` — `DELETE /subjects/{subject_id}` com o
    mesmo desenho de posse do PATCH.
- Os quatro arquivos passaram no parser oficial da extensão XanoScript 0.5.12
  (`xanoscriptParser`), sem erros de sintaxe.
- Branch de trabalho: `feat/api-crud-subjects`.

---

2. SEGURANÇA (user_id)

- Todo endpoint exige JWT (`auth = ""`); requisição sem token é recusada
  antes de qualquer acesso ao banco.
- `GET` filtra por `user_id == $auth.id` — um aluno nunca lista disciplinas de
  outro.
- `POST` ignora qualquer `user_id` enviado no body e grava o id do token.
- `PATCH` e `DELETE` carregam o registro e recusam com `accessdenied` quando
  `$subject.user_id != $auth.id`, além de responderem `notfound` para id
  inexistente.

---

3. ENTREGÁVEIS

- [x] Fluxo OpenSpec completo (proposal → implementação → archive).
      `openspec/changes/archive/` e `openspec/specs/subjects/spec.md`
- [x] Quatro endpoints `.xs` no GitHub.
      `apis/autenticacao_edutrack_ia_est/subjects_*.xs`
- [ ] Push dos endpoints para o Xano (passo manual, REGRA Nº 2).
      `xano workspace push --branch v1 --include
      "apis/autenticacao_edutrack_ia_est/subjects*"`
- [ ] Screenshot do Swagger do Xano com os novos endpoints.
      `docs/evidencias/tarefa13/`

---

4. CRITÉRIOS DE AVALIAÇÃO

- [x] Fluxo OpenSpec correto (proposal, spec como delta, design, tasks,
      validate --strict, archive).
- [x] Filtro de segurança por usuário em todos os métodos.
- [ ] Endpoints CRUD funcionais no Xano (após o push manual).

---

5. OBSERVAÇÕES

- **Grupo de API reusado.** `AutenticacaoEduTrackIAEst` (Tarefa 07) recebe os
  endpoints em vez de um grupo novo: evita mais um objeto no workspace já
  poluído por templates (pendência nº 1) e mantém a Base URL que o FlutterFlow
  já usa.
- **Sem `GET /subjects/{id}`.** O enunciado lista POST, GET, PATCH e DELETE; a
  leitura de uma disciplina específica é atendida pelo filtro da lista.
- **Deletar disciplina não remove `academic_tasks` filhas.** A cascata não foi
  pedida e fica registrada em `design.md` como risco para uma change futura.
- **Nenhum push automático pela IA (REGRA Nº 2).** Os endpoints estão gerados
  e validados; o push para o Xano, o teste no Run & Debug/Swagger (dois
  usuários distintos) e o screenshot são passos do desenvolvedor.

---

6. PRÓXIMO PASSO

Combinar essas APIs com as tarefas acadêmicas e o cálculo de progresso na
Tarefa 14.

---

Aluno: Wender Araujo Santos · Faculdade Impacta · 2026
