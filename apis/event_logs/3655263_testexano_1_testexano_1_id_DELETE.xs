// Delete TesteXano1 record.
query "testexano1/{testexano1_id}" verb=DELETE {
  api_group = "Event Logs"

  input {
    int testexano1_id? filters=min:1
  }

  stack {
    db.del "" {
      field_name = "id"
      field_value = $input.testexano1_id
    }
  }

  response = null
}