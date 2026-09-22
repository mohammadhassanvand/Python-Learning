import json
from pathlib import Path

FILE_NAME = "tasks.json"

def load_tasks():
    if Path(FILE_NAME).exists():
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{i}. {task['title']} - {status}")

def add_task(tasks):
    title = input("Task title: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

def main():
    tasks = load_tasks()
    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            break

if __name__ == "__main__":
    main()
