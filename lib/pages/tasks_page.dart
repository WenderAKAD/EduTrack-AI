import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

import '../models/seed_data.dart';
import '../theme/app_theme.dart';
import '../widgets/app_page_header.dart';
import '../widgets/task_tile.dart';

class TasksPage extends StatelessWidget {
  const TasksPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        AppPageHeader(
          title: 'Tarefas',
          subtitle: '8 próximas entregas',
          trailing: IconButton(
            tooltip: 'Nova tarefa',
            onPressed: () {},
            icon: SvgPicture.asset(
              'assets/icons/add-task.svg',
              width: 22,
              height: 22,
              colorFilter: const ColorFilter.mode(
                AppColors.primary,
                BlendMode.srcIn,
              ),
            ),
          ),
        ),
        Expanded(
          child: Center(
            child: ConstrainedBox(
              constraints: const BoxConstraints(maxWidth: 760),
              child: ListView.builder(
                padding: const EdgeInsets.all(20),
                itemCount: SeedData.tasks.length,
                itemBuilder: (context, index) {
                  return Padding(
                    padding: const EdgeInsets.only(bottom: 10),
                    child: TaskTile(task: SeedData.tasks[index]),
                  );
                },
              ),
            ),
          ),
        ),
      ],
    );
  }
}