import os
import json
import argparse

def load_tasks(file_path):
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_tasks(tasks, file_path):
    with open(file_path, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description, file_path):
    tasks = load_tasks(file_path)
    new_id = 1 if not tasks else max(task['id'] for task in tasks) + 1
    new_task = {
        'id': new_id,
        'description': description,
        'completed': False
    }
    tasks.append(new_task)
    save_tasks(tasks, file_path)
    print(f"Task added: '{description}' (ID: {new_id})")
    return new_task

def list_tasks(file_path):
    tasks = load_tasks(file_path)
    if not tasks:
        print("No tasks found.")
        return []
    for task in tasks:
        status = "[x]" if task['completed'] else "[ ]"
        print(f"{task['id']}: {status} {task['description']}")
    return tasks

def complete_task(task_id, file_path):
    tasks = load_tasks(file_path)
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            save_tasks(tasks, file_path)
            print(f"Task {task_id} marked as complete.")
            return True
    print(f"Task {task_id} not found.")
    return False

def delete_task(task_id, file_path):
    tasks = load_tasks(file_path)
    initial_length = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) < initial_length:
        save_tasks(tasks, file_path)
        print(f"Task {task_id} deleted.")
        return True
    print(f"Task {task_id} not found.")
    return False

def main():
    parser = argparse.ArgumentParser(description="CLI To-Do List Manager")
    parser.add_argument('--file', type=str, default='tasks.json', help='Path to the tasks JSON file')

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    subparsers.add_parser('list', help='List all tasks')

    complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
    complete_parser.add_argument('id', type=int, help='ID of the task to complete')

    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='ID of the task to delete')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description, args.file)
    elif args.command == 'list':
        list_tasks(args.file)
    elif args.command == 'complete':
        complete_task(args.id, args.file)
    elif args.command == 'delete':
        delete_task(args.id, args.file)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
