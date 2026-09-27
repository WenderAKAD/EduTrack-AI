// Query all TRANSAÇÃO records
query transa_o verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $transa_o
  }

  response = $transa_o
}