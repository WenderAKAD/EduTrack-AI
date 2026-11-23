// Cadastra um usuario e devolve um token de autenticacao com validacao previa de codigo.
//
// POST /auth/signup — valida se o codigo de verificacao enviado e valido e
// nao expirou na tabela email_verification. Se valido, cria a conta na tabela
// "user" e ja devolve o JWT.
//
// Grupo reusado (Tarefa 07/13): o token vale para os endpoints subjects, que
// leem $auth.id. Nome do grupo exatamente como esta no servidor.
//
// Change: openspec/changes/email-verification-xano.
query "auth/signup" verb=POST {
  api_group = "Autenticacao EduTrackIA Est"
  description = "Cadastra um usuario apos validar o codigo de verificacao de e-mail e devolve o token JWT."

  input {
    text name? filters=trim
    email email? filters=lower|trim
    password password? filters=min:8|minAlpha:1|minDigit:1
    text verification_code? filters=trim
  }

  stack {
    precondition ($input.verification_code != null && $input.verification_code != "") {
      error_type = "badrequest"
      error = "Codigo de verificacao e obrigatorio."
    }

    // Valida se o email ja existe em user
    db.get user {
      field_name = "email"
      field_value = $input.email
    } as $existing

    precondition ($existing == null) {
      error_type = "accessdenied"
      error = "Este e-mail ja esta em uso."
    }

    // Busca o codigo mais recente na tabela email_verification
    db.query email_verification {
      where = $db.email_verification.email == $input.email && $db.email_verification.code == $input.verification_code
      sort = {field: "created_at", direction: "desc"}
      return = {type: "single"}
    } as $verification

    // Regra estrita de bloqueio: codigo precisa existir e nao estar expirado
    precondition ($verification != null) {
      error_type = "accessdenied"
      error = "Codigo de verificacao invalido."
    }

    precondition ($verification.expires_at > "now") {
      error_type = "accessdenied"
      error = "Codigo de verificacao expirado. Solicite um novo."
    }

    // Cria a conta do usuario no Xano
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

    // Marca codigo como verificado
    db.edit email_verification {
      field_name = "id"
      field_value = $verification.id
      data = {
        verified: true
      }
    }

    security.create_auth_token {
      table = "user"
      extras = {}
      expiration = 86400
      id = $user.id
    } as $authToken
  }

  response = {authToken: $authToken}
  guid = "Xb8e9FHf__WhvjSAQiaWf0ie4aQ"
}
