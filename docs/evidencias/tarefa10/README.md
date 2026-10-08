# Evidências – Tarefa 10

Material e registro da entrega **Tarefa 10 – Configuração Avançada do AGENTS.md**.

| Arquivo | Descrição |
|---|---|
| `Tarefa10-entrega.html` | Documento de entrega (versão editável) |
| `Tarefa10-entrega.pdf` | Documento de entrega (versão final, 8 páginas) |

## O que esta tarefa entregou

- `AGENTS.md` reescrito na raiz do repositório, com as quatro regras
  prioritárias, convenções de branch/commit, segurança (`user_id`) e o checklist
  de validação OpenSpec.
- Proposta de teste `feature-notas-atividades` criada, validada e arquivada em
  `openspec/changes/archive/2026-10-08-feature-notas-atividades/`.
- Cópia do material de entrega versionada neste diretório.

## Evidência pendente (coleta manual)

- **Screenshot da resposta da IA** confirmando que leu as regras do `AGENTS.md`.
  Precisa ser capturado do chat do agente de IA — não é produzível por linha de
  comando. Depois de salvo, colocar o PNG neste diretório.

## Verificação

```bash
openspec status --change "feature-notas-atividades"   # 4/4 artifacts complete
openspec validate feature-notas-atividades --strict   # is valid
openspec list                                         # nenhuma change ativa de teste
openspec validate --specs --strict                    # subjects e user válidas
```