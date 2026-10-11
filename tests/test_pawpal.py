"""Pytest suite for PawPal+."""

from datetime import date, timedelta

from pawpal_system import Owner, Pet, Scheduler, Task


def make_scheduler():
    """Build an owner with two pets and a scheduler."""
    owner = Owner("Test")
    dog = Pet("Rex", "dog")
    cat = Pet("Mia", "cat")
    owner.add_pet(dog)
    owner.add_pet(cat)
    return Scheduler(owner), dog, cat


def test_mark_complete_changes_status():
    """Calling mark_complete() should flip completed to True."""
    task = Task("Walk", "08:00")

    task.mark_complete()

    assert task.completed is True


def test_adding_task_increases_task_count():
    """Adding a task to a pet should grow that pet's task list."""
    pet = Pet("Rex", "dog")

    pet.add_task(Task("Feed", "09:00"))

    assert len(pet.tasks) == 1


def test_sort_by_time_across_pets():
    """Tasks from different pets come back in chronological order."""
    scheduler, dog, cat = make_scheduler()
    dog.add_task(Task("Late", "18:00"))
    cat.add_task(Task("Early", "06:00"))
    dog.add_task(Task("Middle", "12:00"))

    times = [t.time for t in scheduler.sort_by_time()]

    assert times == ["06:00", "12:00", "18:00"]


def test_daily_task_creates_next_day_copy():
    """Completing a daily task adds a new, unfinished task for tomorrow."""
    scheduler, dog, _ = make_scheduler()
    task = Task("Feed", "08:00", frequency="daily")
    dog.add_task(task)

    scheduler.complete_task(task)

    assert len(dog.tasks) == 2
    assert dog.tasks[1].due_date == date.today() + timedelta(days=1)
    assert dog.tasks[1].completed is False


def test_conflict_detected_between_different_pets():
    """Two pets with a task at the same time should trigger a warning."""
    scheduler, dog, cat = make_scheduler()
    dog.add_task(Task("Walk", "08:00"))
    cat.add_task(Task("Meds", "08:00"))

    warnings = scheduler.detect_conflicts()

    assert len(warnings) == 1


def test_filter_by_pet_and_by_status():
    """Filtering returns only matching tasks."""
    scheduler, dog, cat = make_scheduler()
    done = Task("A", "07:00")
    dog.add_task(done)
    cat.add_task(Task("B", "08:00"))
    done.mark_complete()

    mia_tasks = scheduler.filter_tasks(pet_name="Mia")
    finished = scheduler.filter_tasks(completed=True)

    assert [t.description for t in mia_tasks] == ["B"]
    assert finished == [done]


def test_pet_with_no_tasks():
    """Edge case: an empty household should not crash anything."""
    scheduler, _, _ = make_scheduler()

    assert scheduler.sort_by_time() == []
    assert scheduler.detect_conflicts() == []