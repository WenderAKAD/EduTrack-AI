// Porte XanoScript da logica de scripts/search_overdue_subjects.py.
//
// Recebe as tarefas academicas e as disciplinas ja filtradas por nome/usuario
// e devolve somente as disciplinas com pelo menos uma tarefa nao concluida
// vencida (status != completed e due_date < hoje), espelhando a regra Python.
//
// Change: openspec/changes/busca-avancada-inteligente (Tarefa 14).
function search_overdue_subjects {
  input {
    json tasks
    json subjects
  }

  stack {
    var $today {
      value = (now|format_timestamp:"Y-m-d":"America/Sao_Paulo")
    }

    var $overdue_subject_ids {
      value = []
    }

    foreach ($input.tasks) {
      each as $task {
        conditional {
          if (($task.status|to_lower|trim) != "completed" && ($task.due_date|to_text) < $today) {
            var.update $overdue_subject_ids {
              value = $overdue_subject_ids|push:$task.subject_id
            }
          }
        }
      }
    }

    var $result {
      value = []
    }

    foreach ($input.subjects) {
      each as $subject {
        conditional {
          if ($overdue_subject_ids|some:$$ == $subject.id) {
            var.update $result {
              value = $result|push:$subject
            }
          }
        }
      }
    }
  }

  response = {subjects: $result}
  guid = "CZ3mhJm5I7sh38nQJzQBEO0Ulbw"
}
