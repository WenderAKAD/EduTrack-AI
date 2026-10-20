import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';

import '../widgets/app_nav_bar.dart';
import 'home_page.dart';
import 'subjects_page.dart';
import 'tasks_page.dart';

class MainShell extends StatefulWidget {
  const MainShell({super.key});

  @override
  State<MainShell> createState() => _MainShellState();
}

class _MainShellState extends State<MainShell> {
  late int _index = _initialIndex();

  static const List<Widget> _pages = [
    HomePage(),
    SubjectsPage(),
    TasksPage(),
  ];

  int _initialIndex() {
    if (!kIsWeb) return 0;
    final page = Uri.base.queryParameters['page'];
    return switch (page) {
      'subjects' => 1,
      'tasks' => 2,
      _ => 0,
    };
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: IndexedStack(index: _index, children: _pages),
      bottomNavigationBar: AppNavBar(
        index: _index,
        onDestinationSelected: (value) => setState(() => _index = value),
      ),
    );
  }
}