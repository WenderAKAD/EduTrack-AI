// Get STATUS_TRANSAÇÃO record
query "status_transa_o/{status_transa_o_id}" verb=GET {
  api_group = "Event Logs"

  input {
    int status_transa_o_id? filters=min:1
  }

  stack {
    db.get "" {
      field_name = "id"
      field_value = $input.status_transa_o_id
    } as $status_transa_o
  
    precondition ($status_transa_o != null) {
      error_type = "notfound"
      error = "Not Found."
    }
  }

  response = $status_transa_o
}