import 'package:flutter/material.dart';
import 'package:flutter_svg/flutter_svg.dart';

class AppNavBar extends StatelessWidget {
  const AppNavBar({
    super.key,
    required this.index,
    required this.onDestinationSelected,
  });

  final int index;
  final ValueChanged<int> onDestinationSelected;

  @override
  Widget build(BuildContext context) {
    return NavigationBar(
      selectedIndex: index,
      onDestinationSelected: onDestinationSelected,
      destinations: const [
        NavigationDestination(
          icon: _NavAssetIcon('assets/icons/home.svg'),
          selectedIcon: _NavAssetIcon('assets/icons/home.svg'),
          label: 'Home',
        ),
        NavigationDestination(
          icon: _NavAssetIcon('assets/icons/subjects.svg'),
          selectedIcon: _NavAssetIcon('assets/icons/subjects.svg'),
          label: 'Disciplinas',
        ),
        NavigationDestination(
          icon: _NavAssetIcon('assets/icons/tasks.svg'),
          selectedIcon: _NavAssetIcon('assets/icons/tasks.svg'),
          label: 'Tarefas',
        ),
      ],
    );
  }
}

class _NavAssetIcon extends StatelessWidget {
  const _NavAssetIcon(this.asset);

  final String asset;

  @override
  Widget build(BuildContext context) {
    final color = IconTheme.of(context).color ?? Colors.black;
    return SvgPicture.asset(
      asset,
      width: 24,
      height: 24,
      colorFilter: ColorFilter.mode(color, BlendMode.srcIn),
    );
  }
}