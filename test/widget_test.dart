import 'package:flutter_test/flutter_test.dart';

import 'package:edutrack_ai/app.dart';

void main() {
  testWidgets('EduTrack AI shell renders the three pages', (tester) async {
    await tester.pumpWidget(const EdutrackApp());
    expect(find.text('EduTrack AI'), findsOneWidget);
    await tester.tap(find.text('Disciplinas'));
    await tester.pumpAndSettle();
    expect(find.text('Programação Avançada'), findsWidgets);
    await tester.tap(find.text('Tarefas'));
    await tester.pumpAndSettle();
    expect(find.text('Relatório do módulo 2'), findsOneWidget);
  });
}