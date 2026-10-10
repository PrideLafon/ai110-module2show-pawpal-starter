"""PawPal+ logic layer: Task, Pet, Owner, and Scheduler classes."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional


@dataclass
class Task:
    """A single pet-care activity (feeding, walk, medication...)."""

    description: str
    time: str  # "HH:MM" in 24-hour format
    due_date: date = field(default_factory=date.today)
    frequency: str = "once"  # "once", "daily", or "weekly"
    completed: bool = False
    pet_name: str = ""

    def mark_complete(self) -> Optional[Task]:
        """Mark done; return the next occurrence if the task repeats."""
        pass


@dataclass
class Pet:
    """A pet and the tasks that belong to it."""

    name: str
    species: str
    age: int = 0
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        """Attach a task to this pet."""
        pass

    def remove_task(self, task: Task) -> None:
        """Remove a task from this pet."""
        pass

    def get_tasks(self) -> List[Task]:
        """Return this pet's tasks."""
        pass


class Owner:
    """A pet owner who manages one or more pets."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to this owner."""
        pass

    def get_all_tasks(self) -> List[Task]:
        """Return every task from every pet."""
        pass


class Scheduler:
    """The 'brain': organizes and manages tasks across all pets."""

    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def get_all_tasks(self) -> List[Task]:
        """Fetch all tasks via the Owner."""
        pass

    def sort_by_time(self) -> List[Task]:
        """Return tasks in chronological order."""
        pass

    def filter_tasks(self) -> List[Task]:
        """Return tasks filtered by pet or completion status."""
        pass

    def detect_conflicts(self) -> List[str]:
        """Return warnings for tasks scheduled at the same time."""
        pass

    def complete_task(self, task: Task) -> None:
        """Complete a task and schedule the next one if it repeats."""
        pass

    def get_todays_schedule(self) -> List[Task]:
        """Return today's tasks in time order."""
        pass