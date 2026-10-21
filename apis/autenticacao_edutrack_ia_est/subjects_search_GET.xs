// Busca hibrida: filtra disciplinas por nome ou por tarefas atrasadas.
query "subjects/search" verb=GET {
  api_group = "Autenticacao EduTrackIA Est"
  auth = ""
  description = "Busca hibrida de disciplinas por nome e por tarefas atrasadas."

  input {
    text q?
    text overdue?
  }

  stack {
    db.query subjects {
      where = $db.subjects.user_id == $auth.id
      return = {type: "list"}
    } as $all_subjects

    conditional {
      if ($input.overdue == "true") {
        db.query academic_tasks {
          return = {type: "list"}
        } as $all_tasks

        function.run "search_overdue_subjects" {
          input = {tasks: $all_tasks}
        } as $overdue_result
      }
    }
  }

  response = $all_subjects
}
