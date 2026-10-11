import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

import '../models/seed_data.dart';
import '../theme/app_theme.dart';
import '../widgets/app_page_header.dart';
import '../widgets/task_tile.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        AppPageHeader(
          title: 'EduTrack AI',
          subtitle: 'semestre 2026.2',
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
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(20),
            child: Center(
              child: ConstrainedBox(
                constraints: const BoxConstraints(maxWidth: 760),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.stretch,
                  children: [
                    const _KpiRow(),
                    const SizedBox(height: 16),
                    _Panel(
                      title: 'Progresso por disciplina',
                      child: Column(
                        children: [
                          for (final subject in SeedData.subjects)
                            _SubjectProgressRow(subject: subject),
                        ],
                      ),
                    ),
                    const SizedBox(height: 16),
                    _Panel(
                      title: 'Tarefas recentes',
                      child: Column(
                        children: [
                          for (final task in SeedData.tasks.take(4))
                            Padding(
                              padding: const EdgeInsets.only(bottom: 10),
                              child: TaskTile(task: task),
                            ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }
}

class _KpiRow extends StatelessWidget {
  const _KpiRow();

  @override
  Widget build(BuildContext context) {
    return const Row(
      children: [
        Expanded(
          child: _KpiCard(
            label: 'Progresso geral',
            value: '${SeedData.overallProgress}%',
            footer: '+6% no último mês',
            mono: false,
          ),
        ),
        SizedBox(width: 12),
        Expanded(
          child: _KpiCard(
            label: 'Tarefas pendentes',
            value: '${SeedData.pendingTasks}',
            footer: '${SeedData.lateTasks} com atraso',
            mono: true,
          ),
        ),
        SizedBox(width: 12),
        Expanded(
          child: _KpiCard(
            label: 'Disciplinas',
            value: '${SeedData.subjectCount}',
            footer: '${SeedData.atRiskSubjects} em risco',
            mono: false,
          ),
        ),
      ],
    );
  }
}

class _KpiCard extends StatelessWidget {
  const _KpiCard({
    required this.label,
    required this.value,
    required this.footer,
    required this.mono,
  });

  final String label;
  final String value;
  final String footer;
  final bool mono;

  @override
  Widget build(BuildContext context) {
    final scheme = Theme.of(context).colorScheme;
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: scheme.surface,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: scheme.outline),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            label.toUpperCase(),
            style: TextStyle(
              fontSize: 10,
              letterSpacing: 0.5,
              color: scheme.onSurfaceVariant,
            ),
          ),
          const SizedBox(height: 6),
          FittedBox(
            fit: BoxFit.scaleDown,
            alignment: Alignment.centerLeft,
            child: Text(
              value,
              style: TextStyle(
                fontFamily: mono ? 'JetBrainsMono' : 'Inter',
                fontSize: 26,
                fontWeight: FontWeight.w700,
                letterSpacing: -0.6,
                color: scheme.onSurface,
              ),
            ),
          ),
          const SizedBox(height: 4),
          Text(
            footer,
            maxLines: 2,
            overflow: TextOverflow.ellipsis,
            style: TextStyle(
              fontSize: 11,
              color: scheme.onSurfaceVariant,
            ),
          ),
        ],
      ),
    );
  }
}

class _Panel extends StatelessWidget {
  const _Panel({required this.title, required this.child});

  final String title;
  final Widget child;

  @override
  Widget build(BuildContext context) {
    final scheme = Theme.of(context).colorScheme;
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: scheme.surface,
        borderRadius: BorderRadius.circular(14),
        border: Border.all(color: scheme.outline),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            children: [
              Container(
                width: 3,
                height: 16,
                decoration: BoxDecoration(
                  color: scheme.brightness == Brightness.dark
                      ? AppColors.accentDark
                      : AppColors.accentLight,
                  borderRadius: BorderRadius.circular(2),
                ),
              ),
              const SizedBox(width: 8),
              Text(title, style: Theme.of(context).textTheme.titleMedium),
            ],
          ),
          const SizedBox(height: 14),
          child,
        ],
      ),
    );
  }
}

class _SubjectProgressRow extends StatelessWidget {
  const _SubjectProgressRow({required this.subject});

  final Subject subject;

  @override
  Widget build(BuildContext context) {
    final scheme = Theme.of(context).colorScheme;
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(
                subject.name,
                style: const TextStyle(fontSize: 13),
              ),
              Text(
                '${subject.progress}%',
                style: TextStyle(
                  fontFamily: 'JetBrainsMono',
                  fontSize: 12,
                  color: scheme.onSurfaceVariant,
                ),
              ),
            ],
          ),
          const SizedBox(height: 6),
          ClipRRect(
            borderRadius: BorderRadius.circular(6),
            child: LinearProgressIndicator(
              value: subject.progress / 100,
              minHeight: 6,
              color: AppColors.primary,
              backgroundColor: scheme.outline.withValues(alpha: 0.5),
            ),
          ),
        ],
      ),
    );
  }
}