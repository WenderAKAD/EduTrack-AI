// Gera e registra um codigo temporario de verificacao de e-mail.
//
// POST /auth/send-verification-code — verifica se o e-mail ja esta em uso
// na tabela user. Se nao estiver, gera um codigo de 6 digitos e grava na
// tabela email_verification com validade de 15 minutos (now + 900000ms).
//
// Grupo: Autenticacao EduTrackIA Est
// Change: openspec/changes/email-verification-xano.
query "auth/send-verification-code" verb=POST {
  api_group = "Autenticacao EduTrackIA Est"
  description = "Gera e registra um codigo temporario de verificacao de e-mail para novo usuario."

  input {
    email email? filters=lower|trim
  }

  stack {
    precondition ($input.email != null && $input.email != "") {
      error_type = "badrequest"
      error = "Informe um e-mail valido."
    }

    db.get user {
      field_name = "email"
      field_value = $input.email
    } as $existing_user

    precondition ($existing_user == null) {
      error_type = "accessdenied"
      error = "Este e-mail ja esta em uso."
    }

    // Gera codigo aleatorio de 6 digitos
    var $code {
      value = 100000 + (random() * 899999)|round
    }

    // Expiracao de 15 minutos
    var $expires {
      value = "now"|timestamp_add:15:"minutes"
    }

    // Registra na tabela email_verification
    db.add email_verification {
      data = {
        email      : $input.email
        code       : $code|to_string
        expires_at : $expires
        verified   : false
        created_at : "now"
      }
    } as $verification_entry
  }

  response = {
    status  : "ok"
    message : "Codigo de verificacao gerado com sucesso."
    code    : $code|to_string
  }
}
