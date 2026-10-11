# Proposal

## Why

O EduTrack AI ainda não registra notas. As tabelas `user` e `subjects` existem,
mas não há onde armazenar a nota que o professor atribui a um aluno em uma
atividade específica. Sem esse registro, o acompanhamento de desempenho — objetivo
central do app — não tem dado de origem.

## What Changes

- Nova tabela `activity_grades`, que guarda a nota de um aluno em uma atividade
  específica, vinculada ao usuário logado por `user_id`.
- Novo endpoint `POST /activity_grades`, que permite ao professor lançar a nota
  de um aluno em uma atividade.

Fora de escopo, por não terem sido pedidos: listagem (`GET`), edição (`PATCH`),
remoção (`DELETE`) e qualquer tela de frontend.

## Capabilities

### New Capabilities

- `activity-grades`: o registro da nota de um aluno em uma atividade específica,
  com posse por `user_id` e o endpoint que a grava.

### Modified Capabilities

None. `subjects` e `user` existem e não mudam de comportamento.

## Impact

- **Banco:** nova tabela `activity_grades`. Como o CLI envia documentos em ordem
  alfabética de caminho e `tables/activity_grades.xs` ordena antes de
  `tables/user.xs`, o push da tabela referencia `user` e deve ser feito em push
  separado, depois de a tabela `user` existir.
- **API:** novo endpoint `POST /activity_grades`.
- **Sem frontend** e sem alteração nas tabelas existentes.