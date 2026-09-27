// Query all SOLCANCELAMENTO records
query solcancelamento verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $solcancelamento
  }

  response = $solcancelamento
}