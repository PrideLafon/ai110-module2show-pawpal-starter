# PawPal+ (Module 2 Project)

PawPal+ is a Streamlit app that helps a busy pet owner plan care tasks (walks, feeding, medication, appointments) for one or more pets. The logic lives in a small set of Python classes, with a command-line demo, an automated test suite, and a web UI on top.

## Features

- **Multi-pet management:** one owner can have many pets, each with its own tasks.
- **Sorting by time:** all tasks across all pets appear in chronological order.
- **Filtering:** view tasks by pet name or by completion status.
- **Conflict warnings:** tasks scheduled at the same date and time are flagged.
- **Recurring tasks:** completing a daily or weekly task creates the next one.
- **Streamlit UI:** add pets and tasks, see the sorted schedule, and mark tasks done.

## System Overview

PawPal+ is built from four classes in `pawpal_system.py`:

- `Task` represents one chore and can mark itself complete (creating the next occurrence if it repeats).
- `Pet` stores a pet's details and its list of tasks.
- `Owner` holds a list of pets and can return every task across all of them.
- `Scheduler` takes an owner and handles sorting, filtering, conflict detection, and recurring tasks across all pets.

The UML diagrams are in `diagrams/uml_draft.mmd` (initial design) and `diagrams/uml_final.mmd` (final design).

## How to Run

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
python -m streamlit run app.py
python -m pytest
```

- `python main.py` runs the command-line demo.
- `python -m streamlit run app.py` starts the web app.
- `python -m pytest` runs the tests.

## Sample Output

Output from running `python main.py`:

```
Today's Schedule
----------------------------------------------------------
[ ] 2026-10-10 07:30  Buddy   Breakfast (daily)
[ ] 2026-10-10 07:30  Luna    Medication (once)
[ ] 2026-10-10 14:00  Luna    Vet appointment (once)
[ ] 2026-10-10 18:00  Buddy   Evening walk (daily)

Warnings
----------------------------------------------------------
! Conflict on 2026-10-10 at 07:30 -> Buddy: Breakfast, Luna: Medication

Buddy's tasks after completing Breakfast
----------------------------------------------------------
[x] 2026-10-10 07:30  Buddy   Breakfast (daily)
[ ] 2026-10-10 18:00  Buddy   Evening walk (daily)
[ ] 2026-10-11 07:30  Buddy   Breakfast (daily)

Pending tasks only
----------------------------------------------------------
[ ] 2026-10-10 07:30  Luna    Medication (once)
[ ] 2026-10-10 14:00  Luna    Vet appointment (once)
[ ] 2026-10-10 18:00  Buddy   Evening walk (daily)
[ ] 2026-10-11 07:30  Buddy   Breakfast (daily)
```

## Smarter Scheduling

| Feature | Method | Behavior |
|---|---|---|
| Sorting | `Scheduler.sort_by_time()` | Orders tasks by due date, then by `HH:MM` time |
| Filtering | `Scheduler.filter_tasks()` | Filters by pet name and/or completion status |
| Conflict detection | `Scheduler.detect_conflicts()` | Returns a warning for each date/time with more than one unfinished task |
| Recurring tasks | `Task.mark_complete()` and `Scheduler.complete_task()` | A daily task creates a copy for tomorrow, a weekly task for 7 days later |

## Demo Walkthrough

**Main UI features:** add a pet, schedule a task for a pet (time, date, repeat), view the sorted schedule with conflict warnings, and mark a task complete.

**Example workflow:**

1. Add two pets, Buddy and Luna.
2. Schedule a daily 08:00 task for Buddy and a task for Luna at 08:00.
3. A warning appears because both tasks share the same time.
4. Mark Buddy's task complete and a new one appears for tomorrow.

**Key Scheduler behaviors shown:** sorting

## Extension: Priority Scheduling

Tasks have a `priority` field (`"high"`, `"medium"`, or `"low"`, default `"medium"`). `Scheduler.sort_by_priority()` sorts by priority first, then by date and time, using the `PRIORITY_ORDER` lookup table in `pawpal_system.py`.

Files modified: `pawpal_system.py` (new field, lookup table, method), `main.py` (demo), `tests/test_pawpal.py` (new test).

Sample output from `python main.py`:

```
Priority schedule (high first, then by time)
----------------------------------------------------------
[HIGH  ] 20:00  Luna    Flea treatment
[MEDIUM] 07:30  Luna    Medication
[MEDIUM] 14:00  Luna    Vet appointment
[MEDIUM] 18:00  Buddy   Evening walk
[LOW   ] 09:00  Buddy   Grooming

```

Tradeoff: priority is applied across all dates, so for a multi-day list a high-priority task next week would outrank a low-priority task today. The demo applies it to today's tasks only.