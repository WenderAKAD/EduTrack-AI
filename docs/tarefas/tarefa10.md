# Tarefa 10 – Configuração Avançada do AGENTS.md

[← Voltar ao índice](../../README.md#tarefas)

---

Aluno: Wender Araujo Santos
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code
Módulo: 1 – Introdução ao Spec-Driven Development

O `AGENTS.md` da raiz foi reescrito com a camada avançada de regras que a IA
deve seguir ao codificar o EduTrack AI. Como prova de que as regras funcionam,
uma proposta OpenSpec de teste foi criada, validada e arquivada.

---

1. O QUE FOI FEITO

- `AGENTS.md` da raiz reescrito com as quatro regras prioritárias: **(1)**
  escopo de tarefas (só o que foi pedido), **(2)** a IA não faz push/deploy,
  **(3)** ordem de precedência de instruções e **(4)** obrigação de consultar os
  guidelines do XanoScript antes de criar/editar `.xs`.
- Convenções adicionadas: código em inglês, banco em `snake_case`, branches
  `feat/`/`fix/`/`docs/` e Conventional Commits.
- Segurança fixada como regra mandatória: toda query filtra por `user_id` do
  usuário autenticado; APIs REST (`GET`/`POST`/`PATCH`/`DELETE`).
- Checklist de validação OpenSpec e dois exemplos de `spec.md` (válido vs. o que
  falha) incorporados ao arquivo.
- O bloco gerenciado pelo framework
  `<!-- OPENSPEC:START --> … <!-- OPENSPEC:END -->` foi **preservado intacto**.
- Proposta de teste `feature-notas-atividades` criada com os quatro artifacts do
  schema `spec-driven` (`proposal.md`, `specs/activity-grades/spec.md`,
  `design.md`, `tasks.md`), validada (`4/4 artifacts complete`,
  `is valid`) e arquivada em
  `openspec/changes/archive/2026-10-08-feature-notas-atividades/`.

---

2. ENTREGÁVEIS

- [x] Conteúdo completo do `AGENTS.md`.
      Arquivo: `AGENTS.md` (raiz do repositório)
- [x] Proposta OpenSpec criada e arquivada.
      `openspec/changes/archive/2026-10-08-feature-notas-atividades/`
- [x] Link do repositório GitHub.
      https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est
- [x] Screenshot da resposta da IA confirmando que leu as regras.
      Arquivo: `docs/evidencias/tarefa10/resposta-ia.png`
- [x] Material de entrega versionado.
      `docs/evidencias/tarefa10/Tarefa10-entrega.html`, `.pdf` e `resposta-ia.png`

---

3. CRITÉRIOS DE AVALIAÇÃO

- [x] `AGENTS.md` presente na raiz do repositório.
- [x] Instruções claras sobre as tecnologias (Xano, FlutterFlow, OpenSpec).
- [x] Definição de padrões de commit e nomenclatura.
- [x] Proposta OpenSpec criada e arquivada.
- [x] README do repositório atualizado com o progresso.
      Este arquivo.

---

4. OBSERVAÇÕES TÉCNICAS

- **Escopo da proposta de teste foi respeitado.** O pedido foi "permitir que o
  professor lance notas", então o `tasks.md` contém apenas a tabela
  `activity_grades` e o endpoint `POST /activity_grades` — sem `GET`, `PATCH`,
  `DELETE` nem tela, que não foram pedidos.
- **Arquivada sem integrar spec permanente.** A proposta de teste não foi
  implementada, então foi movida para `changes/archive/` em vez de rodar
  `openspec archive`. O `archive` fundiria o delta nas specs de `openspec/specs/`,
  registrando a capability `activity-grades` como se existisse. A própria tarefa
  prevê a movimentação manual como alternativa.
- **Enunciado corrigido contra a realidade do repositório.** A tabela é `user`
  (criada pelo projeto em `tables/user.xs`, Tarefa 08), não `users`; os arquivos
  `docs/*_guideline.md` do XanoScript não estão versionados aqui; e os comandos
  slash ficam em `.gemini/commands/opsx/`, não `.../openspec/`.
- **Nenhum push ao Xano.** Conforme a REGRA Nº 2, os arquivos foram apenas
  gerados; o envio é responsabilidade do desenvolvedor.
- **A IA leu o `AGENTS.md`.** No teste de leitura, o agente confirmou a leitura
  do arquivo da raiz e acertou as quatro perguntas (nome do projeto, prefixo de
  branch, estrutura de Proposal no OpenSpec e o filtro por `user_id`). Print em
  `docs/evidencias/tarefa10/resposta-ia.png`.

---

5. PRÓXIMO PASSO

Módulo 2 — criação das funcionalidades reais do backend no Xano, começando pelos
endpoints de `subjects` e `user`.

---

Data de entrega: 6 de outubro de 2026
Aluno: Wender Araujo Santos

---
