# design-assets Specification

## Purpose
Define the icon and image files the EduTrack AI frontend is built from — where
they come from, how they are named and formatted, where they are versioned, and
the design tokens every one of them must match.

## Requirements

### Requirement: Assets originate from the EduTrack AI Design System
The system SHALL source every icon and image asset from the Design System of
Tarefa 07, recorded in `flutterflow/REGISTRO-CONFIGURACAO.md` and materialized in
the editable reference mockup `flutterflow/tema-referencia.html`. There is no
source to export from in a design tool: the EduTrack AI Figma file named by
Tarefa 06 was never duplicated, and no machine available to this project runs
Figma (`WebGL: Disabled`; Safari 16.6 vs. required 17.4+). The mockup is
therefore the design source, and its Dashboard section SHALL group elements
logically by function — one group for the subject card, one for the task card,
one for the navigation bar. No asset may be authored without a counterpart in
the mockup.

#### Scenario: Icon is sourced from the reference mockup
- **WHEN** an icon asset is added to the project
- **THEN** it has a counterpart in `flutterflow/tema-referencia.html` and derives from the Design System of Tarefa 07, not from an element exported out of Figma

#### Scenario: Elements are grouped by function
- **WHEN** the Dashboard section of the reference mockup is inspected
- **THEN** its elements are organized into groups by function, such as a subject card group, a task card group and a navigation bar group

#### Scenario: Ungrouped element is refused
- **WHEN** an asset corresponds to an element that still sits loose in the mockup, outside any functional group
- **THEN** the element is grouped in the mockup before the asset is accepted

### Requirement: Icons use the SVG format
The system SHALL provide every icon, glyph or logo mark as **SVG**, and SHALL NOT
commit raster icons in their place. Icons SHALL be delivered in a single color
that the host frontend can recolor, so that one file serves both the light and
the dark theme of the Design System.

#### Scenario: Icon is provided as SVG
- **WHEN** an icon is added to the repository
- **THEN** the file is an `.svg`

#### Scenario: Raster icon is refused
- **WHEN** an icon arrives as `.png`, `.jpg` or `.webp` in `assets/icons/`
- **THEN** it is rejected and replaced by an SVG from the design sources

#### Scenario: One icon serves both themes
- **WHEN** the same icon is used on a light background and on a dark background
- **THEN** a single committed SVG file serves both, recolored by the tool that renders it, with no second variant of the file required

### Requirement: Asset naming is kebab-case and descriptive
The system SHALL name every asset file in `kebab-case`, without spaces or accents,
using a name that describes the element's function rather than its appearance.
Files SHALL be sorted into `assets/icons/` for vector marks and `assets/images/`
for raster content.

#### Scenario: Icon lands in the icons directory
- **WHEN** an SVG asset is committed
- **THEN** it is located at `assets/icons/<kebab-case-name>.svg`

#### Scenario: Raster image lands in the images directory
- **WHEN** a raster asset is committed
- **THEN** it is located at `assets/images/<kebab-case-name>.<ext>`

#### Scenario: Name describes function
- **WHEN** an asset file name is read
- **THEN** it names what the element represents, such as `add-task.svg` or `empty-subjects.svg`, and not how it looks, such as `red-circle.svg`

#### Scenario: Empty directories are tracked
- **WHEN** a directory under `assets/` holds no file yet
- **THEN** it carries a `.gitkeep` file, so the structure exists in Git before it holds assets

### Requirement: Assets are versioned in Git
The system SHALL commit every asset to the repository, so that the original
files survive independently of the FlutterFlow cloud copy. The assets SHALL be
delivered on a dedicated branch, so that the addition of binary and vector files
is reviewable on its own.

#### Scenario: Asset is committed
- **WHEN** an asset is added to the design sources
- **THEN** it is added to the repository and pushed to a branch of its own

#### Scenario: Asset survives deletion from the frontend
- **WHEN** an asset is removed from the Media Assets library of the host frontend
- **THEN** the original file is still recoverable from the repository, and can be re-uploaded without rebuilding it from scratch

### Requirement: Assets match the design tokens
Every asset SHALL be built against the Design System recorded in
`flutterflow/REGISTRO-CONFIGURACAO.md`. Icons SHALL carry no hardcoded fill that
prevents recoloring, and the interface that hosts them SHALL use the recorded
palette: `#E10600` primary, `#C1121F` for red text on light backgrounds,
`#F7F4F3` background and `#1A1312` primary text. Typography SHALL be **Inter**
for titles and body, **JetBrains Mono** for identifiers and dates.

#### Scenario: Icon is recolorable
- **WHEN** an SVG asset is inspected
- **THEN** it does not hardcode a fill that prevents the host interface from applying its own color

#### Scenario: Screen uses only recorded colors
- **WHEN** a page of the shell is inspected
- **THEN** every color it uses comes from the palette recorded in `flutterflow/REGISTRO-CONFIGURACAO.md`, by hex value

#### Scenario: Red text on light background stays accessible
- **WHEN** red text is rendered over a light background
- **THEN** it uses `#C1121F`, because the neon `#FF1E3C` does not hold contrast on white

#### Scenario: Neon accent stays a minority
- **WHEN** the dark theme is applied
- **THEN** the neon `#FF1E3C` occupies no more than 5–10% of the screen, as accents and the active navigation item
