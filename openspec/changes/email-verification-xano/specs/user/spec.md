# user Specification

## Purpose
Defines the email verification rules and security preconditions for registering users in the EduTrack AI Xano backend.

## ADDED Requirements

### Requirement: Email verification code table
The system SHALL store temporary verification codes in an `email_verification` table in Xano.

| Field | Type | Rules |
|---|---|---|
| `id` | int | auto-generated, primary key |
| `email` | email | required, trimmed, lowercased |
| `code` | text | required, 6 digits |
| `expires_at` | timestamp | required |
| `verified` | bool | optional, defaults to `false` |
| `created_at` | timestamp | optional, defaults to `now` |

#### Scenario: Code is recorded with expiration
- **WHEN** a verification code is requested for an email
- **THEN** a record is created with the 6-digit code and an expiration timestamp 15 minutes in the future

### Requirement: Request verification code endpoint
The system SHALL expose `POST /auth/send-verification-code` in the `AutenticacaoEduTrackIAEst` API group.

#### Scenario: Code generated for unregistered email
- **WHEN** `POST /auth/send-verification-code` is called with an email not present in `user`
- **THEN** system generates a 6-digit code, stores it in `email_verification` and returns HTTP 200

#### Scenario: Rejection when email already registered
- **WHEN** `POST /auth/send-verification-code` is called with an email already present in `user`
- **THEN** system rejects with `accessdenied` error "Este e-mail ja esta em uso."

### Requirement: Mandatory verification code in signup
The system SHALL require a valid `verification_code` input in `POST /auth/signup` and reject registration if missing, incorrect, or expired.

#### Scenario: Signup succeeds with valid verification code
- **WHEN** `POST /auth/signup` is called with valid email, name, password and matching non-expired code
- **THEN** user record is created in `user` table and JWT auth token is returned

#### Scenario: Signup rejected with invalid or expired code
- **WHEN** `POST /auth/signup` is called with an incorrect code or expired code
- **THEN** system rejects with `accessdenied` error "Codigo de verificacao invalido ou expirado." and no user is created
