// Gera e registra um codigo temporario de verificacao de e-mail e dispara via SendGrid.
//
// POST /auth/send-verification-code — verifica se o e-mail ja esta em uso
// na tabela user. Se nao estiver, gera um codigo de 6 digitos, grava na
// tabela email_verification com validade de 15 minutos (now + 900000ms) e
// dispara o e-mail real via SendGrid quando configurado no workspace.
//
// Grupo: Autenticacao EduTrackIA Est
// Change: openspec/changes/email-verification-xano.
query "auth/send-verification-code" verb=POST {
  api_group = "Autenticacao EduTrackIA Est"
  description = "Gera e registra um codigo temporario de verificacao de e-mail para novo usuario e dispara via SendGrid."

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

    // Se o SendGrid estiver configurado no Xano (sendgrid_api_key), dispara o e-mail real
    conditional {
      if ($env.workspace.sendgrid_api_key != null && $env.workspace.sendgrid_api_key != "") {
        function.run "sendgrid_basic_send" {
          input = {
            to_email : $input.email
            subject  : "EduTrack AI - Seu codigo de verificacao: " ~ ($code|to_string)
            body     : "Ola!\n\nSeu codigo de verificacao no EduTrack AI e: " ~ ($code|to_string) ~ "\n\nEste codigo expira em 15 minutos.\nSe voce nao solicitou este cadastro, desconsidere esta mensagem."
          }
        }
      }
    }
  }

  response = {
    status  : "ok"
    message : "Codigo de verificacao enviado com sucesso."
    code    : $code|to_string
  }
}
