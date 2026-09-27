// Get TesteXano1 record
query "testexano1/{testexano1_id}" verb=GET {
  api_group = "Event Logs"

  input {
    int testexano1_id? filters=min:1
  }

  stack {
    db.get "" {
      field_name = "id"
      field_value = $input.testexano1_id
    } as $testexano1
  
    precondition ($testexano1 != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $testexano1
}