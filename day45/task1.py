from fastapi import FastAPI

from fastapi import FastAPI

tasks = [
    {
        "id": 1,
        "title": "Make website",
        "description": "To create an ecommerce website",
        "status": "completed"
    },
    {
        "id": 2,
        "title": "Fix API Dictionary Access",
        "description": "Update get_product_by_name to access the 'products' key in the JSON response",
        "status": "completed"
    },
    {
        "id": 3,
        "title": "Resolve Environment Issues",
        "description": "Fix ModuleNotFoundError by syncing Python interpreter with pip packages",
        "status": "completed"
    },
    {
        "id": 4,
        "title": "Implement Inventory Logic",
        "description": "Create a function to calculate total stock value (Price * Stock)",
        "status": "pending"
    },
    {
        "id": 5,
        "title": "Search Filter by Status",
        "description": "Build a tool to return only products that are 'in-stock' or 'completed'",
        "status": "pending"
    }
]
app = FastAPI(
    title="Task API",
    description="A simple task management API"
)







@app.get("/")
def read_root():
    return {"message": "Task API is running"}

@app.get("/tasks")
def get_tasks(status:str="all"):
    global tasks
    if status == "all":
        return tasks
    status_tasks=[task for task in tasks if task["status"].lower() == status.lower()]
    return status_tasks

       
