// Query all Teste1 records
query teste1 verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $teste1
  }

  response = $teste1
}