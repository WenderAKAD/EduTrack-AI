# Evidências da Tarefa 09 — app Flutter local (substituto do FlutterFlow)

Capturas do app **EduTrack AI** rodando com Flutter 3.29.3 (build web) a partir
do código em `lib/`, nas duas larguras de conferência da spec `app-navigation`:
**celular** (390×844) e **navegador** (1280×800).

> **Substituição registrada.** O FlutterFlow não carrega na máquina de
> desenvolvimento (Intel Core `m-5Y31`, 0,90 GHz) — ver
> `docs/guia-execucao-windows.md` e a seção 5 de
> `openspec/changes/add-figma-assets-and-navigation/tasks.md`. Para não bloquear
> a entrega, as três páginas e a NavBar foram construídas **em Flutter local**
> com o mesmo Design System, mesma nomenclatura de páginas (`HomePage`,
> `SubjectsPage`, `TasksPage`) e os mesmos nove ícones de `assets/icons/`.

| Arquivo | Largura | Página | Conteúdo conferido |
|---|---|---|---|
| `flutterflow-home-phone.png` | 390×844 | `HomePage` | Título EduTrack AI, KPIs (72% / 12 / 6), painéis de progresso e tarefas recentes, NavBar ativa em Home |
| `flutterflow-home-browser.png` | 1280×800 | `HomePage` | Mesmo conteúdo em largura de navegador, sem scroll horizontal |
| `flutterflow-subjects-phone.png` | 390×844 | `SubjectsPage` | Título Disciplinas, cards arredondados com nome/professor/carga, NavBar ativa em Disciplinas |
| `flutterflow-subjects-browser.png` | 1280×800 | `SubjectsPage` | Mesmo conteúdo em largura de navegador |
| `flutterflow-tasks-phone.png` | 390×844 | `TasksPage` | Título Tarefas, ListView de tarefas com data e estado (concluída/pendente/atrasada), NavBar ativa em Tarefas |
| `flutterflow-tasks-browser.png` | 1280×800 | `TasksPage` | Mesmo conteúdo em largura de navegador |

Captura de navegador gerada com Chrome headless usando SwiftShader
(renderização por software, `--enable-unsafe-swiftshader`), porque a GPU de 2015
está em blocklist do Chrome (`WebGL: Disabled`).

**Pasta `assets/` no VS Code:** evidência manual a capturar pelo aluno na
máquina de desenvolvimento; a estrutura versionada é
[`assets/`](../../assets/) (`icons/` + `images/` + `README.md`).

## Como reproduzir

```bash
flutter build web
cd build/web && python3 -m http.server 8080
./tools/capture-screenshots.sh   # Chrome headless + SwiftShader
```