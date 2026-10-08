import 'package:flutter/material.dart';

/// Design tokens for EduTrack AI, source: `flutterflow/REGISTRO-CONFIGURACAO.md`
/// (Tarefa 07) and `flutterflow/tema-referencia.html` (Tarefa 09).
abstract final class AppColors {
  // Brand / shared
  static const Color primary = Color(0xFFE10600);

  // Light theme
  static const Color secondaryLight = Color(0xFF8B0012);
  static const Color accentLight = Color(0xFFC1121F);
  static const Color bgLight = Color(0xFFF7F4F3);
  static const Color surfaceLight = Color(0xFFFFFFFF);
  static const Color borderLight = Color(0xFFEADFDC);
  static const Color textLight = Color(0xFF1A1312);
  static const Color mutedLight = Color(0xFF7B6A67);

  // Dark theme
  static const Color bgDark = Color(0xFF0A0A0A);
  static const Color surfaceDark = Color(0xFF16181C);
  static const Color borderDark = Color(0xFF2A2D33);
  static const Color textDark = Color(0xFFF2F3F5);
  static const Color mutedDark = Color(0xFF9AA0A6);
  static const Color accentDark = Color(0xFFFF1E3C);
  static const Color hoverDark = Color(0xFFFF4D5E);
  static const Color secondaryDark = Color(0xFF101215);

  // Semantic (both themes)
  static const Color success = Color(0xFF1C7A4A);
}

abstract final class AppTheme {
  static ThemeData light() => _build(
        brightness: Brightness.light,
        background: AppColors.bgLight,
        surface: AppColors.surfaceLight,
        border: AppColors.borderLight,
        text: AppColors.textLight,
        muted: AppColors.mutedLight,
        active: AppColors.primary,
        secondary: AppColors.secondaryLight,
        accent: AppColors.accentLight,
      );

  static ThemeData dark() => _build(
        brightness: Brightness.dark,
        background: AppColors.bgDark,
        surface: AppColors.surfaceDark,
        border: AppColors.borderDark,
        text: AppColors.textDark,
        muted: AppColors.mutedDark,
        active: AppColors.accentDark,
        secondary: AppColors.secondaryDark,
        accent: AppColors.accentDark,
      );

  static ThemeData _build({
    required Brightness brightness,
    required Color background,
    required Color surface,
    required Color border,
    required Color text,
    required Color muted,
    required Color active,
    required Color secondary,
    required Color accent,
  }) {
    final scheme = ColorScheme(
      brightness: brightness,
      primary: AppColors.primary,
      onPrimary: Colors.white,
      secondary: secondary,
      onSecondary: Colors.white,
      error: accent,
      onError: Colors.white,
      surface: surface,
      onSurface: text,
      outline: border,
      outlineVariant: border,
      surfaceContainerHighest: surface,
      onSurfaceVariant: muted,
    );

    final base = ThemeData(
      useMaterial3: true,
      brightness: brightness,
      colorScheme: scheme,
      scaffoldBackgroundColor: background,
      fontFamily: 'Inter',
      splashFactory: InkSparkle.splashFactory,
    );

    return base.copyWith(
      textTheme: base.textTheme.copyWith(
        displaySmall: const TextStyle(
          fontFamily: 'Inter',
          fontSize: 28,
          fontWeight: FontWeight.w700,
          letterSpacing: -0.6,
        ),
        titleLarge: const TextStyle(
          fontFamily: 'Inter',
          fontSize: 20,
          fontWeight: FontWeight.w700,
          letterSpacing: -0.3,
        ),
        titleMedium: const TextStyle(
          fontFamily: 'Inter',
          fontSize: 16,
          fontWeight: FontWeight.w700,
        ),
        bodyMedium: const TextStyle(
          fontFamily: 'Inter',
          fontSize: 14,
          fontWeight: FontWeight.w400,
        ),
        labelLarge: const TextStyle(
          fontFamily: 'Inter',
          fontSize: 14,
          fontWeight: FontWeight.w600,
        ),
        labelSmall: const TextStyle(
          fontFamily: 'Inter',
          fontSize: 12,
          fontWeight: FontWeight.w600,
        ),
      ),
      appBarTheme: AppBarTheme(
        backgroundColor: surface,
        surfaceTintColor: surface,
        foregroundColor: text,
        elevation: 0,
        centerTitle: false,
      ),
      cardTheme: CardThemeData(
        color: surface,
        surfaceTintColor: surface,
        elevation: 0,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(14),
          side: BorderSide(color: border),
        ),
      ),
      navigationBarTheme: NavigationBarThemeData(
        backgroundColor: surface,
        surfaceTintColor: surface,
        elevation: 0,
        indicatorColor: AppColors.primary.withValues(alpha: 0.12),
        height: 68,
        labelBehavior: NavigationDestinationLabelBehavior.alwaysShow,
        iconTheme: WidgetStateProperty.resolveWith((states) {
          final selected = states.contains(WidgetState.selected);
          return IconThemeData(color: selected ? active : muted);
        }),
        labelTextStyle: WidgetStateProperty.resolveWith((states) {
          final selected = states.contains(WidgetState.selected);
          return TextStyle(
            fontFamily: 'Inter',
            fontSize: 12,
            fontWeight: selected ? FontWeight.w600 : FontWeight.w400,
            color: selected ? active : muted,
          );
        }),
      ),
      inputDecorationTheme: InputDecorationTheme(
        border: OutlineInputBorder(borderRadius: BorderRadius.circular(10)),
      ),
    );
  }
}