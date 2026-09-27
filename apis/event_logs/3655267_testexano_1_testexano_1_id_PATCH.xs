// Edit TesteXano1 record
query "testexano1/{testexano1_id}" verb=PATCH {
  api_group = "Event Logs"

  input {
    int testexano1_id? filters=min:1
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
      field_value = $input.testexano1_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $testexano1
  }

  response = $testexano1
}