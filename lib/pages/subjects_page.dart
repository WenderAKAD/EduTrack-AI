import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

import '../models/seed_data.dart';
import '../theme/app_theme.dart';
import '../widgets/app_page_header.dart';
import '../widgets/subject_card.dart';

class SubjectsPage extends StatelessWidget {
  const SubjectsPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        AppPageHeader(
          title: 'Disciplinas',
          subtitle: 'semestre 2026.2',
          trailing: IconButton(
            tooltip: 'Adicionar disciplina',
            onPressed: () {},
            icon: SvgPicture.asset(
              'assets/icons/add-subject.svg',
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
          child: ListView.builder(
            padding: const EdgeInsets.all(20),
            itemCount: SeedData.subjects.length,
            itemBuilder: (context, index) {
              return Padding(
                padding: const EdgeInsets.only(bottom: 12),
                child: Center(
                  child: ConstrainedBox(
                    constraints: const BoxConstraints(maxWidth: 760),
                    child: SubjectCard(subject: SeedData.subjects[index]),
                  ),
                ),
              );
            },
          ),
        ),
      ],
    );
  }
}