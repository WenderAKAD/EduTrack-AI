# Design

## Context

See `proposal.md` — Why, for the motivation.

The shape of this change: the EduTrack AI frontend has a Design System record and
nothing else. `flutterflow/REGISTRO-CONFIGURACAO.md` fixes a palette and two
typefaces, and the reference mockup `flutterflow/tema-referencia.html`
materializes the visual reference. Neither has been turned into pages.

Five constraints come from the platform, not from preference:

- **The development machine cannot run either web IDE.** The MacBook Pro 2016
  (`MacBook8,1`, Intel Core `m-5Y31` at 0.90 GHz, Intel HD Graphics 5300) blocks
  both tools: Chrome 154 reports `WebGL: Disabled` because the 2015 GPU is
  blocklisted, and Figma refuses Safari 16.6 because it requires 17.4+, which
  macOS 13.7.8 cannot provide. Both steps therefore run on a Windows 11 machine
  over remote access. This is an environment limitation, not a design choice —
  recorded so that the constraint is not rediscovered later.
- FlutterFlow is browser-based. There is no build artifact to commit, so the
  repository can only hold the *inputs* to the frontend — the original asset
  files and a written record of the configuration. Versioning the app itself is
  not available.
- The Figma-to-FlutterFlow automatic import is experimental and fails often.
  The project decided in Tarefa 07 to use a visual reference and assemble
  widgets by hand. This change keeps that decision.
- **Figma is not the design source.** The EduTrack AI Figma file named by Tarefa 06 was never
  created, and no machine available to this project runs the tool, so the change
  sources the assets from the Design System of Tarefa 07 and the reference
  mockup `flutterflow/tema-referencia.html` instead.
- FlutterFlow serves both a phone build and a browser preview from one project,
  so a layout that only works at one width fails half the requirement.

## Goals / Non-Goals

**Goals:**

- Make the asset files reproducible and checkable: a reader can tell which
  file came from which element of the design sources and where it is used.
- Declare the navigation topology in the spec, so "three pages and a working
  NavBar" is verifiable rather than a screenshot assertion.
- Pin the design tokens the shell must use, so consistency with the Design
  System is checkable per page.

**Non-Goals:**

- No data binding. The pages render static content; the Xano API is untouched.
- No Xano endpoints. Those are a separate change, and the tables from Tarefa 08
  have no endpoints yet.
- No design-tool restructuring beyond grouping the Dashboard section's elements.
  Redesigning the interface is not this change.
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

**The design sources are HTML/CSS and raw SVG, not a vector canvas** → The
mockup carries the grouping and the tokens; the icons are edited directly in SVG
and reviewed against the mockup rather than in a design tool. A future design
tool adoption is out of scope — this change fixes the mockup as the source.
Nothing about the pages, the navigation or the FlutterFlow build changes as a
result.

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

**The work happens off the development machine** → The pages are built on a
Windows 11 machine reached over remote access; only the files come back to this
repository. The risk is divergence between what was built and what is recorded
here, so the screenshots of the three pages are required evidence rather than
decoration, and the asset record names the file each screenshot shows.

**No Figma file exists for this project, and no machine runs it** → Tarefa 06
recorded four Community templates as visual references in
`docs/pesquisa/referencias.md`; it duplicated no file and left no project link. A
file named "EduTrack Orbit AI — Design System" (`file_key`
`i6BKRzp9HGlhyubcz6xhJ1`) does exist, but it belongs to a different, abandoned
project — a Streamlit/Python application with its own git history at
`Documents/2 Semestre/Innovation Lab/EduTrack Orbit IA/`. It must not be used: it
is a different stack, a different codebase and a different design, and importing
from it would mix two projects in one deliverable. The change therefore adopts
`flutterflow/tema-referencia.html`, already built from the Design System recorded
in `flutterflow/REGISTRO-CONFIGURACAO.md`, as the editable design source in place
of Figma. Trade-off: HTML/CSS is not a vector editor, so icon work is done in
raw SVG and verified against the mockup — which is exactly what the export step
used to guarantee.