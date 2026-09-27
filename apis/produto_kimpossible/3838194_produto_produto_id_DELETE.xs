// Delete PRODUTO record
query "produto/{produto_id}" verb=DELETE {
  api_group = "ProdutoKimpossible"

  input {
    int produto_id? filters=min:1
  }

  stack {
    db.del "" {
      field_name = "id"
      field_value = $input.produto_id
    }
  }

  response = null
}