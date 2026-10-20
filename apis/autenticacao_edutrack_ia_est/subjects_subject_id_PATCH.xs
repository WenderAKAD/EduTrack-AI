// Atualiza uma disciplina do usuario autenticado.
//
// PATCH /subjects/{subject_id} — o registro e lido primeiro (db.get) para que
// duas precondiciones rodem antes de qualquer escrita:
//   notfound     quando o id nao existe;
//   accessdenied quando subject.user_id != $auth.id (dono).
// O merge e parcial: util.get_raw_input devolve o body cru e os campos
// enviados sao aplicados sem apagar os demais.
//
// Change: openspec/changes/api-crud-disciplinas (Tarefa 13).
query "subjects/{subject_id}" verb=PATCH {
  api_group = "AutenticacaoEduTrackIAEst"
  auth = ""
  description = "Atualiza uma disciplina do usuario autenticado."

  input {
    int subject_id? filters=min:1
    text name? filters=trim
    text teacher? filters=trim
    int hours? filters=min:1
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
      error = "Sem permissao para alterar esta disciplina."
    }

    util.get_raw_input {
      encoding = "json"
      exclude_middleware = false
    } as $raw_input

    db.patch subjects {
      field_name = "id"
      field_value = $input.subject_id
      data = `$input|pick:($raw_input|keys)`|filter_null|filter_empty_text
    } as $updated
  }

  response = $updated
}
