# Evidências – Tarefa 12

Material e registro da entrega **Tarefa 12 – Integração Python Básica**.

| Arquivo | Descrição |
|---|---|
| `Tarefa12-entrega.html` | Documento de entrega (versão editável) |
| `Tarefa12-entrega.pdf` | Documento de entrega (versão final) |
| `saida-terminal.txt` | Saída real capturada de `python3 scripts/calculate_progress.py` |
| `teste-saida-terminal.png` | Figura da saída do terminal (reproduz o `saida-terminal.txt`) |

## O que esta tarefa entregou

- Change OpenSpec `logica-calculo-progresso` com os quatro artifacts
  (`proposal`, `specs`, `design`, `tasks`), validada e arquivada em
  `openspec/changes/archive/2026-10-15-logica-calculo-progresso/`.
- Spec mestra `openspec/specs/progress-calculation/spec.md`.
- Script `scripts/calculate_progress.py` — função customizada em Python puro
  (apenas built-ins, importa só `json`), com contrato JSON
  `{"tasks": [...]}` → `{"percentage": ...}`.
- Merge do PR #10 (`feat/python-progress`) na `main` em 15/10/2026.

## Verificação do teste

```bash
python3 scripts/calculate_progress.py
# {"percentage": 50.0}
# {"percentage": 100.0}
# {"percentage": 0}
# {"percentage": 66.67}

python3 -m py_compile scripts/calculate_progress.py   # sem erros
```

## Cópia para a pasta de entregas

O material também está em `../../DMAtividades/12Atividade/`
(`Tarefa12-entrega.html` e `.pdf`), no mesmo padrão das tarefas 01 a 11.
