// Delete TRANSACAO record.
query "transacao/{transacao_id}" verb=DELETE {
  api_group = "Event Logs"

  input {
    int transacao_id? filters=min:1
  }

  stack {
    db.del "" {
      field_name = "id"
      field_value = $input.transacao_id
    }
  }

  response = null
}