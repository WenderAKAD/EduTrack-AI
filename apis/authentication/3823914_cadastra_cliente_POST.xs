// Dado um conjunto de Nome, email,
// senha, celular, cpf e status salvar cada dado em
// sua respectiva tabela.
query cadastraCliente verb=POST {
  api_group = "Authentication"

  input {
    text nome? filters=trim
    text email? filters=trim
    text password? filters=trim
    text cpf? filters=trim
    text celular? filters=trim
    text status_do_cliente? filters=trim
  }

  stack {
    api.request {
      url = "https://x8ki-letl-twmt.n7.xano.io/api:ZWbTfCcn/auth/signup"
      method = "POST"
      params = {
        name    : $input.nome
        email   : $input.email
        password: $input.se
        nha     : ``
      }
    
      headers = ["Content-Type: application/json"]
    } as $api1
  
    api.request {
      url = "https://x8ki-letl-twmt.n7.xano.io/api:ZWbTfCcn/auth/me"
      method = "GET"
      params = `$var.api1.response.result.authToken`
      headers = ["Authorization: Bearer " ~
      $var.api1.response.result.authToken,"Content-Type:
      application/json"]
    } as $api2
  
    db.query "" {
      where = $db.STATUS_CLIENTE.status == $input.status_do_cliente
      return = {type: "list"}
    } as $STATUS_CLIENTE1
  
    db.add "" {
      enforce_hidden_fields = false
      data = {
        nome             : $input.nome
        celular          : $input.celular
        cpf              : $input.cpf
        status_cliente_id: $var.STATUS_CLIENTE1[0].id
        user_id          : `$var.api2.response.result.id`
      }
    } as $CLIENTE1
  }

  response = {
    result2: ```
      {'user':$var.api2.response.result,'cliente':$var.CLIENTE1,'authT
      oken':$var.api1.response.result.authToken}
      ```
  }
}