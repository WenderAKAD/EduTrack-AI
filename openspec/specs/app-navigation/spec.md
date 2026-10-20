# app-navigation Specification

## Purpose
Define the three pages that make up the EduTrack AI interface shell and the
bottom navigation bar that moves between them, so that navigation is a declared
part of the frontend rather than an arrangement discovered by clicking.

## Requirements

### Requirement: Three named pages
The system SHALL create exactly three pages in the EduTrack AI frontend project,
named `HomePage`, `SubjectsPage` and `TasksPage`. They are built locally with
Flutter (3.29.3) as a substitute for the FlutterFlow IDE, which does not load on
the development hardware (Intel Core `m-5Y31`; the webGL-accelerated editor does
not render). Each page SHALL carry its own visible title, so a user can tell
which page they are on from the screenshot alone.

#### Scenario: HomePage exists
- **WHEN** the EduTrack AI project pages are listed
- **THEN** `HomePage` is present, and is the dashboard overview of the student

#### Scenario: SubjectsPage exists
- **WHEN** the EduTrack AI project pages are listed
- **THEN** `SubjectsPage` is present, and is the list of the student's subjects

#### Scenario: TasksPage exists
- **WHEN** the EduTrack AI project pages are listed
- **THEN** `TasksPage` is present, and is the list of the student's tasks

#### Scenario: Every page is identifiable from its content
- **WHEN** a screenshot of any single page is viewed in isolation
- **THEN** the page title makes it clear whether it is the dashboard, the subject list or the task list

### Requirement: Bottom navigation bar connects the three pages
The system SHALL provide a bottom navigation bar with one item per page. Every
item SHALL have an action assigned that navigates to its own page, so no item
is inert. Tapping an item SHALL mark that item as the active one.

#### Scenario: Every item is wired
- **WHEN** each navigation bar item is inspected
- **THEN** it has a navigation action pointing at its own page

#### Scenario: Item navigates to its page
- **WHEN** a user taps the navigation item for `SubjectsPage`
- **THEN** `SubjectsPage` becomes the visible page

#### Scenario: Active item is marked
- **WHEN** the current page is `TasksPage`
- **THEN** the navigation bar marks the `TasksPage` item as active, distinguishably from the other two

#### Scenario: Inert item is a defect
- **WHEN** a navigation item has no action assigned
- **THEN** the navigation is not considered complete, and tapping it must do nothing only if the whole page is still under construction

### Requirement: Pages render content, not empty containers
Every page SHALL contain visible content. A `ListView` SHALL have children, and
a `Container` standing in for a mockup card SHALL contain at least one `Text`
widget. An empty container SHALL NOT count as a built page.

#### Scenario: Subject card has content
- **WHEN** the subject card on `SubjectsPage` is inspected
- **THEN** it is a rounded `Container` holding text, not an empty box

#### Scenario: Task list is not empty
- **WHEN** the task list on `TasksPage` is inspected
- **THEN** its `ListView` has at least one item

#### Scenario: Empty list renders a placeholder
- **WHEN** a list has no data to show
- **THEN** it renders an explicit empty-state, rather than rendering nothing at all

### Requirement: The shell adapts to phone and browser widths
The shell SHALL be usable at both a phone width and a browser width, because
FlutterFlow is expected to run in both. The navigation bar SHALL remain
reachable at both, and lists SHALL not force a horizontal scrollbar at phone
width.

#### Scenario: Navigation is reachable on a phone
- **WHEN** the app is viewed at a phone width
- **THEN** the bottom navigation bar is visible and not clipped

#### Scenario: Content is readable in a browser
- **WHEN** the app is viewed at a desktop browser width
- **THEN** the content is laid out without horizontal scrolling, and the navigation bar remains visible

### Requirement: No data is bound to the shell in this change
The pages SHALL render static content in this change. They SHALL NOT call the
Xano API, and SHALL NOT consume an API Group action. This change delivers the
interface only; binding it to data requires the endpoints that do not exist yet.

#### Scenario: No API call is configured
- **WHEN** the three pages are inspected for API calls
- **THEN** none of them calls the Xano Backend API Group

#### Scenario: Static content is intentional
- **WHEN** a page shows sample text or sample rows
- **THEN** the values are static placeholders, and not the result of a request

#### Scenario: Wiring is deferred, not forgotten
- **WHEN** a page is later bound to real data
- **THEN** the change that does the binding also covers the endpoints it depends on
