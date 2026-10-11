"""PawPal+ Streamlit UI."""

from datetime import date, time

import streamlit as st

from pawpal_system import Owner, Pet, Scheduler, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾")
st.title("🐾 PawPal+")

# Streamlit re-runs this whole file on every click, so the Owner must
# live in session_state or it would be recreated (empty) each time.
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Pet Owner")

owner = st.session_state.owner
scheduler = Scheduler(owner)

# ---------------------------------------------------------------- Add a pet
st.header("1. Add a pet")
with st.form("add_pet_form", clear_on_submit=True):
    pet_name = st.text_input("Pet name")
    species = st.selectbox("Species", ["dog", "cat", "bird", "other"])
    age = st.number_input("Age", min_value=0, max_value=40, value=1)
    add_pet_clicked = st.form_submit_button("Add pet")

if add_pet_clicked:
    clean_name = pet_name.strip()
    if not clean_name:
        st.warning("Please enter a pet name.")
    elif owner.get_pet(clean_name) is not None:
        st.warning(f"You already have a pet named {clean_name}.")
    else:
        owner.add_pet(Pet(clean_name, species, int(age)))
        st.success(f"Added {clean_name} the {species}!")

# -------------------------------------------------------------- Add a task
st.header("2. Schedule a task")
if not owner.pets:
    st.info("Add a pet first, then you can schedule tasks for it.")
else:
    with st.form("add_task_form", clear_on_submit=True):
        chosen_pet = st.selectbox("Pet", [p.name for p in owner.pets])
        description = st.text_input("Task (e.g. Morning walk)")
        task_time = st.time_input("Time", value=time(8, 0))
        due = st.date_input("Date", value=date.today())
        frequency = st.selectbox("Repeats", ["once", "daily", "weekly"])
        add_task_clicked = st.form_submit_button("Add task")

    if add_task_clicked:
        if not description.strip():
            st.warning("Please describe the task.")
        else:
            new_task = Task(
                description.strip(),
                task_time.strftime("%H:%M"),
                due_date=due,
                frequency=frequency,
            )
            owner.get_pet(chosen_pet).add_task(new_task)
            st.success(f"Scheduled '{description.strip()}' for {chosen_pet}.")

# ---------------------------------------------------------------- Schedule
st.header("3. Schedule")
all_tasks = scheduler.sort_by_time()

if not all_tasks:
    st.info("No tasks yet.")
else:
    for warning in scheduler.detect_conflicts():
        st.warning(warning)

    st.table(
        [
            {
                "Date": str(t.due_date),
                "Time": t.time,
                "Pet": t.pet_name,
                "Task": t.description,
                "Repeats": t.frequency,
                "Done": "✅" if t.completed else "",
            }
            for t in all_tasks
        ]
    )

    pending = scheduler.sort_by_time(scheduler.filter_tasks(completed=False))
    if pending:
        st.subheader("Mark a task complete")
        labels = [
            f"{t.due_date} {t.time} - {t.pet_name}: {t.description}"
            for t in pending
        ]
        picked = st.selectbox(
            "Pending tasks", range(len(pending)), format_func=lambda i: labels[i]
        )
        if st.button("Mark complete"):
            scheduler.complete_task(pending[picked])
            st.rerun()