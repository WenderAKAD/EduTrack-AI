// Signup and retrieve an authentication token
query "auth/signup" verb=POST {
  api_group = "Desafio"

  input {
    text name?
    email email? filters=lower|trim
    password password?
  }

  stack {
    db.get "" {
      field_name = "email"
      field_value = $input.email
    } as $USER
  
    precondition ($USER == null) {
      error_type = "accessdenied"
      error = "This account is already in use."
    }
  
    db.add "" {
      enforce_hidden_fields = false
      data = {
        created_at: "now"
        name      : $input.name
        email     : $input.email
        password  : $input.password
      }
    } as $USER
  
    security.create_auth_token {
      table = ""
      extras = {}
      expiration = 86400
      id = $USER.id
    } as $authToken
  }

  response = {authToken: $authToken}
}