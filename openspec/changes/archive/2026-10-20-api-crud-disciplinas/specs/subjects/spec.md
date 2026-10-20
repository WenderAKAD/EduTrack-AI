# subjects Specification

## Purpose

Expose the student's subjects through an authenticated REST layer, so the
frontend can create new subjects, list the several subjects taken at the same
time, and edit or remove them — always scoped to the owning user.

## ADDED Requirements

### Requirement: List the authenticated user's subjects
The system SHALL expose an endpoint `GET /subjects` that requires
authentication and returns only the subjects whose `user_id` equals the
authenticated user's id.

#### Scenario: Authenticated user lists their subjects
- **WHEN** an authenticated user sends `GET /subjects` with a valid JWT token
- **THEN** the system returns the list of subjects owned by that user
- **AND** subjects belonging to other users are not returned

#### Scenario: Request without a token
- **WHEN** a request is sent to `GET /subjects` without a valid JWT token
- **THEN** the system rejects the request with an authentication error
- **AND** the database is not queried

### Requirement: Create a subject owned by the authenticated user
The system SHALL expose an endpoint `POST /subjects` that requires
authentication, accepts `name`, `teacher` and `hours`, and stores the new
subject with `user_id` taken from the JWT token — never from the request body.

#### Scenario: Authenticated user creates a subject
- **WHEN** an authenticated user sends `POST /subjects` with `name`, `teacher`
  and `hours`
- **THEN** the system creates the subject with `user_id` equal to the
  authenticated user's id
- **AND** returns the created record

#### Scenario: Owner field is not attacker-controlled
- **WHEN** an authenticated user sends `POST /subjects` with a `user_id` in
  the request body
- **THEN** the system ignores the body value
- **AND** stores the subject with the id from the JWT token

### Requirement: Update a subject owned by the authenticated user
The system SHALL expose an endpoint `PATCH /subjects/{subject_id}` that requires
authentication, loads the subject by id, refuses the request when the subject
belongs to another user, and merges only the fields present in the request
body.

#### Scenario: Owner updates their subject
- **WHEN** an authenticated user sends `PATCH /subjects/{subject_id}` for a
  subject they own
- **THEN** the system applies the sent fields and returns the updated record

#### Scenario: Update of a foreign subject is refused
- **WHEN** an authenticated user sends `PATCH /subjects/{subject_id}` for a
  subject owned by another user
- **THEN** the system refuses with `accessdenied`
- **AND** the record is not modified

#### Scenario: Unknown subject id
- **WHEN** an authenticated user sends `PATCH /subjects/{subject_id}` with an
  id that does not exist
- **THEN** the system responds with `notfound`

#### Scenario: Partial update keeps the other fields
- **WHEN** an authenticated user sends `PATCH /subjects/{subject_id}` with only
  the `name` field
- **THEN** the system updates `name`
- **AND** `teacher` and `hours` keep their previous values

### Requirement: Delete a subject owned by the authenticated user
The system SHALL expose an endpoint `DELETE /subjects/{subject_id}` that
requires authentication, loads the subject by id and refuses the request when
the subject belongs to another user.

#### Scenario: Owner deletes their subject
- **WHEN** an authenticated user sends `DELETE /subjects/{subject_id}` for a
  subject they own
- **THEN** the system deletes the record

#### Scenario: Delete of a foreign subject is refused
- **WHEN** an authenticated user sends `DELETE /subjects/{subject_id}` for a
  subject owned by another user
- **THEN** the system refuses with `accessdenied`
- **AND** the record is not deleted

#### Scenario: Unknown subject id
- **WHEN** an authenticated user sends `DELETE /subjects/{subject_id}` with an
  id that does not exist
- **THEN** the system responds with `notfound`
