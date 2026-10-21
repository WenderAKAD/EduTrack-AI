# subjects Specification

## Purpose

Add advanced hybrid search for subjects, combining Xano database filtering with Python logic to find subjects by name or by overdue tasks.

## ADDED Requirements

### Requirement: Search subjects by name
The system SHALL provide an authenticated endpoint to search subjects by name with partial, case-insensitive matching, scoped to the authenticated user.

#### Scenario: Search by partial name
- **WHEN** an authenticated user calls the search endpoint with query parameter `q` containing part of a subject name
- **THEN** the system returns only subjects belonging to that user whose name matches the query case-insensitively

#### Scenario: Empty query returns all user's subjects
- **WHEN** an authenticated user calls the search endpoint with no `q` parameter
- **THEN** the system returns all subjects belonging to that user (subject to other filters)

### Requirement: Search subjects with overdue tasks using Python
The system SHALL integrate Python logic to identify subjects that have at least one incomplete task past its due date, and allow filtering for them.

#### Scenario: Filter overdue subjects
- **WHEN** an authenticated user calls the search endpoint with `overdue=true`
- **THEN** the Python logic analyzes academic_tasks for that user's subjects to find tasks where status is not completed and due_date < current date
- **AND** the system returns only subjects that have at least one overdue incomplete task

#### Scenario: Combine name search with overdue filter
- **WHEN** an authenticated user calls the search endpoint with both `q` and `overdue=true`
- **THEN** the system applies both filters (name match AND has overdue task)
- **AND** results are still scoped to the authenticated user

### Requirement: Security and authentication
The search endpoint SHALL require authentication and only return data belonging to the authenticated user.

#### Scenario: Unauthenticated request
- **WHEN** a request is made without valid authentication
- **THEN** the system rejects the request
