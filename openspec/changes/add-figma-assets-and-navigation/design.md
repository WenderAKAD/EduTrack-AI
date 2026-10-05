# Design

## Context

See `proposal.md` — Why, for the motivation.

The shape of this change: the EduTrack AI frontend has a Design System record and
nothing else. `flutterflow/REGISTRO-CONFIGURACAO.md` fixes a palette and two
typefaces, and the Figma file referenced in Tarefa 06 supplies the visual
reference. Neither has been turned into files or pages.

Three constraints come from the platform, not from preference:

- FlutterFlow is browser-based. There is no build artifact to commit, so the
  repository can only hold the *inputs* to the frontend — the original asset
  files and a written record of the configuration. Versioning the app itself is
  not available.
- The Figma-to-FlutterFlow automatic import is experimental and fails often.
  The project already decided in Tarefa 07 to use Figma as a visual reference
  and assemble widgets by hand. This change keeps that decision.
- FlutterFlow serves both a phone build and a browser preview from one project,
  so a layout that only works at one width fails half the requirement.

## Goals / Non-Goals

**Goals:**

- Make the exported asset files reproducible and checkable: a reader can tell
  which file came from which Figma element and where it is used.
- Declare the navigation topology in the spec, so "three pages and a working
  NavBar" is verifiable rather than a screenshot assertion.
- Pin the design tokens the shell must use, so consistency with the Design
  System is checkable per page.

**Non-Goals:**

- No data binding. The pages render static content; the Xano API is untouched.
- No Xano endpoints. Those are a separate change, and the tables from Tarefa 08
  have no endpoints yet.
- No Figma file restructuring beyond grouping the Dashboard screen's elements.
  Redesigning the file is not this change.
- No icons for features that do not exist yet — no "edit profile", no "settings",
  no "grades". Assets are limited to what the three pages actually show.

## Decisions

**SVG for every icon, single file for both themes.**
SVG is the format the task specifies for icons and is also the right choice on
the merits: one vector file stays sharp from a 16px navigation item to a 3x
export. The requirement that one file serves both themes is the part that
constrains the export — a file exported with its fill baked in cannot be
recolored, so the export has to keep the mark as a shape rather than as a
painted path.
*Alternative considered:* PNG at 2x/3x, which the task offers as a fallback when
SVG recoloring proves troublesome. Rejected for now — it costs three files per
icon and loses sharpness, and nothing in the shell is pixel-critical. If a
specific icon turns out to be unrecolorable, that icon alone moves to PNG.

**`kebab-case` names that describe function.**
`add-task.svg`, not `red-circle.svg`. The shell will grow; an icon named after
its color breaks the first time the palette is used in a second context.
*Alternative considered:* naming after the Figma layer path. Rejected — layer
names change when the file is reorganized, and the criterion asks for names that
hold up outside Figma.

**The three pages are named after the domain, not after the layout.**
`HomePage`, `SubjectsPage`, `TasksPage`. These are the entities the app is
actually about, and the names are fixed by the task. The naming also survives
the endpoint change: `SubjectsPage` is still the right name when its list stops
being static.
*Alternative considered:* `DashboardPage`, `SubjectsListPage`, `TasksListPage`.
Rejected — "List" in the name becomes wrong the moment a detail view is added
to the same page.

**No data binding in this change, stated as a requirement.**
The obvious temptation is to wire the pages to the Xano API Group created in
Tarefa 07, since it already exists and returns 200. The spec forbids it, and the
reason is that the endpoint it would call does not exist: `GET /status` is a
connectivity probe with no subjects in it. Binding a list widget to it would
produce a page that looks wired and is not. Writing the subjects endpoints
first would turn this into two changes.
*Alternative considered:* build the subjects endpoints now and bind them. Rejected
— it merges an interface task with a backend task, and the backend change would
land unreviewed.

**The nav bar marks the active item through color, not through structure.**
Active item uses `#E10600` in the light theme and the neon `#FF1E3C` in the dark
theme; inactive items use the secondary text token. This follows the palette
already recorded in Tarefa 07 rather than inventing a fourth state color.
*Alternative considered:* a distinct icon shape per state. Rejected — it doubles
the asset count for a distinction color already carries.

**Assets are versioned on their own branch.**
The task's flow calls for `style/assets-figma`. Beyond following the task, a
branch makes binary and vector additions reviewable as one unit — a reviewer can
approve or reject the whole asset set without it interleaving with the config
record.
*Alternative considered:* commit assets on `main` directly. Rejected — it is the
project's established PR flow, from Tarefa 05.

## Risks / Trade-offs

**The Figma file may not be grouped as the task expects** → Group the Dashboard
elements first, then export. If a specific element cannot be grouped without
redesigning the file, export it anyway and record the exception in the asset
record rather than silently shipping an untraceable file.

**A page built at one width may break at the other** → Build and check both
widths before the change is archived. The requirement is explicit for this
reason.

**Static placeholder content can be mistaken for working data** → The spec
requires the pages to declare that they call no API, and the asset and config
record labels every sample value as a placeholder. This is the failure mode the
"no data binding" requirement exists to prevent.

**Neon on white loses contrast** → Enforced as a spec requirement: red text on a
light background uses `#C1121F`, and the neon stays confined to fills and the
active nav item. Carried over from the Tarefa 07 observation, restated here
because assets are where the mistake is easiest to make.