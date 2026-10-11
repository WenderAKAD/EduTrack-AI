import 'package:flutter/material.dart';

import 'pages/main_shell.dart';
import 'theme/app_theme.dart';

class EdutrackApp extends StatelessWidget {
  const EdutrackApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'EduTrack AI',
      debugShowCheckedModeBanner: false,
      theme: AppTheme.light(),
      darkTheme: AppTheme.dark(),
      themeMode: ThemeMode.light,
      home: const MainShell(),
    );
  }
}