# Proposal

## Why

Atualmente, qualquer usuário pode criar uma conta no EduTrack AI informando qualquer e-mail no endpoint `POST /auth/signup` e no app web, sem comprovar posse ou legitimidade do endereço. Para garantir a segurança dos dados acadêmicos e integridade do banco de dados no Xano, é necessário introduzir uma validação com código temporário de 6 dígitos enviado por e-mail antes de efetivar o registro do usuário na tabela `user`.

## What Changes

- Criação da tabela `tables/email_verification.xs` no Xano para armazenar os códigos de validação gerados, data de expiração (15 minutos) e status de confirmação.
- Criação do endpoint `POST /auth/send-verification-code`: recebe o e-mail, verifica se já não está cadastrado na tabela `user`, gera um código numérico de 6 dígitos e registra na tabela `email_verification`.
- Atualização do endpoint `POST /auth/signup` com **regra estrita de bloqueio**: passa a exigir `verification_code` como input e valida se o código corresponde ao e-mail informado e está dentro da validade; caso contrário, a requisição é rejeitada com `accessdenied` ("Código de verificação inválido ou expirado").
- Atualização do frontend Streamlit (`app.py`): o cadastro e login passam a consumir diretamente a API do Xano (`AutenticacaoEduTrackIAEst`), com fluxo de envio e validação do código de verificação.

## Capabilities

### New Capabilities

- `email-verification`: geração e validação de códigos temporários de 6 dígitos para confirmação de e-mails de usuários.

### Modified Capabilities

- `user`: o cadastro (`POST /auth/signup`) passa a exigir validação prévia de e-mail por código temporário antes de inserir na tabela `user`.

## Impact

- **Novos arquivos:** `tables/email_verification.xs`, `apis/autenticacao_edutrack_ia_est/auth_send_verification_code_POST.xs`.
- **Arquivos modificados:** `apis/autenticacao_edutrack_ia_est/auth_signup_POST.xs`, `app.py`.
- **Banco Xano:** nova tabela `email_verification` e bloqueio de criação em `user` sem código válido.
- **Grupo de API:** `Autenticacao EduTrackIA Est` (Base URL `https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC`).
