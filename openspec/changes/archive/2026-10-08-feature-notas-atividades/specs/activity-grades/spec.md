# Activity Grades Specification

## Purpose

Define como a nota de um aluno em uma atividade específica é registrada — o
primeiro caminho de escrita do boletim do EduTrack AI.

## ADDED Requirements

### Requirement: Activity grade table structure

The system SHALL store grades in an `activity_grades` table with at least `id`,
`activity_id`, `student_id`, `grade` and `user_id`.

#### Scenario: Table exists after push

- **WHEN** `tables/activity_grades.xs` is pushed to the Xano workspace
- **THEN** an `activity_grades` table exists with the declared fields

#### Scenario: Primary key is auto-generated

- **WHEN** a new grade is inserted
- **THEN** `id` is assigned automatically by the database

### Requirement: Grade is owned by the logged-in user

Every row SHALL carry a `user_id` referencing the authenticated user, and every
query SHALL filter by it.

#### Scenario: Grade is written with the logged-in user

- **WHEN** the professor records a grade
- **THEN** the row stores the `user_id` of the authenticated user

#### Scenario: Grade without an owner is rejected

- **WHEN** a write would leave `user_id` empty
- **THEN** the system rejects it

### Requirement: Record a grade endpoint

The system SHALL expose `POST /activity_grades`, which records a grade for a
student on a specific activity.

#### Scenario: Professor records a grade

- **WHEN** the professor sends a grade for a student and an activity
- **THEN** the system stores it and returns the created record

#### Scenario: Missing grade is rejected

- **WHEN** the request has no grade value
- **THEN** the system rejects it with a validation error