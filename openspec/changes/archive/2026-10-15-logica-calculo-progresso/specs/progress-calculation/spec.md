# Progress Calculation Specification

## Purpose

Define how the completion percentage of a subject is computed from its tasks by
the custom Python function `scripts/calculate_progress.py`.

## ADDED Requirements

### Requirement: Compute completion percentage
The system SHALL expose a function `calculate_progress(completed_tasks,
total_tasks)` that returns a JSON object with a single key, `percentage`, equal
to `completed_tasks / total_tasks * 100`, rounded to two decimal places and
bounded between `0` and `100`.

#### Scenario: Half of the tasks are done
- **WHEN** `calculate_progress` is called with `completed_tasks = 1` and `total_tasks = 2`
- **THEN** it returns `{"percentage": 50.0}`

#### Scenario: All tasks are done
- **WHEN** `calculate_progress` is called with `completed_tasks = 4` and `total_tasks = 4`
- **THEN** it returns `{"percentage": 100.0}`

#### Scenario: Result carries the percentage key
- **WHEN** the function returns
- **THEN** the returned JSON object has exactly the key `percentage`

### Requirement: Handle division by zero
The system SHALL NOT raise on a subject without tasks. When `total_tasks` is
zero or negative, `percentage` SHALL be `0`.

#### Scenario: Subject has no tasks
- **WHEN** `calculate_progress` is called with `total_tasks = 0`
- **THEN** it returns `{"percentage": 0}` and does not raise `ZeroDivisionError`

#### Scenario: Empty task list
- **WHEN** the function is called with an empty list of tasks
- **THEN** it returns `{"percentage": 0}`

### Requirement: Derive progress from a task list
The system SHALL provide a helper `calculate_subject_progress(tasks)` that takes
the list of a subject's tasks and derives `completed_tasks` and `total_tasks`
from it. A task SHALL count as completed when its `status`, after trimming and
lower-casing, equals `completed`; every other status counts as not done.

#### Scenario: Count completed tasks
- **WHEN** the list contains tasks whose statuses are `completed`, `pending` and `completed`
- **THEN** the function counts two completed tasks out of three and returns `{"percentage": 66.67}`

#### Scenario: Status comparison ignores case and spaces
- **WHEN** a task's `status` is `" Completed "`
- **THEN** the task counts as completed

#### Scenario: Other statuses are not completed
- **WHEN** a task `status` is anything other than `completed`
- **THEN** that task counts as not done

### Requirement: Pure Python with no external dependencies
The script SHALL run with the Python standard library only, importing nothing
beyond `json`, so it can run inside the constrained environment of a Xano custom
function. The file SHALL live at `scripts/calculate_progress.py` and SHALL accept
JSON in and produce JSON out.

#### Scenario: No external imports
- **WHEN** the script's imports are inspected
- **THEN** the only module imported is `json` from the standard library

#### Scenario: JSON in, JSON out
- **WHEN** the script is given a task list as JSON
- **THEN** it produces a JSON object containing the `percentage` key

#### Scenario: Script runs standalone
- **WHEN** the file is executed with `python scripts/calculate_progress.py`
- **THEN** it prints example results and exits without error
