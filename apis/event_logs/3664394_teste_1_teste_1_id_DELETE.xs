// Delete Teste1 record.
query "teste1/{teste1_id}" verb=DELETE {
  api_group = "Event Logs"

  input {
    int teste1_id? filters=min:1
  }

  stack {
    db.del "" {
      field_name = "id"
      field_value = $input.teste1_id
    }
  }

  response = null
}