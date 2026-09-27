// Query all STATUS_TRANSAÇÃO records
query status_transa_o verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $status_transa_o
  }

  response = $status_transa_o
}