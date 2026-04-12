# Task Tracker App

## Problem
Users are unable to keep track of their tasks.Task Tracker would give them a way to store their tasks and mark them completed as they have finished it

## Features

### Add Tasks
- Create tasks with title and description
  - Title is required (max 100 characters)
  - Description is optional
- Set optional due dates
- Assign priority levels (high, medium, low)

### View Tasks
- Display all tasks with status
- Filter by priority or due date
- Show completed and pending separately

### Mark Complete
- Mark tasks as done
- Track completion timestamps
- Move completed tasks to archive

### Delete Tasks
- Remove tasks permanently
- Confirm before deleting to prevent accidents


## Dependencies

This project utilizes the following external libraries to enhance the CLI experience:

| Library | Purpose | Documentation |
| :--- | :--- | :--- |
| **Inquirer** | Manages interactive menus and user input prompts. | [View Docs](https://magmax.org/python-inquirer/) |
| **Tabulate** | Renders task lists into clean, readable terminal tables. | [View Docs](https://github.com/astanin/python-tabulate) |
| **Python-Dateutil** | Handles flexible date parsing and manipulation. | [View Docs](https://dateutil.readthedocs.io/en/stable/) |


### Installation

To install all dependencies, run:

```bash
uv add inquirer tabulate python-dateutil
```


## Expected Output

When the user runs `python tracker.py`, they should see:

```text
Task Tracker Menu
1. Add Task
2. View Tasks
3. Mark Complete
4. Delete Task
5. Exit

Choose an option: _
```

When viewing tasks, the display looks like:

```text
Your Tasks:
1. Buy groceries [Pending] - Due: 2025-11-08
2. Call dentist [Pending] - Due: 2025-11-07
3. Submit report [Complete] - Done: 2025-11-06
```

When the task list is empty:

```text
Your Tasks:
No tasks yet. Use option 1 to add a task.
```

## Resources

- [Python Official Documentation](https://docs.python.org/) - Language reference
- [Python File I/O Tutorial](https://docs.python.org/3/tutorial/inputoutput.html) - For saving tasks to file

## Visuals 

![Task Tracker main menu showing 5 options: Add Task, View Tasks, Mark Complete, Delete Task, and Exit](/images/tasktracker.jpg)