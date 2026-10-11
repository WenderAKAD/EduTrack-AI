# Evidências – Tarefa 10

Material e registro da entrega **Tarefa 10 – Configuração Avançada do AGENTS.md**.

| Arquivo | Descrição |
|---|---|
| `Tarefa10-entrega.html` | Documento de entrega (versão editável) |
| `Tarefa10-entrega.pdf` | Documento de entrega (versão final, 9 páginas) |
| `resposta-ia.png` | Print da resposta da IA confirmando a leitura do `AGENTS.md` |

## O que esta tarefa entregou

- `AGENTS.md` reescrito na raiz do repositório, com as quatro regras
  prioritárias, convenções de branch/commit, segurança (`user_id`) e o checklist
  de validação OpenSpec.
- Proposta de teste `feature-notas-atividades` criada, validada e arquivada em
  `openspec/changes/archive/2026-10-08-feature-notas-atividades/`.
- Cópia do material de entrega versionada neste diretório.

## Evidência da IA

- **Screenshot da resposta da IA** (`resposta-ia.png`): o agente confirmou que leu
  o `AGENTS.md` da raiz e acertou as quatro perguntas do teste de leitura — nome
  do projeto, prefixos de branch, estrutura de Proposal no OpenSpec e o filtro
  obrigatório por `user_id`.

## Verificação

```bash
openspec status --change "feature-notas-atividades"   # 4/4 artifacts complete
openspec validate feature-notas-atividades --strict   # is valid
openspec list                                         # nenhuma change ativa de teste
openspec validate --specs --strict                    # subjects e user válidas
```