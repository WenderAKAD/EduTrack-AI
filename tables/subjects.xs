// Tabela de disciplinas do EduTrack AI — primeira entidade de dominio.
//
// Nome da tabela em snake_case, conforme AGENTS.md.
// A coluna user_id e o vinculo com a tabela de autenticacao "user", que ja
// existe no workspace do Xano. Toda leitura deve filtrar por user_id.
//
// Especificacao: openspec/specs/subjects/spec.md
table subjects {
  auth = false

  schema {
    // Chave primaria auto-incrementada
    int id

    // Nome da disciplina
    text name filters=trim

    // Docente responsavel
    text teacher

    // Carga horaria semanal
    int hours filters=min:1

    // Dono do registro. Obrigatorio: toda disciplina pertence a um usuario.
    int user_id {
      table = "user"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "user_id"}]}
  ]
}