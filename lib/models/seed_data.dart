/// Static placeholder data for the Tarefa 09 shell. No API is called by any
/// page (spec `app-navigation`): values below are intentional stand-ins for the
/// data that the Xano endpoints of the next task will provide.
library;

enum TaskStatus { done, pending, late }

class Subject {
  const Subject({
    required this.name,
    required this.professor,
    required this.workload,
    required this.progress,
  });

  final String name;
  final String professor;
  final String workload;
  final int progress;
}

class TaskItem {
  const TaskItem({
    required this.title,
    required this.due,
    required this.status,
  });

  final String title;
  final String due;
  final TaskStatus status;
}

abstract final class SeedData {
  static const List<Subject> subjects = [
    Subject(
      name: 'Programação Avançada',
      professor: 'Prof. C. Martins',
      workload: '60h',
      progress: 88,
    ),
    Subject(
      name: 'Banco de Dados',
      professor: 'Prof. A. Ribeiro',
      workload: '72h',
      progress: 74,
    ),
    Subject(
      name: 'Redes de Computadores',
      professor: 'Prof. M. Tanaka',
      workload: '64h',
      progress: 61,
    ),
    Subject(
      name: 'Empreendedorismo',
      professor: 'Prof. R. Souza',
      workload: '48h',
      progress: 42,
    ),
    Subject(
      name: 'Inovação e Startups',
      professor: 'Prof. L. Ferraz',
      workload: '56h',
      progress: 35,
    ),
    Subject(
      name: 'UX & Prototipagem',
      professor: 'Prof. B. Almeida',
      workload: '40h',
      progress: 51,
    ),
  ];

  static const List<TaskItem> tasks = [
    TaskItem(title: 'Relatório do módulo 2', due: '08/10', status: TaskStatus.late),
    TaskItem(title: 'Exercício de SQL', due: '10/10', status: TaskStatus.pending),
    TaskItem(title: 'Lab de redes', due: '07/10', status: TaskStatus.done),
    TaskItem(title: 'Pitch de produto', due: '12/10', status: TaskStatus.pending),
    TaskItem(title: 'Protótipo navegável', due: '14/10', status: TaskStatus.pending),
    TaskItem(title: 'Revisão da paleta', due: '13/10', status: TaskStatus.done),
    TaskItem(title: 'Entrega da Tarefa 09', due: '07/10', status: TaskStatus.late),
    TaskItem(title: 'Modelagem do banco', due: '16/10', status: TaskStatus.done),
  ];

  static const int overallProgress = 72;
  static const int pendingTasks = 12;
  static const int lateTasks = 3;
  static const int subjectCount = 6;
  static const int atRiskSubjects = 2;
}