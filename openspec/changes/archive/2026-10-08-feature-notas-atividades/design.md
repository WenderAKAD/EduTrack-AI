# Design

## Context

Ver `proposal.md` — *Why* para a motivação e
`specs/activity-grades/spec.md` para os requisitos. Aqui ficam apenas as decisões
que moldam a abordagem.

- `user` e `subjects` já existem; esta change não as altera.
- O CLI do Xano envia documentos em ordem alfabética de caminho:
  `tables/activity_grades.xs` ordena **antes** de `tables/user.xs`, então um push
  combinado deixaria o relationship com `user` sem resolver.

## Goals / Non-Goals

**Goals:**

- Gravar a nota de um aluno em uma atividade, com posse garantida por `user_id`.
- Expor um único caminho de escrita: `POST /activity_grades`.

**Non-Goals:**

- Listar, editar ou remover notas — não foram pedidos.
- Qualquer tela de frontend para lançamento de notas.
- Cálculo de média, boletim ou relatórios.

## Decisions

**Escopo restrito ao lançamento.**
O pedido foi "permitir que o professor lance notas". Uma tabela e um endpoint de
escrita cobrem exatamente isso. As operações de leitura e edição entram quando
forem solicitadas, em change própria.
*Alternativa considerada:* entregar CRUD completo. Rejeitada — é escopo não
pedido e contraria a REGRA Nº 1 do `AGENTS.md`.

**`user_id` obrigatório e relationship com `user`.**
Mantém a regra de posse e isolamento do projeto: toda query filtra pelo usuário
autenticado, e o banco recusa uma linha sem dono.
*Alternativa considerada:* `user_id` como `int` solto. Rejeitada — tiraria a
garantia do banco.

## Risks / Trade-offs

- **Ordem de push** — `activity_grades` antes de `user` deixaria o FK sem
  resolver → *Mitigação:* dar push de `tables/activity_grades.xs` em separado,
  depois de confirmar que `tables/user.xs` já está no workspace.