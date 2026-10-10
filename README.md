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
