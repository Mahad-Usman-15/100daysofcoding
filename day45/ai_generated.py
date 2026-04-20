from enum import Enum
# Enums is a collection of constants
class TaskStatus(str, Enum):
    COMPLETED = "completed"
    PENDING = "pending"
    ALL = "all"

@app.get("/tasks")
def get_tasks(status: TaskStatus = TaskStatus.ALL):
    if status == TaskStatus.ALL:
        return tasks
    return [t for t in tasks if t["status"] == status.value]

