// Query all TRANSACAO records
query transacao verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $transacao
  }

  response = $transacao
}