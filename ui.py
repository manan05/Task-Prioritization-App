import streamlit as st
from ics import Calendar
from datetime import datetime

# Title of the app
st.title('Task Prioritization App')

# Subheader for calendar section
st.subheader('Upload Your Calendar (.ics) File')

# File uploader widget for .ics files
uploaded_file = st.file_uploader("Choose an .ics file", type="ics")

# List to store tasks (parsed from .ics)
tasks = []

# Parse and display calendar events if a file is uploaded
if uploaded_file is not None:
    # Read the content of the .ics file
    calendar_data = uploaded_file.read().decode("utf-8")

    # Parse the file using ics library
    cal = Calendar(calendar_data)

    st.write("### Calendar Events:")

    # Loop through events and add them to the task list
    for event in cal.events:
        # Extract task details from each event
        task_name = event.name
        task_start = event.begin.datetime
        task_end = event.end.datetime
        task_priority = "Medium"  # You can add logic to assign priority

        # Append the task to the list
        tasks.append({
            "title": task_name,
            "start": task_start.isoformat(),
            "end": task_end.isoformat()
        })

else:
    st.write("Please upload an .ics file to see the events.")

# View Toggle: List View or Calendar View
view_option = st.radio("Choose a view", ('List View', 'Calendar View'))

# If List View is selected
if view_option == 'List View':
    st.write("### Prioritized Task List:")
    if tasks:
        for t in tasks:
            st.write(f"Task: {t['title']} | Start: {t['start']} | End: {t['end']}")
    else:
        st.write("No tasks available.")

# If Calendar View is selected
elif view_option == 'Calendar View':
    # Convert tasks into JavaScript array format for FullCalendar
    task_events_js = str(tasks).replace("'", '"')

    # FullCalendar HTML with embedded JavaScript for month, week, and day views
    fullcalendar_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <link href='https://cdn.jsdelivr.net/npm/fullcalendar@5.11.0/main.min.css' rel='stylesheet' />
        <script src='https://cdn.jsdelivr.net/npm/fullcalendar@5.11.0/main.min.js'></script>
        <script>
          document.addEventListener('DOMContentLoaded', function() {{
            var calendarEl = document.getElementById('calendar');

            var calendar = new FullCalendar.Calendar(calendarEl, {{
              initialView: 'dayGridMonth',  // Default view (can be dayGridMonth, timeGridWeek, timeGridDay)
              headerToolbar: {{
                left: 'prev,next today',
                center: 'title',
                right: 'dayGridMonth,timeGridWeek,timeGridDay'
              }},
              events: {task_events_js},  // Insert tasks here
              eventDisplay: 'block',  // Ensures events are wrapped properly
              editable: true,  // Enables dragging and resizing (optional)
              eventResizableFromStart: true  // Allows resizing of events from start
            }});

            calendar.render();
          }});
        </script>
    </head>
    <body>
      <div id='calendar'></div>
    </body>
    </html>
    """

    # Streamlit to embed the FullCalendar HTML
    st.components.v1.html(fullcalendar_html, height=600)

    st.write("""
    ### Calendar View
    This calendar supports multiple views:
    - *Month* view shows the entire month.
    - *Week* view shows one week at a time.
    - *Day* view shows a single day's tasks.
    """)

# Key for toggling the manual task form
myKey = 'show_manual_task_form'

# Initialize session state if it doesn't exist
if myKey not in st.session_state:
    st.session_state[myKey] = False

# Toggle form visibility based on button click
if st.session_state[myKey]:
    # Show the form and display the "Cancel" button
    myBtn = st.button('Cancel')
    st.subheader("Add a Task Manually")

    # Manual task form input
    manual_task_name = st.text_input("Task Name")
    manual_task_priority = st.selectbox("Task Priority", ["Low", "Medium", "High"])
    manual_task_date = st.date_input("Task Date", datetime.now())
    manual_task_time = st.time_input("Task Time", datetime.now().time())

    if st.button("Add Manual Task"):
        manual_task_start = datetime.combine(manual_task_date, manual_task_time)
        tasks.append({
            "title": manual_task_name,
            "start": manual_task_start.isoformat(),
            "end": manual_task_start.isoformat()  # Modify this if you want a longer event duration
        })
        st.success(f"Manual Task '{manual_task_name}' added successfully!")

        # Re-sort tasks after adding a new manual task
        sorted_tasks = sorted(tasks, key=lambda x: (x['start'], x['end']))

        # Display updated prioritized task list
        st.write("### Updated Prioritized Task List:")
        for t in sorted_tasks:
            st.write(f"Task: {t['title']} | Start: {t['start']} | End: {t['end']}")
else:
    # Show "Add a Task Manually" button when form is hidden
    myBtn = st.button('Add a Task Manually')

# Toggle session state based on button clicks
if myBtn:
    st.session_state[myKey] = not st.session_state[myKey]