// Tabela de codigos de verificacao de e-mail do EduTrack AI.
//
// Armazena codigos temporarios de 6 digitos para confirmacao de e-mail
// antes de registrar a conta na tabela "user".
//
// Especificacao: openspec/changes/email-verification-xano/specs/user/spec.md
table email_verification {
  auth = false

  description = "Codigos temporarios de verificacao de e-mail para cadastro de usuarios."

  schema {
    // Chave primaria auto-incrementada
    int id

    // E-mail de destino
    email email filters=trim|lower

    // Codigo numerico de 6 digitos
    text code filters=trim

    // Data e hora de expiracao do codigo (15 minutos apos criacao)
    timestamp expires_at

    // Indica se o codigo ja foi validado
    bool verified?=false

    // Momento da emissao do codigo
    timestamp created_at?=now
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "email"}]}
  ]
}
