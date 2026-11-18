# Evidências — Tarefa 14: Busca Avançada Híbrida (Xano + Python)

**Aluno:** Wender Araújo Santos  
**Disciplina:** Innovation Lab: Desenvolvimento Avançado No/Low Code  
**Módulo:** 2 – Ciclo de Mudança com IA, Python e XanoScript

---

## O que foi feito

- **Change OpenSpec:** `busca-avancada-inteligente` (proposal, design, specs delta com `## ADDED Requirements`, tasks) validada estritamente com `openspec validate busca-avancada-inteligente --strict` e arquivada em `openspec/changes/archive/2026-11-11-busca-avancada-inteligente/`.
- **Script Analítico em Python:** `scripts/search_overdue_subjects.py` com funções puras (`find_overdue_subject_ids`, `filter_overdue_subjects`, `handle`) sem dependências externas, validando tarefas atrasadas (`due_date < hoje` e `status != completed`).
- **Endpoint XanoScript:** `apis/autenticacao_edutrack_ia_est/subjects_search_GET.xs` adicionando `GET /subjects/search` ao grupo `Autenticacao EduTrackIA Est` (Base URL `https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC`).
- **Custom function XanoScript:** `functions/search_overdue_subjects.xs` com o porte da regra de atraso do Python (`status != completed` e `due_date < hoje`), usada pelo endpoint para filtrar as disciplinas em runtime.
- **Push Xano:** custom function e endpoint publicados no workspace `148813` (branch `v1`); GUIDs registrados em `functions/search_overdue_subjects.xs` e `apis/autenticacao_edutrack_ia_est/subjects_search_GET.xs`.
- **Parâmetros suportados:**
  - `q` (busca parcial e case-insensitive por nome da disciplina via `ilike` no Xano).
  - `overdue=true` (filtragem inteligente das disciplinas com tarefas acadêmicas vencidas via custom function `search_overdue_subjects`).
- **Segurança por Token:** Isolamento estrito de dados por usuário autenticado (`where = $db.subjects.user_id == $auth.id` e `academic_tasks.subject_id.user_id == $auth.id`).
- **Git & GitHub:** Branch `feat/hybrid-search`, Pull Request #12 merged na branch `main` e espelhado no repositório pessoal (`WenderAKAD/EduTrack-AI`).

---

## Arquivos versionados

- `scripts/search_overdue_subjects.py`
- `functions/search_overdue_subjects.xs`
- `apis/autenticacao_edutrack_ia_est/subjects_search_GET.xs`
- `openspec/changes/archive/2026-11-11-busca-avancada-inteligente/*`
- `openspec/specs/subjects/spec.md` (especificação mestra atualizada)
- `docs/tarefas/tarefa14.md`
- `docs/evidencias/tarefa14/Tarefa14-entrega.html`
- `docs/evidencias/tarefa14/Tarefa14-entrega.pdf`
- `docs/evidencias/tarefa14/saida-terminal.txt`

---

## Execução e teste local

Para rodar a validação do script auxiliar Python:
```bash
python3 scripts/search_overdue_subjects.py
```

Saída:
```json
{"overdue_subject_ids": [1], "subjects": [{"id": 1, "name": "Innovation Lab", "teacher": "Prof. Silva", "hours": 4}]}
```
