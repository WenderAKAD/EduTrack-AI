// Add STATUS_TRANSAÇÃO record
query status_transa_o verb=POST {
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
    } as $status_transa_o
  }

  response = $status_transa_o
}