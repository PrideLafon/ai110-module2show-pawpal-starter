"""CLI demo for PawPal+."""

from pawpal_system import Owner, Pet, Scheduler, Task


def print_schedule(title, tasks):
    """Print a list of tasks as a readable table."""
    print(f"\n{title}")
    print("-" * 58)
    if not tasks:
        print("(nothing here)")
    for t in tasks:
        mark = "x" if t.completed else " "
        print(
            f"[{mark}] {t.due_date} {t.time}  "
            f"{t.pet_name:<7} {t.description} ({t.frequency})"
        )


def main():
    """Build a sample household and demo the scheduler."""
    # 1. Create an owner and two pets.
    owner = Owner("Pride")
    buddy = Pet("Buddy", "dog", 3)
    luna = Pet("Luna", "cat", 5)
    owner.add_pet(buddy)
    owner.add_pet(luna)

    # 2. Add tasks OUT OF ORDER on purpose.
    buddy.add_task(Task("Evening walk", "18:00", frequency="daily"))
    breakfast = Task("Breakfast", "07:30", frequency="daily")
    buddy.add_task(breakfast)
    luna.add_task(Task("Medication", "07:30"))
    luna.add_task(Task("Vet appointment", "14:00"))

    scheduler = Scheduler(owner)

    # 3. Sorted schedule across BOTH pets.
    print_schedule("Today's Schedule", scheduler.get_todays_schedule())

    # 4. Conflict warnings.
    print("\nWarnings")
    print("-" * 58)
    for warning in scheduler.detect_conflicts():
        print("!", warning)

    # 5. Complete a daily task: tomorrow's copy appears.
    scheduler.complete_task(breakfast)
    buddy_tasks = scheduler.filter_tasks(pet_name="Buddy")
    print_schedule(
        "Buddy's tasks after completing Breakfast",
        scheduler.sort_by_time(buddy_tasks),
    )

    # 6. Pending tasks only, across both pets.
    pending = scheduler.filter_tasks(completed=False)
    print_schedule("Pending tasks only", scheduler.sort_by_time(pending))


    # 7. Priority-based schedule (extension).
    buddy.add_task(Task("Grooming", "09:00", priority="low"))
    luna.add_task(Task("Flea treatment", "20:00", priority="high"))

    print("\nPriority schedule (high first, then by time)")
    print("-" * 58)
    todays = scheduler.get_todays_schedule()
    for t in scheduler.sort_by_priority(todays):
        print(
            f"[{t.priority.upper():<6}] {t.time}  "
            f"{t.pet_name:<7} {t.description}"
        )

if __name__ == "__main__":
    main()