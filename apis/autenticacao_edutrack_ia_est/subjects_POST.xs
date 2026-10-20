// Cria uma disciplina para o usuario autenticado.
//
// POST /subjects — name, teacher e hours vem do body (obrigatorios, como na
// tabela). user_id NAO e input: e gravado no db.add a partir de $auth.id, o
// id do JWT. Assim um aluno nao consegue criar disciplina em nome de outro.
//
// Change: openspec/changes/api-crud-disciplinas (Tarefa 13).
query "subjects" verb=POST {
  api_group = "AutenticacaoEduTrackIAEst"
  auth = ""
  description = "Cria uma disciplina do usuario autenticado."

  input {
    text name? filters=trim
    text teacher? filters=trim
    int hours? filters=min:1
  }

  stack {
    db.add subjects {
      enforce_hidden_fields = false
      data = {
        name    : $input.name
        teacher : $input.teacher
        hours   : $input.hours
        user_id : $auth.id
      }
    } as $subject
  }

  response = $subject
}
