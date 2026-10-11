# Tarefa 08 – Uso do OpenSpec para Planejar Mudanças

[← Voltar ao índice](../../README.md#tarefas)

---

Aluno: Wender Araujo Santos
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code
Módulo: 1 – Introdução ao Spec-Driven Development

Primeira aplicação real do Spec-Driven Development no EduTrack AI: duas
changes criadas, implementadas, validadas e arquivadas, produzindo as duas
primeiras tabelas do projeto.

---

1. O QUE FOI FEITO

- `AGENTS.md` configurado na raiz do projeto com as regras do enunciado:
  nomenclatura em inglês para código, `snake_case` no banco, `kebab-case` nas
  proposals, e a regra de segurança de que toda query filtra por `user_id`.
- Change `create-subjects-table` criada com os quatro artifacts que o schema
  `spec-driven` exige: `proposal.md`, `specs/subjects/spec.md`, `design.md` e
  `tasks.md`.
- A spec da change gerou `openspec/specs/subjects/spec.md` com 4 requirements
  e 12 scenarios, cobrindo estrutura da tabela, posse do registro, validação de
  campos, isolamento entre usuários e a descrição de posse da tabela.
- `tables/subjects.xs` implementado e enviado ao Xano (tabela id `904017`),
  com `id` auto-incrementado, `name` com `trim`, `teacher`, `hours` com
  `filters=min:1` e `user_id` como relationship obrigatório. A tabela também
  declara a `description` exigida pela spec.
- Durante a implementação descobriu-se que a tabela `user` **não existia** no
  workspace: o workspace tinha 194 objetos e zero tabelas. O arquivo
  `addons/109599_user.xs`, que aparentava ser essa tabela, é um addon
  corrompido com `table = ""` e `db.query ""`.
- Change `create-user-table` criada para corrigir isso: 5 requirements e 13
  scenarios, menghasilkan `openspec/specs/user/spec.md`.
- `tables/user.xs` implementado com `auth = true` e enviado ao Xano (tabela id
  `904016`), desbloqueando a relationship de `subjects.user_id`.
- Ambas as changes validadas com `openspec validate --strict` e arquivadas com
  `openspec archive`, o que gerou as specs mestras em `openspec/specs/`.
  Total: 9 requirements e 25 scenarios. Todas as tasks das duas changes estão
  marcadas (`subjects` 11/11, `user` 15/15).

---

2. ENTREGÁVEIS

- [x] Proposal da change `create-subjects-table`.
      Arquivo: openspec/changes/archive/2026-10-05-create-subjects-table/proposal.md
- [x] Spec da change `create-subjects-table`.
      Arquivo: openspec/specs/subjects/spec.md
- [x] Design da change `create-subjects-table`.
      Arquivo: openspec/changes/archive/2026-10-05-create-subjects-table/design.md
- [x] Tasks da change `create-subjects-table`.
      Arquivo: openspec/changes/archive/2026-10-05-create-subjects-table/tasks.md
- [x] Arquivo de configuração do agente de IA.
      Arquivo: AGENTS.md
- [x] Implementação da tabela `subjects` em XanoScript.
      Arquivo: tables/subjects.xs
- [x] Link do repositório GitHub com o README atualizado (este arquivo).
      https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est (PR #5
      merged — https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est/pull/5)

&nbsp;

Change adicional, criada por dependência técnica e não prevista no enunciado:

- [x] Proposal, spec, design e tasks da change `create-user-table`.
      Arquivo: openspec/changes/archive/2026-10-05-create-user-table/
- [x] Spec mestra da tabela `user`.
      Arquivo: openspec/specs/user/spec.md
- [x] Implementação da tabela `user` em XanoScript.
      Arquivo: tables/user.xs

---

3. CRITÉRIOS DE AVALIAÇÃO

- [x] Executar o slash command `/openspec:proposal` para criar a primeira
      proposal do projeto.
      Executado pelo slash command `/opsx:propose`, o mesmo fluxo do
      `/openspec:proposal`. A change `create-subjects-table` foi gerada por ele
      e arquivada com proposal, spec, design e tasks. O Gemini Code Assist não
      está autenticado nesta máquina, então o slash command foi invocado a
      partir do Antigravity, que é a IA registrada na Tarefa 02. Detalhado na
      seção 4.
- [x] Gerar a tabela `subjects` com os campos `id` (automático), `name`
      (texto), `teacher` (texto), `hours` (inteiro) e `user_id` (vínculo com
      o usuário autenticado).
      Confirmado no dashboard do Xano: tabela `904017` com os 5 campos.
- [x] Garantir que todas as tabelas refiram ao usuário via `user_id`.
      `subjects.user_id` é relationship obrigatório para `user`, com índice
      btree. A regra está fixada na spec, em `design.md` e em `AGENTS.md`.
- [x] Versionar os arquivos `.xs` gerados.
      `tables/subjects.xs` e `tables/user.xs` versionados no repositório.
- [x] Push para o Xano e validação no dashboard.
      Ambas as tabelas confirmadas no dashboard, com relationship resolvida.

---

4. OBSERVAÇÕES TÉCNICAS

- **A tabela `user` não vinha pronta no Xano.** O `AGENTS.md` do enunciado
  afirma que ela já existe. Isso é falso para este workspace: os 194 objetos
  do workspace são 176 endpoints, 10 API groups, 5 functions, 1 tool, 1 agent
  e 1 addon — nenhuma tabela. A regra foi corrigida no `AGENTS.md` e a tabela
  passou a ser criada pelo projeto, em change própria.

- **`addons/109599_user.xs` não é uma tabela.** É um addon (bloco de lógica
  reutilizável, sintaxe `addon user { ... }`) e está corrompido: carrega
  `table = ""` e `db.query ""`. Foi ele que deu a impressão de que a tabela
  `user` existia. Vale notar que o próprio Xano gera essa referência quebrada
  ao criar FKs, então outros arquivos do repositório também a carregam.

- **A ordem de push é uma restrição real.** O CLI envia documentos em ordem
  alfabética de caminho, e `tables/subjects.xs` ordena antes de
  `tables/user.xs`. Um push combinado deixaria o relationship de `user_id`
  como referência não resolvida. Por isso as duas tabelas foram enviadas em
  pushes separados, `user` primeiro. Isso está registrado em `design.md` e na
  task 3.3 de `create-user-table`.

- **A extensão `xano.xanoscript` foi descontinuada.** O aviso aparece ao fazer
  login. A Tarefa 08 migrou para o Xano CLI (`@xano/cli` 1.3.3) com o
  `xano.xanoscript-language-server` 0.3.3, usando `--include` para enviar
  apenas os arquivos do EduTrack AI entre os 198 do repositório.

- **O formato do enunciado é de uma versão antiga do OpenSpec.** O enunciado
  descreve `## Why:` e `specs/spec.md`; a versão 1.13.2 usa `## Why` sem
  dois-pontos, e `specs/<capability>/spec.md`. A spec de `subjects` também
  precisou de `design.md`, porque `tasks` declara `requires: [specs, design]`.

- **A limpeza dos 194 objetos de template do Xano ficou pendente.** Foi
  registrada na seção "Pendências Técnicas" deste README, junto de outros
  quatro itens. Nenhum bloqueia as tarefas 01 a 08.

- **Um item de sync ficou aberto de propósito.** O `user_id` criado
  manualmente no dashboard é uma self-reference que o app não usa. Ele está
  declarado em `tables/user.xs` sem o atributo `methods`, que a documentação
  da Xano não descreve, então o dry-run sempre reporta `UPDATE_FIELD`. A
  decisão foi não dar push nessa tabela de novo: com o campo declarado, o CLI
  nunca propõe o `DROP_FIELD` que o removeria do servidor.

- **Houve uma consolidação da change `create-subjects-table`.** A primeira
  versão arquivada partia da premissa de que a tabela `user` já existia no
  workspace, o que se provou falso. Ela foi removida e substituída pela versão
  gerada pelo slash command `/opsx:propose`, que declara `user` como
  dependência e não como tabela pré-existente. A spec mestra foi sincronizada
  com o delta: 4 requirements e 12 scenarios, incluindo o requirement da
  `description` da tabela.

- **Comandos por nome de change só funcionam antes do arquivamento.**
  `openspec validate create-subjects-table --strict` respondia `valid` enquanto
  a change estava ativa; depois de arquivada passa a responder
  `Unknown item 'create-subjects-table'`, porque o nome só é resolvido em
  `openspec/changes/`. O estado atual se verifica com
  `openspec validate --specs --strict` (2 passed, 0 failed), que valida as
  specs mestras. O `[INFO]` deRequirement longo que aparece ali é aviso de
  estilo, não erro.

---

5. PRÓXIMO PASSO

Tarefa 09 — criação dos endpoints da API no Xano, consumindo as tabelas
`user` e `subjects` já especificadas e implementadas.

---
