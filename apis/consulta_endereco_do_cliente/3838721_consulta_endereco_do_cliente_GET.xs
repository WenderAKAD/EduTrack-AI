query ConsultaEnderecoDoCliente verb=GET {
  api_group = "ConsultaEnderecoDoCliente"

  input {
  }

  stack {
    api.request {
      url = ""
      method = "GET"
    } as $api1
  }

  response = $api1
}