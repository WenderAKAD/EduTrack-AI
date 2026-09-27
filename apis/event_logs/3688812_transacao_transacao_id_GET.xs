// Get TRANSACAO record
query "transacao/{transacao_id}" verb=GET {
  api_group = "Event Logs"

  input {
    int transacao_id? filters=min:1
  }

  stack {
    db.get "" {
      field_name = "id"
      field_value = $input.transacao_id
    } as $transacao
  
    precondition ($transacao != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $transacao
}