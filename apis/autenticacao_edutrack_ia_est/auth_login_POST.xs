// Autentica um usuario e devolve um token de autenticacao.
//
// POST /auth/login — localiza a conta pelo email, confere a senha e emite o
// JWT. Email inexistente e senha errada devolvem a mesma mensagem, para nao
// revelar qual campo falhou.
//
// Grupo reusado (Tarefa 07/13): o token vale para os endpoints subjects.
//
// Change: openspec/changes/auth-endpoints.
query "auth/login" verb=POST {
  api_group = "Autenticacao EduTrackIA Est"
  description = "Autentica um usuario e devolve um token de autenticacao."

  input {
    email email? filters=lower|trim
    text password?
  }

  stack {
    db.get user {
      field_name = "email"
      field_value = $input.email
      output = ["id", "created_at", "name", "email", "password"]
    } as $user

    precondition ($user != null) {
      error_type = "accessdenied"
      error = "Invalid Credentials."
    }

    security.check_password {
      text_password = $input.password
      hash_password = $user.password
    } as $is_valid

    precondition ($is_valid) {
      error_type = "accessdenied"
      error = "Invalid Credentials."
    }

    security.create_auth_token {
      table = "user"
      extras = {}
      expiration = 86400
      id = $user.id
    } as $authToken
  }

  response = {authToken: $authToken}
}
