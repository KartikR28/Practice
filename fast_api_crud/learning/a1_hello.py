tasks = [
    {"id": 1, "title": "Learn venv", "done": True},
    {"id": 2, "title": "Learn functions", "done": False},
    {"id": 3, "title": "Learn classes", "done": True},
]

pending_tasks = [task["title"] for task in tasks if not task["done"]]

print(pending_tasks)

task_dict = {task["id"]: task["title"] for task in tasks}

print(task_dict)

print(f"Pending taska are {len(pending_tasks)} of { len(task_dict) } tasks left")

