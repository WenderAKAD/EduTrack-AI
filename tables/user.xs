// Tabela de autenticação do EduTrack AI.
//
// auth = true torna esta a tabela de autenticação do workspace. É daqui que os
// endpoints leem $auth.id e é o alvo do user_id em tables/subjects.xs.
//
// `password` é sensitive para nunca aparecer em query. `email` NÃO é sensitive
// porque o login precisa ler o valor para localizar a conta.
//
// Atenção à ordem de push: o CLI envia em ordem alfabética de caminho e
// subjects.xs ordena antes de user.xs. Esta tabela precisa ir em um push
// separado, antes.
//
// Especificação: openspec/specs/user/spec.md
table user {
  auth = true

  schema {
    // Chave primária auto-incrementada
    int id

    // Nome do aluno
    text name filters=trim

    // E-mail de login. Único e normalizado para minúsculas.
    email email filters=trim|lower

    // Senha. A política de força é validada no schema, não no endpoint.
    password password filters=min:8|minAlpha:1|minDigit:1 {
      sensitive = true
    }

    // Conta ativa. Contas desativadas são preservadas, não removidas.
    bool is_active?=true

    // Momento do cadastro
    timestamp created_at?=now

    // Preenchido quando a conta for alterada
    timestamp updated_at?
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree|unique", field: [{name: "email"}]}
  ]
}