// Busca hibrida de disciplinas: nome no banco (Xano) + atraso no Python.
//
// GET /subjects/search aceita dois filtros opcionais na query string:
//   q       -> busca por nome, parcial e case-insensitive (operador ilike,
//              resolvido no banco pelo Xano);
//   overdue -> "true" devolve apenas disciplinas com pelo menos uma tarefa
//              atrasada e nao concluida, calculado pela custom function
//              search_overdue_subjects (scripts/search_overdue_subjects.py).
// Os dois filtros combinam quando enviados juntos (nome E atraso).
//
// Seguranca (AGENTS.md): subjects e filtrado por user_id == $auth.id e
// academic_tasks pela posse herdada via subject_id -> subjects.user_id.
// Nenhum dado de outro usuario sai do banco. auth = "" faz o Xano validar
// o JWT antes de o stack rodar.
//
// Change: openspec/changes/busca-avancada-inteligente (Tarefa 14).
// Grupo reusado da Tarefa 07: https://x8ki-letl-twmt.n7.xano.io/api:JBdUmIAC
query "subjects/search" verb=GET {
  api_group = "AutenticacaoEduTrackIAEst"
  auth = ""
  description = "Busca hibrida de disciplinas por nome (Xano) e por tarefas atrasadas (Python)."

  input {
    text q? filters=trim
    text overdue? filters=trim|lower
  }

  stack {
    // Lado Xano: disciplinas do usuario, com filtro de nome quando q existe.
    conditional {
      if ($input.q == null) {
        db.query subjects {
          where = $db.subjects.user_id == $auth.id
          return = {type: "list"}
        } as $subjects
      }

      else {
        db.query subjects {
          where = $db.subjects.user_id == $auth.id && $db.subjects.name ilike ("%" ~ $input.q ~ "%")
          return = {type: "list"}
        } as $subjects
      }
    }

    // Sem atraso: devolve a busca por nome.
    var $result {
      value = $subjects
    }

    // Lado Python: mantem apenas disciplinas com tarefa atrasada nao concluida.
    conditional {
      if ($input.overdue == "true") {
        db.query academic_tasks {
          where = $db.academic_tasks.subject_id.user_id == $auth.id
          return = {type: "list"}
        } as $tasks

        function.run "search_overdue_subjects" {
          input = {
            tasks   : $tasks
            subjects: $subjects
          }
        } as $overdue_result

        var $result {
          value = $overdue_result.subjects
        }
      }
    }
  }

  response = $result
}
