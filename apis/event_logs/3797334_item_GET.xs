// Query all ITEM records
query item verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $item
  }

  response = $item
}