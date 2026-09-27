// Add TOKENS record
query tokens verb=POST {
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
    } as $tokens
  }

  response = $tokens
}