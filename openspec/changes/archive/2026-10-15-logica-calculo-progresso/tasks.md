# Tasks

## 1. Script Python

- [x] 1.1 Criar `scripts/calculate_progress.py` com apenas a biblioteca padrão (`json`)
- [x] 1.2 Implementar `calculate_progress(completed_tasks, total_tasks)` retornando `{"percentage": ...}` entre `0` e `100`
- [x] 1.3 Tratar divisão por zero: quando `total_tasks <= 0`, retornar `{"percentage": 0}`
- [x] 1.4 Implementar `calculate_subject_progress(tasks)`, derivando concluídas e total da lista (status `completed`, caso-insensível e sem espaços)
- [x] 1.5 Rodar `python scripts/calculate_progress.py` e conferir as saídas de exemplo sem erro
- [x] 1.6 Rodar `openspec validate logica-calculo-progresso --strict` e conferir que a change passa

## 2. Arquivar

- [x] 2.1 Arquivar com `openspec archive logica-calculo-progresso` e confirmar que `openspec/specs/progress-calculation/spec.md` foi gerado

## 3. Entrega

- [ ] 3.1 Publicar a mudança em uma branch `feat/python-progress` e abrir o Pull Request
- [ ] 3.2 Anexar o screenshot do teste do script (execução local ou painel do Xano)
