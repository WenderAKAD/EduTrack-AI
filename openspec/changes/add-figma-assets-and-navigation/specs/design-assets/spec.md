# design-assets Specification

## Purpose

Define the icon and image files the EduTrack AI frontend is built from — where
they come from, how they are named and formatted, where they are versioned, and
the design tokens every one of them must match.

## ADDED Requirements

### Requirement: Assets originate from the EduTrack AI Figma file
The system SHALL source every icon and image asset from the project's Figma file
by exporting the element, rather than by authoring the file outside Figma. The
export SHALL be of the Dashboard screen's elements, grouped logically by
function — one group for the subject card, one for the task card, one for the
navigation bar. No asset may be drawn or traced outside Figma.

#### Scenario: Icon is exported from Figma
- **WHEN** an icon asset is added to the project
- **THEN** it was exported from a selected element of the EduTrack AI Figma file, and not recreated from scratch elsewhere

#### Scenario: Elements are grouped by function
- **WHEN** the Dashboard screen is inspected in Figma
- **THEN** its elements are organized into groups by function, such as a subject card group, a task card group and a navigation bar group

#### Scenario: Ungrouped element is refused
- **WHEN** an asset is exported from an element that still sits loose on the canvas, outside any functional group
- **THEN** the element is grouped in Figma before the export is accepted

### Requirement: Icons use the SVG format
The system SHALL export every icon, glyph or logo mark as **SVG**, and SHALL NOT
commit raster icons in their place. Icons SHALL be exported in a single color
that FlutterFlow can recolor, so that one file serves both the light and the
dark theme of the Design System.

#### Scenario: Icon is exported as SVG
- **WHEN** an icon is exported from Figma for the repository
- **THEN** the exported file is an `.svg`

#### Scenario: Raster icon is refused
- **WHEN** an icon arrives as `.png`, `.jpg` or `.webp` in `assets/icons/`
- **THEN** it is rejected and re-exported from Figma as SVG

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
The system SHALL commit every exported asset to the repository, so that the
original files survive independently of the FlutterFlow cloud copy. The assets
SHALL be delivered on a dedicated branch, so that the addition of binary and
vector files is reviewable on its own.

#### Scenario: Asset is committed
- **WHEN** an asset is exported from Figma
- **THEN** it is added to the repository and pushed to a branch of its own

#### Scenario: Asset survives deletion from FlutterFlow
- **WHEN** an asset is removed from the FlutterFlow Media Assets library
- **THEN** the original file is still recoverable from the repository, and can be re-uploaded without re-exporting it from Figma

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