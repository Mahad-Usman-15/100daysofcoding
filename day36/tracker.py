import inquirer
from tabulate import tabulate
from dateutil import parser as date_parser
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"


def load_tasks():
    """Load tasks from JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    """Add a new task with title, description, due date, and priority."""
    questions = [
        inquirer.Text("title", message="Enter task title (max 100 characters)", validate=lambda _, x: 0 < len(x) <= 100),
        inquirer.Text("description", message="Enter description (optional)", validate=lambda _, x: True),
        inquirer.Text("due_date", message="Enter due date (e.g., 2025-12-31 or leave empty)", validate=lambda _, x: True),
        inquirer.List("priority", message="Select priority", choices=["High", "Medium", "Low"]),
    ]

    answers = inquirer.prompt(questions)
    if not answers:
        return

    task = {
        "title": answers["title"].strip(),
        "description": answers["description"].strip(),
        "priority": answers["priority"].lower(),
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "completed_at": None,
        "due_date": None,
    }

    if answers["due_date"].strip():
        try:
            due_date = date_parser.parse(answers["due_date"].strip())
            task["due_date"] = due_date.strftime("%Y-%m-%d")
        except (ValueError, OverflowError):
            print("Invalid date format. Due date will be empty.")

    tasks.append(task)
    save_tasks(tasks)
    print(f"\nTask '{task['title']}' added successfully!")


def view_tasks(tasks):
    """Display tasks with optional filtering."""
    if not tasks:
        print("\nYour Tasks:")
        print("No tasks yet. Use option 1 to add a task.")
        return

    questions = [
        inquirer.List("filter", message="Filter tasks by", choices=["All", "Pending", "Completed", "High Priority", "Medium Priority", "Low Priority"]),
    ]

    answers = inquirer.prompt(questions)
    if not answers:
        return

    filter_type = answers["filter"]

    if filter_type == "Pending":
        filtered = [t for t in tasks if t["status"] == "pending"]
    elif filter_type == "Completed":
        filtered = [t for t in tasks if t["status"] == "completed"]
    elif filter_type == "High Priority":
        filtered = [t for t in tasks if t["priority"] == "high"]
    elif filter_type == "Medium Priority":
        filtered = [t for t in tasks if t["priority"] == "medium"]
    elif filter_type == "Low Priority":
        filtered = [t for t in tasks if t["priority"] == "low"]
    else:
        filtered = tasks

    if not filtered:
        print(f"\nNo tasks found for filter: {filter_type}")
        return

    table_data = []
    for i, task in enumerate(filtered, 1):
        status = task["status"].capitalize()
        due = task["due_date"] if task["due_date"] else "N/A"
        if task["status"] == "completed" and task["completed_at"]:
            done_date = task["completed_at"][:10]
            table_data.append([i, task["title"], status, task["priority"].capitalize(), due, done_date])
        else:
            table_data.append([i, task["title"], status, task["priority"].capitalize(), due, ""])

    headers = ["#", "Title", "Status", "Priority", "Due Date", "Completed At"]
    print("\n" + tabulate(table_data, headers=headers, tablefmt="grid"))


def mark_complete(tasks):
    """Mark a task as completed."""
    pending_tasks = [t for t in tasks if t["status"] == "pending"]

    if not pending_tasks:
        print("\nNo pending tasks to mark as complete!")
        return

    task_choices = [(f"{t['title']} (Due: {t['due_date'] or 'N/A'})", i) for i, t in enumerate(pending_tasks)]

    questions = [
        inquirer.List("task", message="Select task to mark as complete", choices=task_choices),
    ]

    answers = inquirer.prompt(questions)
    if not answers:
        return

    task_index = answers["task"]
    pending_tasks[task_index]["status"] = "completed"
    pending_tasks[task_index]["completed_at"] = datetime.now().isoformat()

    save_tasks(tasks)
    print(f"\nTask '{pending_tasks[task_index]['title']}' marked as complete!")


def delete_task(tasks):
    """Delete a task permanently with confirmation."""
    if not tasks:
        print("\nNo tasks to delete!")
        return

    task_choices = [(f"{t['title']} [{t['status'].capitalize()}]", i) for i, t in enumerate(tasks)]

    questions = [
        inquirer.List("task", message="Select task to delete", choices=task_choices),
        inquirer.Confirm("confirm", message="Are you sure you want to delete this task?"),
    ]

    answers = inquirer.prompt(questions)
    if not answers or not answers["confirm"]:
        print("Deletion cancelled.")
        return

    task_title = tasks[answers["task"]]["title"]
    tasks.pop(answers["task"])
    save_tasks(tasks)
    print(f"\nTask '{task_title}' deleted successfully!")


def main():
    """Main menu loop for the Task Tracker."""
    tasks = load_tasks()

    while True:
        print("\n" + "=" * 40)
        print("Task Tracker Menu")
        print("=" * 40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Complete")
        print("4. Delete Task")
        print("5. Exit")

        questions = [
            inquirer.List("option", message="Choose an option", choices=["1. Add Task", "2. View Tasks", "3. Mark Complete", "4. Delete Task", "5. Exit"]),
        ]

        answers = inquirer.prompt(questions)
        if not answers:
            continue

        choice = answers["option"]

        if choice == "1. Add Task":
            add_task(tasks)
        elif choice == "2. View Tasks":
            view_tasks(tasks)
        elif choice == "3. Mark Complete":
            mark_complete(tasks)
        elif choice == "4. Delete Task":
            delete_task(tasks)
        elif choice == "5. Exit":
            print("\nGoodbye! Keep tracking your tasks!")
            break


if __name__ == "__main__":
    main()
