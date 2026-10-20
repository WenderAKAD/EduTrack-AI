import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

import '../models/seed_data.dart';
import '../theme/app_theme.dart';

class TaskTile extends StatelessWidget {
  const TaskTile({super.key, required this.task});

  final TaskItem task;

  @override
  Widget build(BuildContext context) {
    final scheme = Theme.of(context).colorScheme;
    final isDark = Theme.of(context).brightness == Brightness.dark;

    final (icon, tagColor) = switch (task.status) {
      TaskStatus.done => ('assets/icons/check.svg', AppColors.success),
      TaskStatus.late => (
          'assets/icons/clock.svg',
          isDark ? AppColors.accentDark : AppColors.accentLight,
        ),
      TaskStatus.pending => (
          'assets/icons/clock.svg',
          scheme.onSurfaceVariant,
        ),
    };

    final label = switch (task.status) {
      TaskStatus.done => 'concluída',
      TaskStatus.late => 'atrasada',
      TaskStatus.pending => 'pendente',
    };

    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      decoration: BoxDecoration(
        color: scheme.surface,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: scheme.outline),
      ),
      child: Row(
        children: [
          SvgPicture.asset(
            icon,
            width: 20,
            height: 20,
            colorFilter: ColorFilter.mode(tagColor, BlendMode.srcIn),
          ),
          const SizedBox(width: 12),
          Expanded(
            child: Text(
              task.title,
              style: TextStyle(
                fontSize: 14,
                fontWeight: FontWeight.w500,
                color: scheme.onSurface,
              ),
            ),
          ),
          Text(
            task.due,
            style: TextStyle(
              fontFamily: 'JetBrainsMono',
              fontSize: 12,
              color: scheme.onSurfaceVariant,
            ),
          ),
          const SizedBox(width: 10),
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(20),
              border: Border.all(color: tagColor),
              color: tagColor.withValues(alpha: 0.08),
            ),
            child: Text(
              label,
              style: TextStyle(
                fontSize: 10,
                fontWeight: FontWeight.w700,
                color: tagColor,
              ),
            ),
          ),
        ],
      ),
    );
  }
}