// Get PRODUTO record
query "produto/{produto_id}" verb=GET {
  api_group = "ProdutoKimpossible"

  input {
    int produto_id? filters=min:1
  }

  stack {
    db.get "" {
      field_name = "id"
      field_value = $input.produto_id
    } as $model
  
    precondition ($model != null) {
      error_type = "notfound"
      error = "Not Found"
    }
  }

  response = $model
}