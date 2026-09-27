// Query all STATUS_CLIENTE records
query status_cliente verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $status_cliente
  }

  response = $status_cliente
}