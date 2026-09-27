// Query all PEDIDO records
query pedido verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $pedido
  }

  response = $pedido
}