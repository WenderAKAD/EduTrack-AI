// Dado um novo CEP, ex: 04048000, verificar se ele já está presente na tabela CEP
query buscaCEP verb=GET {
  api_group = "API1s customizadas"

  input {
    // CEP a ser pesquisado
    text cep? filters=trim
  }

  stack {
    db.query "" {
      where = $db.CEP.cep == $input.cep
      return = {type: "list"}
    } as $CEP1
  }

  response = $CEP1
}