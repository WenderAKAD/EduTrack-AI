# user Specification

## Purpose
Defines the `user` authentication table — the foundation every other EduTrack AI
table depends on for ownership — and the constraints that make an account
usable: a unique email, a hashed password and an active flag.

## Requirements

### Requirement: User table structure

The system SHALL store accounts in a `user` table with `auth = true`, so the
workspace treats it as the authentication table.

| Field | Type | Rules |
|---|---|---|
| `id` | int | auto-generated, primary key |
| `name` | text | required |
| `email` | email | required, trimmed, lowercased, unique |
| `password` | password | required, sensitive |
| `is_active` | bool | optional, defaults to `true` |
| `created_at` | timestamp | optional, defaults to `now` |
| `updated_at` | timestamp | optional |
| `user_id` | int | optional, self-reference; created manually in the Xano dashboard and not used by the application |

#### Scenario: Table exists in the Xano workspace

- **WHEN** the `tables/user.xs` definition is pushed to the Xano workspace
- **THEN** a `user` table exists with the eight fields listed above

#### Scenario: Primary key is auto-generated

- **WHEN** a new user record is inserted
- **THEN** `id` is assigned automatically by the database

#### Scenario: Authentication is enabled on the table

- **WHEN** the table is inspected in the Xano dashboard
- **THEN** it is marked as the authentication table for the workspace

### Requirement: Unused self-reference field

The `user` table SHALL retain a `user_id` self-reference field created manually
in the Xano dashboard. The application SHALL NOT read or write this field. It is
declared in `tables/user.xs` so that the CLI never proposes removing it from the
server.

#### Scenario: Field is never dropped by a sync

- **WHEN** a dry-run push is executed for `tables/user.xs`
- **THEN** the output contains no `DROP_FIELD` operation for `user_id`

#### Scenario: Field is not part of the application contract

- **WHEN** an authentication endpoint is written for this table
- **THEN** it does not read or set `user_id`, because the app is single-account
  with no teams or multi-tenancy

### Requirement: Credential storage

The system SHALL store `email` as a required, unique field, and `password` as a
required and sensitive field. Neither value may ever appear in readable query
output.

#### Scenario: Email is normalised

- **WHEN** an account is registered with a mixed-case email
- **THEN** the stored email is trimmed and lowercased

#### Scenario: Duplicate email is rejected

- **WHEN** an account is registered with an email that already exists
- **THEN** the registration fails

#### Scenario: Password is not readable

- **WHEN** any query returns a user record
- **THEN** the `password` field is excluded from the result

#### Scenario: Password is stored hashed

- **WHEN** an account is registered
- **THEN** the stored `password` is not the plain-text value submitted by the
  user

### Requirement: Account state

Every account SHALL have an `is_active` flag defaulting to `true`, and SHALL
record `created_at` at registration time.

#### Scenario: New account is active by default

- **WHEN** an account is registered without specifying `is_active`
- **THEN** the stored value is `true`

#### Scenario: Registration timestamp is recorded

- **WHEN** an account is registered
- **THEN** `created_at` is set to the moment of registration

#### Scenario: Inactive account is retained

- **WHEN** `is_active` is set to `false`
- **THEN** the record is kept and is excluded from authenticated access

### Requirement: Table naming convention

The table SHALL be named `user`, following the project's `snake_case` naming
convention, and SHALL live at `tables/user.xs` in this repository.

#### Scenario: Table path follows the CLI mapping

- **WHEN** the table definition is read from this repository
- **THEN** it is located at `tables/user.xs`, the path the Xano CLI maps to
  tables
