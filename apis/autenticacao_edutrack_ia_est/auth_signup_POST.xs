// Cadastra um usuario e devolve um token de autenticacao.
//
// POST /auth/signup — cria a conta na tabela de auth "user" e ja devolve o
// JWT, para o cliente nao precisar chamar /auth/login na sequencia. O email
// duplicado e recusado com accessdenied (espelha o indice unico de user.email).
//
// Grupo reusado (Tarefa 07/13): o token vale para os endpoints subjects, que
// leem $auth.id. Nome do grupo exatamente como esta no servidor.
//
// Change: openspec/changes/auth-endpoints.
query "auth/signup" verb=POST {
  api_group = "Autenticacao EduTrackIA Est"
  description = "Cadastra um usuario e devolve um token de autenticacao."

  input {
    text name? filters=trim
    email email? filters=lower|trim
    password password? filters=min:8|minAlpha:1|minDigit:1
  }

  stack {
    db.get user {
      field_name = "email"
      field_value = $input.email
    } as $existing

    precondition ($existing == null) {
      error_type = "accessdenied"
      error = "Este e-mail ja esta em uso."
    }

    db.add user {
      enforce_hidden_fields = false
      data = {
        name       : $input.name
        email      : $input.email
        password   : $input.password
        is_active  : true
        created_at : "now"
      }
    } as $user

    security.create_auth_token {
      table = "user"
      extras = {}
      expiration = 86400
      id = $user.id
    } as $authToken
  }

  response = {authToken: $authToken}
}
