// Get Teste1 record
query "teste1/{teste1_id}" verb=GET {
  api_group = "Event Logs"

  input {
    int teste1_id? filters=min:1
  }

  stack {
    db.get "" {
      field_name = "id"
      field_value = $input.teste1_id
    } as $teste1
  
    precondition ($teste1 != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $teste1
}