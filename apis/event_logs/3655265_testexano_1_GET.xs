// Query all TesteXano1 records
query testexano1 verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $testexano1
  }

  response = $testexano1
}