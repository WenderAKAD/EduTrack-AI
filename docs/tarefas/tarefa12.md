# Tarefa 12 – Integração Python Básica

[← Voltar ao índice](../../README.md#tarefas)

---

Aluno: Wender Araujo Santos
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code
Módulo: 2 – Ciclo de Mudança com IA, Python e XanoScript

A função de progresso de disciplina foi criada em Python puro seguindo o fluxo do
Spec-Driven Development: a mudança foi planejada, implementada, validada,
testada localmente e arquivada.

---

1. O QUE FOI FEITO

- Change OpenSpec `logica-calculo-progresso` criada com os quatro artifacts do
  schema `spec-driven`: `proposal.md`, `specs/progress-calculation/spec.md`,
  `design.md` e `tasks.md`.
- Validada com `openspec validate logica-calculo-progresso --strict` (change
  válida) e `openspec validate --specs --strict` (4 specs, 0 falhas).
- Script implementado em `scripts/calculate_progress.py`, usando **somente a
  biblioteca padrão** (`json`):
  - `calculate_progress(completed_tasks, total_tasks)` retorna
    `{"percentage": x}` entre `0` e `100`, arredondado em duas casas.
  - `calculate_subject_progress(tasks)` deriva concluídas e total a partir da
    lista de tarefas (status `completed`, sem espaços e caso-insensível).
  - `handle(payload)` faz a ponte JSON → JSON usada na integração.
- Tratamento de divisão por zero: quando `total_tasks <= 0`, retorna
  `{"percentage": 0}` em vez de levantar `ZeroDivisionError`.
- Teste local (`python3 scripts/calculate_progress.py`) com saídas de exemplo:
  `50.0`, `100.0`, `0`, `66.67`.
- Change arquivada com `openspec archive logica-calculo-progresso`, gerando a
  spec mestra `openspec/specs/progress-calculation/spec.md`.
- Branch de trabalho: `feat/python-progress`.

---

2. ENTREGÁVEIS

- [x] Script Python funcional e sem erros de sintaxe.
      Arquivo: `scripts/calculate_progress.py`
- [x] Fluxo OpenSpec completo (proposal → implementation → archive).
      `openspec/changes/archive/2026-10-15-logica-calculo-progresso/`
- [x] Spec mestra sincronizada.
      `openspec/specs/progress-calculation/spec.md`
- [x] Link do arquivo `calculate_progress.py` no GitHub.
      https://github.com/wenderaraujo-creator/EduTrack-IA-Wender-Est/blob/feat/python-progress/scripts/calculate_progress.py
- [x] Screenshot do teste do script (terminal local ou painel do Xano).
      `docs/evidencias/tarefa12/saida-terminal.txt` e
      `docs/evidencias/tarefa12/teste-saida-terminal.png`
- [x] Material de entrega versionado.
      `docs/evidencias/tarefa12/Tarefa12-entrega.html`, `.pdf`
      (cópia em `DMAtividades/12Atividade/`)

---

3. CRITÉRIOS DE AVALIAÇÃO

- [x] Script Python funcional e sem erros de sintaxe (`python3 -m py_compile`).
- [x] Uso correto do OpenSpec para documentar a mudança.
- [x] Lógica de tratamento de erro (divisão por zero) implementada.

---

4. OBSERVAÇÕES

- **Python puro, sem dependências externas.** O script importa apenas `json`.
  Funções customizadas no Xano rodam em ambiente restrito, em que nem toda
  biblioteca funciona — por isso o enunciado recomenda apenas built-ins.
- **Contrato JSON.** A entrada é `{"tasks": [...]}` e a saída é
  `{"percentage": ...}`, o formato que trafega entre o Xano e o script.
- **Definição de concluída.** Uma tarefa conta como concluída quando o `status`,
  após `trim` e `lower`, é igual a `completed`; qualquer outro valor conta como
  não concluída.
- **Nenhum push automático pela IA (REGRA Nº 2).** O script roda localmente; a
  publicação no Xano é passo manual do desenvolvedor — como no enunciado, o
  entregável é o arquivo no GitHub mais o teste.
- **Endpoint fora de escopo.** Expor o cálculo via API REST é a Tarefa 13.

---

5. PRÓXIMO PASSO

Vamos expor esses dados para o mundo através de APIs na Tarefa 13.

---

Aluno: Wender Araujo Santos · Faculdade Impacta · 2026
