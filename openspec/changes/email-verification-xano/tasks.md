# Tasks

## 1. Specification and OpenSpec
- [x] 1.1 Criar proposal.md com justificativa, impacto e capacidades
- [x] 1.2 Criar spec delta com ADDED Requirements para tabela e endpoints
- [x] 1.3 Criar design.md documentando decisões de arquitetura e segurança

## 2. XanoScript backend definitions
- [x] 2.1 Criar tabela `tables/email_verification.xs` com schema e indices
- [x] 2.2 Criar endpoint `apis/autenticacao_edutrack_ia_est/auth_send_verification_code_POST.xs`
- [x] 2.3 Atualizar `apis/autenticacao_edutrack_ia_est/auth_signup_POST.xs` com regra de bloqueio por verification_code

## 3. Frontend Streamlit integration
- [x] 3.1 Integrar `app.py` para usar os endpoints do Xano (`/auth/send-verification-code`, `/auth/signup`, `/auth/login`)
- [x] 3.2 Implementar fluxo de dois passos na interface (enviar código -> cadastrar com código)

## 4. Sincronização e Git
- [x] 4.1 Sincronizar arquivos para o repositório pessoal (`EduTrack-AI-Perfil`)
- [ ] 4.2 Executar `python3 scripts/update_status_page.py`
- [ ] 4.3 Commitar e fazer push em ambos os repositórios (`origin/main` e `personal/main`)
