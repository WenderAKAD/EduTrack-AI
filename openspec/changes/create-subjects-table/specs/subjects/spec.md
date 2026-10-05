# Spec Delta

## Purpose

Defines the `subjects` table — the first domain entity of EduTrack AI — and the
rule that every subject belongs to exactly one authenticated user.

## ADDED Requirements

### Requirement: Subjects table structure

The system SHALL store academic subjects in a `subjects` table with the
following fields:

| Field | Type | Rules |
|---|---|---|
| `id` | int | auto-generated, primary key |
| `name` | text | required |
| `teacher` | text | required |
| `hours` | int | required, positive integer |
| `user_id` | int | required, foreign key to the authentication table, indexed |

#### Scenario: Table exists in the Xano workspace

- **WHEN** the `tables/subjects.xs` definition is pushed to the Xano workspace
- **THEN** a `subjects` table exists with the five fields listed above

#### Scenario: Primary key is auto-generated

- **WHEN** a new subject record is inserted
- **THEN** `id` is assigned automatically by the database

#### Scenario: Table name uses snake_case

- **WHEN** the table is created
- **THEN** it is named `subjects`, following the project's `snake_case` naming
  convention

### Requirement: Subject ownership

Every subject SHALL belong to exactly one authenticated user through the
`user_id` field, and `user_id` SHALL be required.

#### Scenario: Authenticated user creates a subject

- **WHEN** an authenticated user creates a subject
- **THEN** the system stores the record with `user_id` set to the authenticated
  user's id

#### Scenario: Subject without an owner is rejected

- **WHEN** a subject is inserted without `user_id`
- **THEN** the insertion fails

### Requirement: Field validation

The system SHALL enforce the following validation rules on subject fields.

#### Scenario: Required fields are present

- **WHEN** a subject is inserted
- **THEN** `name`, `teacher`, `hours` and `user_id` are all required

#### Scenario: Weekly hours must be a positive integer

- **WHEN** a subject is inserted with `hours` less than or equal to zero
- **THEN** the insertion fails

#### Scenario: Subject name is trimmed

- **WHEN** a subject is inserted with leading or trailing whitespace in `name`
- **THEN** the stored `name` has that whitespace removed

### Requirement: Data isolation between users

Every query against the `subjects` table SHALL filter by the authenticated
user's `user_id`.

#### Scenario: User lists only their own subjects

- **WHEN** a user requests their subjects
- **THEN** only records where `user_id` equals the authenticated user's id are
  returned

#### Scenario: User cannot read another user's subject

- **WHEN** a user requests a subject owned by a different user
- **THEN** no record is returned