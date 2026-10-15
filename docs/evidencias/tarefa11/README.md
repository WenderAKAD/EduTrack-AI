# Evidências – Tarefa 11

Material e registro da entrega **Tarefa 11 – Adicionar Tabela Tarefas via
XanoScript**.

| Arquivo | Descrição |
|---|---|
| `Tarefa11-entrega.html` | Documento de entrega (versão editável) |
| `Tarefa11-entrega.pdf` | Documento de entrega (versão final, 7 páginas) |
| `xano-academic-tasks.png` | Print do painel do Xano com a tabela `academic_tasks` |

## O que esta tarefa entregou

- Change OpenSpec `create-academic-tasks-table` com os quatro artifacts
  (`proposal`, `specs`, `design`, `tasks`), validada e arquivada em
  `openspec/changes/archive/2026-10-15-create-academic-tasks-table/`.
- Spec mestra `openspec/specs/academic-tasks/spec.md` (4 requirements).
- Tabela `tables/academic_tasks.xs` criada no XanoScript, com os campos `id`,
  `title`, `description`, `due_date`, `status` e o relacionamento
  `subject_id` → `subjects`.
- Tabela `academic_tasks` criada no backend do Xano (workspace 148813, branch
  `v1`) pelo push manual do aluno.
- Cópia do material de entrega versionada neste diretório.

## Evidência do Xano

- **Screenshot do painel do Xano** (`xano-academic-tasks.png`): mostra a tabela
  `academic_tasks` com os seis campos e o relacionamento `subject_id` ligado à
  tabela `subjects`.

## Verificação

```bash
git branch --show-current                               # feat/tabela-tarefas
openspec validate --specs --strict                      # academic-tasks, subjects e user válidas
grep -n "guid" tables/academic_tasks.xs                 # guid gerado no push
```
