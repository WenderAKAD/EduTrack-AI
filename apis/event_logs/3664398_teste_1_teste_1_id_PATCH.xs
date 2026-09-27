// Edit Teste1 record
query "teste1/{teste1_id}" verb=PATCH {
  api_group = "Event Logs"

  input {
    int teste1_id? filters=min:1
    dblink {
      table = ""
    }
  }

  stack {
    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input
  
    db.patch "" {
      field_name = "id"
      field_value = $input.teste1_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $teste1
  }

  response = $teste1
}