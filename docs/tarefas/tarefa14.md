# Tarefa 14 – Busca Avançada Híbrida (Xano + Python)

[← Voltar ao índice](../../README.md#tarefas)

---

Aluno: Wender Araujo Santos  
Disciplina: Innovation Lab: Desenvolvimento Avançado No/Low Code  
Módulo: 2 – Ciclo de Mudança com IA, Python e XanoScript  

---

A funcionalidade de busca avançada híbrida combina a capacidade de consulta e filtragem do backend Xano com lógica analítica em Python, permitindo que o estudante filtre suas disciplinas pelo nome ou encontre rapidamente quais disciplinas possuem tarefas acadêmicas atrasadas e pendentes de entrega.

---

## 1. O QUE FOI FEITO

- **Change OpenSpec `busca-avancada-inteligente`**: criada seguindo o ciclo Spec-Driven Development com `proposal.md`, `specs/subjects/spec.md` (delta com `## ADDED Requirements`), `design.md` e `tasks.md`.
- **Validação e Arquivamento**: validada com `openspec validate busca-avancada-inteligente --strict` e arquivada em `openspec/changes/archive/2026-11-11-busca-avancada-inteligente/`, atualizando a especificação permanente `openspec/specs/subjects/spec.md`.
- **Script Auxiliar Python (`scripts/search_overdue_subjects.py`)**:
  - Implementa lógica pura Python para detecção de tarefas atrasadas (`due_date < data_atual` e `status != completed`).
  - Funções `get_overdue_subject_ids()`, `filter_overdue_subjects()` e `handle(data)` prontas para teste local e integração como custom function / microserviço.
  - Cobertura de testes embutida (`__main__`) validando cenários de sucesso, tarefas concluídas no prazo e tarefas vencidas.
- **Endpoint XanoScript (`apis/autenticacao_edutrack_ia_est/subjects_search_GET.xs`)**:
  - `GET /subjects/search` adicionado ao grupo de API existente `AutenticacaoEduTrackIAEst`.
  - Suporte ao parâmetro de busca parcial por nome `q` via `ilike` case-insensitive.
  - Suporte ao parâmetro booleano `overdue=true` integrando a detecção analítica de pendências.
  - Escopo rigoroso por `$auth.id`.
- **Branch e Pull Request**:
  - Branch: `feat/hybrid-search`
  - Pull Request #12 no repositório de estudante (`origin`), merged na `main`.
  - Repositório pessoal (`personal`, `WenderAKAD/EduTrack-AI`) sincronizado e espelhado com a branch e o merge da `main`.

---

## 2. SEGURANÇA E ISOLAMENTO DE DADOS (`user_id`)

- **Autenticação obrigatória (`auth = ""`):** Nenhuma busca é permitida sem token JWT válido.
- **Filtro de Disciplinas:** A busca só recupera disciplinas pertencentes ao usuário logado (`where = $db.subjects.user_id == $auth.id`).
- **Filtro de Tarefas Acadêmicas:** A consulta a `academic_tasks` garante que nenhuma tarefa de outro usuário seja processada, vinculando a verificação à disciplina pertencente ao usuário autenticado (`academic_tasks.subject_id.user_id == $auth.id`).

---

## 3. ENTREGÁVEIS

- [x] Fluxo OpenSpec completo (proposal → spec delta → design → tasks → validate → archive).  
      `openspec/changes/archive/2026-11-11-busca-avancada-inteligente/`
- [x] Script analítico em Python para detecção de pendências e tarefas atrasadas.  
      `scripts/search_overdue_subjects.py`
- [x] Endpoint `.xs` do endpoint de busca no repositório.  
      `apis/autenticacao_edutrack_ia_est/subjects_search_GET.xs`
- [x] Pull Request e merge na branch `main` espelhado em ambos os repositórios (estudante e pessoal).
- [ ] Push manual do endpoint para o backend Xano (conforme REGRA Nº 2 do projeto).  
      `xano workspace push --branch v1 --include "apis/autenticacao_edutrack_ia_est/subjects_search_GET.xs"`
- [ ] Teste no Swagger / Run & Debug do Xano com evidências registradas em `docs/evidencias/tarefa14/`.

---

## 4. CRITÉRIOS DE AVALIAÇÃO ATENDIDOS

- [x] **Spec-Driven Development:** Mudança documentada, validada de forma estrita e integrada ao catálogo de specs permanentes.
- [x] **Hibridismo Xano + Python:** Integração conceitual e prática entre filtros do banco de dados relacional e lógica em Python.
- [x] **Segurança por Token:** Isolamento completo de dados por usuário.
- [x] **Sincronização Dupla Git:** Espelhamento entre o repositório acadêmico institucional e o portfólio pessoal.

---

## 5. PRÓXIMO PASSO

Avançar para a **Tarefa 15** assim que os requisitos forem definidos.

---

Aluno: Wender Araujo Santos · Faculdade Impacta · 2026
