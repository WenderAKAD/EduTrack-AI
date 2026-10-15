# Proposal

## Why

The EduTrack AI backend now stores the student's tasks (`academic_tasks`, Tarefa
11) but has no way to summarise how much of a subject is done. The dashboard
needs a single number per subject — the completion percentage — and computing it
with visual blocks alone would be fragile. A small custom function in Python
solves that case: it receives the subject's tasks as JSON and returns the
progress as JSON.

## What Changes

- Add a pure-Python script at `scripts/calculate_progress.py` that computes the
  completion percentage of a subject from its tasks.
- The function `calculate_progress(completed_tasks, total_tasks)` SHALL return a
  JSON object with a single key, `percentage`, between `0` and `100`.
- A helper `calculate_subject_progress(tasks)` SHALL derive `completed_tasks` and
  `total_tasks` from a list of tasks.
- Division by zero SHALL be handled: when there are no tasks, `percentage` is
  `0` instead of raising.

Out of scope, because it was not requested: a Xano API endpoint (that is Tarefa
13), persistence, a chart, and any definition of new task statuses. The script
runs locally; publishing it to Xano is a manual step of the developer.

## Capabilities

### New Capabilities

- `progress-calculation`: the rule that turns a subject's tasks into a
  completion percentage.

### Modified Capabilities

None. `academic-tasks` provides the input data but does not change.

## Impact

- **New file:** `scripts/calculate_progress.py` (Python standard library only).
- **No table and no API change.** The script is called with JSON in and returns
  JSON out; wiring it into Xano is out of scope and manual.
- **Depends on:** the shape of a task from `academic_tasks` — a `status` field.
