# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**
- A user can add a pet so that the app knows who needs care.
- A user can edit or reschedule a task so the day's plan adapts when something unexpected comes up.
- A user can view today's tasks in time order, with warnings for clashes, so they know what to do next and when.

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

    I designed four classes. `Task` represents one chore (description, time, date, frequency, completion status) and can mark itself complete. `Pet` stores a pet's details and its list of tasks. `Owner` stores the owner's name and list of pets, and can return every task from every pet in one list. `Scheduler` is the "brain": it holds an owner and organizes tasks across all of their pets (sorting, filtering, conflict warnings, and recurring tasks). The relationships are: an Owner has many Pets, a Pet has many Tasks, and the Scheduler reads from the Owner rather than from a single pet.

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

    Yes, my design changed after I asked an AI assistant to review my skeleton. I accepted three suggestions:

1. `Pet.add_task()` now stamps the pet's name onto the task, because the Scheduler sees all tasks mixed together and needs to know whose each one is.
2. I added `Owner.get_pet(name)` so the Scheduler can find the right pet when it has to add the next occurrence of a recurring task.
3. I gave `filter_tasks()` parameters (pet name and completion status) and let `sort_by_time()` and `detect_conflicts()` accept a list of tasks, so they can be reused on filtered results.


---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
