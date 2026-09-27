// Query all STATUS_TTOKENIZACAO records
query status_ttokenizacao verb=GET {
  api_group = "Event Logs"

  input {
  }

  stack {
    db.query "" {
      return = {type: "list"}
    } as $status_ttokenizacao
  }

  response = $status_ttokenizacao
}