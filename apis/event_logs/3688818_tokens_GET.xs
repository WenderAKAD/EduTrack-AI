// Query all TOKENS records
query tokens verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $tokens
  }

  response = $tokens
}