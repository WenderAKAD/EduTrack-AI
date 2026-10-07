# Proposal

## Why

The EduTrack AI frontend exists only as a Design System record — the palette and
typography were defined in Tarefa 07, and no page has been built and no asset has
been provided. The Design System is materialized in the reference mockup
`flutterflow/tema-referencia.html`; without pages there is nothing to navigate and
nothing to align against that reference, so the frontend cannot be reviewed or
handed to the next task.

Tarefa 09 is the first task to build the interface shell. Its scope is the
"casca" only: the pages, the navigation between them, and the original asset
files that the Design System produces. No data binding is involved — that is the
following tasks.

## What Changes

- Declare a `design-assets` capability: icons and images sourced from the
  project's Design System (Tarefa 07), materialized in the reference mockup
  `flutterflow/tema-referencia.html`, versioned in the repository under
  `assets/icons/` and `assets/images/`, in the formats and naming convention this
  change fixes.
- Declare an `app-navigation` capability: the three pages the app is planned
  around — `HomePage`, `SubjectsPage` and `TasksPage` — and the bottom
  navigation bar that moves between them.
- Fix the design tokens the shell is built from (colors, typography) as
  spec-level requirements, so "consistent with the Design System" stops being a
  matter of opinion and becomes checkable per page.
- Version the original asset files in Git alongside the configuration record
  that maps each one to where FlutterFlow consumes it.
- Record the FlutterFlow configuration in `flutterflow/`, following the pattern
  established by `REGISTRO-CONFIGURACAO.md` in Tarefa 07.

## Capabilities

### New Capabilities

- `design-assets`: The icon and image files sourced from the EduTrack AI Design
  System, the naming and format rules they follow, their location in the
  repository, and the design tokens every asset and every screen must match.
- `app-navigation`: The three pages of the EduTrack AI shell and the bottom
  navigation bar that switches between them, including the action each item
  performs and the responsive behavior across phone and browser widths.

### Modified Capabilities

None. `subjects` and `user` describe database tables; this change adds no
column, no endpoint and no query. The `SubjectsPage` and `TasksPage` declared
here are presentation shells — the lists they will eventually render are the
subject of a later change, when the Tarefa 10 endpoints exist.

## Impact

- **New directories:** `assets/icons/`, `assets/images/`, each with a `.gitkeep`
  so the structure exists in Git before it holds files.
- **New files:** the exported assets themselves; a record of what each asset is
  and where FlutterFlow consumes it; an updated `flutterflow/` record for the
  page and navigation structure.
- **External systems:** the EduTrack AI project in FlutterFlow, where the three
  pages and the navigation bar are built. The design source is the reference
  mockup `flutterflow/tema-referencia.html`; no Figma file is involved.
- **No backend change.** Nothing is added to the Xano workspace; the tables from
  Tarefa 08 are untouched.
- **No data binding.** The pages render static content in this change, so no
  API call from FlutterFlow depends on it.