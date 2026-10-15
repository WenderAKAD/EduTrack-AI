// Tabela de tarefas academicas do EduTrack AI (licoes, provas e trabalhos).
//
// Nome da tabela em snake_case, conforme AGENTS.md.
// A coluna subject_id e o vinculo com a tabela subjects, criada em
// tables/subjects.xs (change create-subjects-table). A posse do registro e
// herdada de subjects.user_id — por isso esta tabela nao repete user_id.
//
// Atencao a ordem de push: o CLI ordena por caminho e academic_tasks.xs vem
// antes de subjects.xs. Esta tabela deve ser enviada em push separado, depois
// que subjects ja existir no workspace.
//
// Especificacao: openspec/specs/academic-tasks/spec.md
table academic_tasks {
  auth = false

  description = "Tarefas academicas do EduTrack AI (licoes, provas e trabalhos). Cada tarefa pertence a uma disciplina via subject_id, e a posse e herdada de subjects.user_id."

  schema {
    // Chave primaria auto-incrementada
    int id

    // Titulo da tarefa
    text title filters=trim

    // Descricao livre da tarefa
    text description

    // Prazo de entrega (data sem horario)
    date due_date

    // Situacao da tarefa (ex.: pendente, concluida)
    text status filters=trim

    // Disciplina a que a tarefa pertence. Obrigatorio.
    int subject_id {
      table = "subjects"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "subject_id"}]}
  ]
  guid = "yRDl_ymhTx-etC9WEq-J-TNnlZQ"
}
