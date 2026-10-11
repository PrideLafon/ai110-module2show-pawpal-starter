# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
# Paste your pytest output here
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | | e.g., by priority, duration |
| Filtering | | e.g., skip tasks if time runs out |
| Conflict handling | | e.g., overlapping time slots |
| Recurring tasks | | e.g., daily vs. weekly |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->

## Sample Output
'''

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
'''

## Implementation Summary

PawPal+ is built from four classes in `pawpal_system.py`. `Task` represents one chore and can mark itself complete (creating the next occurrence if it repeats). `Pet` stores a pet's details and tasks. `Owner` holds a list of pets and can return every task across all of them. `Scheduler` takes an owner and handles sorting, filtering, conflict detection, and recurring tasks across all pets. `main.py` is a command-line demo that exercises all of this.

## Testing PawPal+

Run the automated tests from the project root with:

```
python -m pytest
```

### What the tests cover

- **Task completion:** `mark_complete()` sets `completed` to `True`.
- **Task addition:** adding a task to a pet increases its task count.
- **Sorting:** tasks from different pets come back in chronological order.
- **Recurrence:** completing a daily task creates an unfinished copy dated tomorrow.
- **Conflict detection:** two pets with tasks at the same time produce a warning.
- **Filtering:** tasks can be filtered by pet name and by completion status.
- **Edge case:** a household with no tasks returns empty results without crashing.

### Sample test output

```
============================= test session starts =============================
platform win32 -- Python 3.14.8, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\PrideLafon\Documents\GitHub\ai110-module2show-pawpal-starter
plugins: anyio-4.15.1
collected 7 items

tests\test_pawpal.py .......                                             [100%]

============================== 7 passed in 0.06s ==============================

```

### Confidence level

★★★★☆ (4/5). All 7 tests pass and they cover the core behavior. Conflict detection only checks for exact matching times, so overlapping durations are not tested.

## Features

- **Multi-pet management:** one owner can have many pets, each with its own tasks.
- **Sorting by time:** all tasks across all pets appear in chronological order.
- **Filtering:** view tasks by pet name or by completion status.
- **Conflict warnings:** tasks scheduled at the same date and time are flagged.
- **Recurring tasks:** completing a daily or weekly task creates the next one.
- **Streamlit UI:** add pets and tasks, see the sorted schedule, and mark tasks done.

## System Overview

PawPal+ is built from four classes in `pawpal_system.py`:

- `Task` represents one chore and can mark itself complete.
- `Pet` stores a pet's details and its list of tasks.
- `Owner` holds a list of pets and can return every task across all of them.
- `Scheduler` takes an owner and handles sorting, filtering, conflict detection, and recurring tasks across all pets.

The UML diagram is in `diagrams/uml_final.mmd`.

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

**Key Scheduler behaviors shown:** sorting across pets, conflict warnings, and daily recurrence. The Sample Output section above shows the command-line version.

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