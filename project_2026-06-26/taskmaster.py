import argparse
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks(file_path=TASKS_FILE):
    if not os.path.exists(file_path):
        return []
    with open(file_path, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks, file_path=TASKS_FILE):
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description, file_path=TASKS_FILE):
    tasks = load_tasks(file_path)
    task_id = 1 if not tasks else max(t['id'] for t in tasks) + 1
    tasks.append({
        'id': task_id,
        'description': description,
        'completed': False
    })
    save_tasks(tasks, file_path)
    print(f"Added task: '{description}' (ID: {task_id})")
    return task_id

def list_tasks(file_path=TASKS_FILE):
    tasks = load_tasks(file_path)
    if not tasks:
        print("No tasks found.")
        return tasks
    print(f"{'ID':<5} | {'Status':<10} | {'Description'}")
    print("-" * 40)
    for task in tasks:
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{task['id']:<5} | {status:<10} | {task['description']}")
    return tasks

def complete_task(task_id, file_path=TASKS_FILE):
    tasks = load_tasks(file_path)
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks, file_path)
            print(f"Marked task {task_id} as completed.")
            return True
    print(f"Task {task_id} not found.")
    return False

def delete_task(task_id, file_path=TASKS_FILE):
    tasks = load_tasks(file_path)
    filtered_tasks = [t for t in tasks if t['id'] != task_id]
    if len(tasks) == len(filtered_tasks):
        print(f"Task {task_id} not found.")
        return False
    save_tasks(filtered_tasks, file_path)
    print(f"Deleted task {task_id}.")
    return True

def main():
    parser = argparse.ArgumentParser(description="TaskMaster CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add task command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Description of the task")

    # List tasks command
    subparsers.add_parser("list", help="List all tasks")

    # Complete task command
    parser_complete = subparsers.add_parser("complete", help="Mark a task as completed")
    parser_complete.add_argument("id", type=int, help="ID of the task to complete")

    # Delete task command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.description)
    elif args.command == "list":
        list_tasks()
    elif args.command == "complete":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
