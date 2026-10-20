# Tasks

## 1. Endpoints de autenticação

- [ ] 1.1 Criar `apis/autenticacao_edutrack_ia_est/auth_signup_POST.xs` — `POST /auth/signup` com `name`, `email` e `password`, checagem de e-mail duplicado (`accessdenied`), `db.add user` e `security.create_auth_token`
- [ ] 1.2 Criar `apis/autenticacao_edutrack_ia_est/auth_login_POST.xs` — `POST /auth/login` com `email` e `password`, `db.get user` + `security.check_password` (`Invalid Credentials`) e `security.create_auth_token`
- [ ] 1.3 Conferir os dois arquivos com o parser da extensão XanoScript (sem erros de sintaxe)

## 2. Validação OpenSpec

- [ ] 2.1 Rodar `openspec validate auth-endpoints --strict` e conferir que a change passa

## 3. Push para o Xano (passo manual do desenvolvedor)

- [ ] 3.1 Confirmar que a tabela de auth `user` existe no workspace antes do push
- [ ] 3.2 Enviar os dois endpoints (`xano workspace push --branch v1 --include "api/autenticacao_edu_track_ia_est/auth*"`)
- [ ] 3.3 Testar com dois usuários: signup + login de cada um e uso do token nos CRUD de `subjects`, confirmando o isolamento por usuário

## 4. Arquivar

- [ ] 4.1 Arquivar com `openspec archive auth-endpoints` e confirmar que `openspec/specs/authentication/spec.md` foi gerado
