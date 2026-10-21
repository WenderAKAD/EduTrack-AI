# Tasks

## 1. Python helper for overdue detection
- [ ] 1.1 Criar `scripts/search_overdue_subjects.py` com função para identificar subject_ids com tarefas atrasadas e não concluídas (lógica pura Python, sem dependências externas)
- [ ] 1.2 Testar o script localmente com dados de exemplo

## 2. Xano endpoint for hybrid search
- [ ] 2.1 Criar `apis/autenticacao_edutrack_ia_est/subjects_search_GET.xs` endpoint `GET /subjects/search` com `auth = ""`
- [ ] 2.2 Implementar filtro por nome (`q`) com busca parcial case-insensitive
- [ ] 2.3 Implementar filtro por tarefas atrasadas (`overdue=true`) integrando com lógica Python
- [ ] 2.4 Garantir filtro obrigatório por `user_id` do usuário autenticado

## 3. Validação e documentação
- [ ] 3.1 Rodar `openspec validate busca-avancada-inteligente --strict`
- [ ] 3.2 Testar endpoint no Xano (Swagger/Run & Debug)
- [ ] 3.3 Criar branch `feat/hybrid-search`, commitar seguindo Conventional Commits
