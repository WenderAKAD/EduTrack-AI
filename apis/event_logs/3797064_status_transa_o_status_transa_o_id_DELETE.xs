// Delete STATUS_TRANSAÇÃO record.
query "status_transa_o/{status_transa_o_id}" verb=DELETE {
  api_group = "Event Logs"

  input {
    int status_transa_o_id? filters=min:1
  }

  stack {
    db.del "" {
      field_name = "id"
      field_value = $input.status_transa_o_id
    }
  }

  response = null
}