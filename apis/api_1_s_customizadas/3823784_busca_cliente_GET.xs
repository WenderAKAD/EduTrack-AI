// Dado um authToken, devolve dados do Cliente
query buscaCliente verb=GET {
  api_group = "API1s customizadas"

  input {
    // Token de autenticação
    text authtoken? filters=trim
  }

  stack {
    api.request {
      url = "https://x8ki-letl-twmt.n7.xano.io/api:ZWbTfCcn/auth/me"
      method = "GET"
      params = $input.authtoken
      headers = [
        "Authorization: Bearer " ~ $input.authtoken
        "Content-Type: application/json"
      ]
    
    } as $api1
  
    conditional {
      if ($api1.response.status == 200) {
        db.get "" {
          field_name = "user_id"
          field_value = `$var.api1.response.result.id`
        } as $CLIENTE1
      }
    
      else {
        var $CLIENTE1 {
          value = {}
        }
      }
    }
  }

  response = $CLIENTE1
}