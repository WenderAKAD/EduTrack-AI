// Add TesteXano1 record
query testexano1 verb=POST {
  api_group = "Event Logs"

  input {
    dblink {
      table = ""
    }
  }

  stack {
    db.add "" {
      enforce_hidden_fields = false
      data = {created_at: "now"}
    } as $testexano1
  }

  response = $testexano1
}