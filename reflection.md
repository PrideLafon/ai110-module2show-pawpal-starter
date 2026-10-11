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

My scheduler considers time (date and HH:MM), which pet a task belongs to, whether it is completed, and how often it repeats. I treated time as the most important constraint because the app's main job is telling the owner what to do next, so everything is sorted by it. I did not build priority levels or owner availability, to keep the design simple and testable.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

My conflict detection only flags tasks that start at exactly the same date and time. It does not check whether a long task overlaps a later one, for example a 30-minute walk at 08:00 and a task at 08:15. This is reasonable here because tasks have no duration field, and an exact-match check is simple, easy to test, and catches the most obvious clashes. The cost is that real overlaps can slip through.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used Claude in a chat window, not an in-editor assistant, to guide me through the project step by step. I used it for design brainstorming (turning my three user actions into four classes), generating the Mermaid UML and the class skeleton, explaining concepts like dataclasses, lambda sort keys and `st.session_state`, and debugging setup problems such as the PowerShell script error and the missing `__init__` in my `Owner` class. I wrote my own three core actions and made the final design decisions.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

I verified AI-generated code by running each piece in the terminal and comparing the output to what I expected before moving on, then locking the behavior in with 7 pytest tests. I also broke a method on purpose to confirm a test would fail. When my demo test failed with "Owner() takes no arguments," I traced it to a method I had accidentally overwritten and fixed it myself.

The AI suggested replacing my third core action ("delete a pet") with a "view today's tasks" action, because none of my actions needed the Scheduler class. I kept "delete a pet" as a possible future feature.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested task completion, adding a task to a pet, sorting tasks across two pets, daily recurrence (a new unfinished task dated tomorrow), conflict detection between different pets, filtering by pet name and completion status, and an empty household. These matter because each one protects a behavior the UI depends on, and the empty case checks that nothing crashes with no data.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I am fairly confident (4 out of 5) in the core logic because all 7 tests pass. If I had more time I would test weekly recurrence, overlapping task durations, tasks crossing a month boundary, duplicate pet names, and times entered without a leading zero like "7:30", which would sort incorrectly because times are compared as text.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I am most satisfied that I built and tested the logic in the terminal before connecting the UI, so the Streamlit app only calls methods I had already verified.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would add task durations so overlaps can be detected, priority levels, and saving to a file, because right now everything is lost when the browser page refreshes. I would also add a way to remove a pet in case the owner looses them for one reason or the other.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

I learned that using AI well means deciding the design myself and then checking every result by running it. I worked in one continuous chat instead of separate sessions per phase, which kept earlier decisions in context but made the conversation long, so next time I would start a fresh session for testing and for the UI.
