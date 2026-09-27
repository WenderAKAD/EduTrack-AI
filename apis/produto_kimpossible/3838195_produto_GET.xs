// Query all PRODUTO records
query produto verb=GET {
  api_group = "ProdutoKimpossible"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $model
  }

  response = $model
}