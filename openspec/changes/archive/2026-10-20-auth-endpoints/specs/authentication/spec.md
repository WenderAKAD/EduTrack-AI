# authentication Specification

## Purpose

Issue JWT tokens for the EduTrack AI backend, so the protected endpoints
(`subjects` and later capabilities) can identify the authenticated user through
`$auth.id`.

## ADDED Requirements

### Requirement: Register a user and issue a token
The system SHALL expose an endpoint `POST /auth/signup` that accepts `name`,
`email` and `password`, rejects an e-mail already registered, stores the new
user in the `user` table and returns an authentication token.

#### Scenario: New user signs up
- **WHEN** a visitor sends `POST /auth/signup` with a new `name`, `email` and
  `password`
- **THEN** the system creates the user in the `user` table
- **AND** returns an `authToken`

#### Scenario: Duplicate e-mail
- **WHEN** a visitor sends `POST /auth/signup` with an `email` already in use
- **THEN** the system refuses with `accessdenied`
- **AND** no new user is created

### Requirement: Authenticate a user and issue a token
The system SHALL expose an endpoint `POST /auth/login` that accepts `email` and
`password`, validates them against the `user` table and returns an
authentication token.

#### Scenario: Valid credentials
- **WHEN** a user sends `POST /auth/login` with a registered `email` and the
  correct `password`
- **THEN** the system returns an `authToken`

#### Scenario: Invalid credentials
- **WHEN** a user sends `POST /auth/login` with an unknown `email` or a wrong
  `password`
- **THEN** the system refuses with an `Invalid Credentials` error
- **AND** both cases return the same message

### Requirement: The issued token authenticates the protected endpoints
The system SHALL issue tokens valid for the group `Autenticacao EduTrackIA Est`,
so a token from `signup` or `login` is accepted by the `subjects` endpoints and
resolves to the correct `$auth.id`.

#### Scenario: Token from login opens a protected endpoint
- **WHEN** a client sends `GET /subjects` with the `authToken` returned by
  `POST /auth/login`
- **THEN** the system accepts the token
- **AND** returns only the subjects whose `user_id` equals the token's user id
