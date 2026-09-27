// Query all CLIENTE records
query cliente verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $cliente
  }

  response = $cliente
}