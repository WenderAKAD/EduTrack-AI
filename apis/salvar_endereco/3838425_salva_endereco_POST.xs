query salvaEndereco verb=POST {
  api_group = "salvarEndereco"

  input {
    text logradouro? filters=trim
    text Numero? filters=trim
    text Bairro? filters=trim
    text Complemento? filters=trim
    text Referencia? filters=trim
    text cep? filters=trim
    text Cidade? filters=trim
    text Estado? filters=trim
    bool padrao?
    int cliente_id? {
      table = ""
    }
  }

  stack {
    api.request {
      url = ""
      method = "GET"
    } as $api1
  }

  response = $api1
}