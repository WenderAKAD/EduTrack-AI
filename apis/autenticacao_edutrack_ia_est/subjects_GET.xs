// Lista as disciplinas do usuario autenticado.
//
// GET /subjects — le as disciplinas do proprio usuario. O filtro
// user_id == $auth.id e obrigatorio (AGENTS.md, Seguranca): um aluno nunca
// enxerga as disciplinas de outro. auth = "user" faz o Xano validar o JWT antes
// de o stack rodar.
//
// Change: openspec/changes/api-crud-disciplinas (Tarefa 13).
// Grupo reusado da Tarefa 07: https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC
query "subjects" verb=GET {
  api_group = "Autenticacao EduTrackIA Est"
  auth = "user"
  description = "Lista as disciplinas do usuario autenticado."

  input {
  }

  stack {
    db.query subjects {
      where = $db.subjects.user_id == $auth.id
      return = {type: "list"}
    } as $subjects
  }

  response = $subjects
  guid = "TBH62ELFxZ8UIQMbuYuMfwGMvOs"
}
