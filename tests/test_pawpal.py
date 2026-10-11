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