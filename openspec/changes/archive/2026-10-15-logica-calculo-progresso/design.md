# Design

## Context

See `proposal.md` — Why and `specs/progress-calculation/spec.md` for the
requirements. Two constraints drive the design:

- The data crosses a boundary as JSON: the Xano side sends the tasks and expects
  the result back in the same format. The script therefore deals in plain
  dictionaries — no external dependency, so it can run in the restricted
  environment of a Xano custom function.
- Python is sensitive to indentation and to division by zero, both called out in
  the task's troubleshooting notes.

## Decisions

**JSON in, JSON out, one key.** The result is `{"percentage": <number>}`. A
single, predictable key keeps the contract with the caller small and easy to
consume in the frontend or in Xano.

**`percentage` is `0`–`100`, rounded to two decimals.** `completed_tasks /
total_tasks * 100`, rounded to two decimals, gives a stable value for display
without floating-point noise.

**Division by zero returns `0`.** `if total_tasks <= 0: return {"percentage": 0}`.
A subject without tasks has no progress to show, and the alternative — raising
`ZeroDivisionError` — would break the caller. This is the error handling the
task explicitly asks for.

**A task is completed when `status` is `completed`.** The comparison trims the
value and ignores case, so `" completed "` and `"Completed"` both count. Only
this value is treated as done; any other status counts as not done.

**Pure Python, standard library only.** No `import` beyond `json`. Custom
functions in Xano run in a constrained environment, and the task's tips warn
that not every library works there. Keeping to built-ins removes that risk.

**No `guid`, no table, no API.** This change produces a file, not a Xano
resource. Publishing to Xano is a manual developer step.
