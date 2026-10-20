// Deleta uma disciplina do usuario autenticado.
//
// DELETE /subjects/{subject_id} — mesmo desenho do PATCH: db.get + precondi-
// coes notfound e accessdenied (dono) antes do db.del. Um aluno que adivinhe
// o id de outro recebe accessdenied e a linha alheia nao e tocada.
//
// Observacao: tarefas vinculadas (academic_tasks.subject_id) nao sao removi-
// das em cascata — regra fora do escopo desta change (ver design.md).
//
// Change: openspec/changes/api-crud-disciplinas (Tarefa 13).
query "subjects/{subject_id}" verb=DELETE {
  api_group = "AutenticacaoEduTrackIAEst"
  auth = ""
  description = "Deleta uma disciplina do usuario autenticado."

  input {
    int subject_id? filters=min:1
  }

  stack {
    db.get subjects {
      field_name = "id"
      field_value = $input.subject_id
    } as $subject

    precondition ($subject != null) {
      error_type = "notfound"
      error = "Disciplina nao encontrada."
    }

    precondition ($subject.user_id == $auth.id) {
      error_type = "accessdenied"
      error = "Sem permissao para deletar esta disciplina."
    }

    db.del subjects {
      field_name = "id"
      field_value = $input.subject_id
    }
  }

  response = null
}
