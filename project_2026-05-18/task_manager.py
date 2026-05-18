import argparse
import sqlite3
import os

DB_NAME = "tasks.db"

def get_db_connection(db_path=DB_NAME):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(db_path=DB_NAME):
    conn = get_db_connection(db_path)
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
    conn.close()

def add_task(title, description="", db_path=DB_NAME):
    conn = get_db_connection(db_path)
    with conn:
        cursor = conn.execute(
            'INSERT INTO tasks (title, description) VALUES (?, ?)',
            (title, description)
        )
        task_id = cursor.lastrowid
    conn.close()
    print(f"Task '{title}' added with ID {task_id}.")
    return task_id

def list_tasks(all_tasks=False, db_path=DB_NAME):
    conn = get_db_connection(db_path)
    query = 'SELECT * FROM tasks'
    if not all_tasks:
        query += ' WHERE completed = 0'

    cursor = conn.execute(query)
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print("No tasks found.")
        return tasks

    print(f"{'ID':<5} | {'Status':<10} | {'Title':<20} | {'Description'}")
    print("-" * 60)
    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        desc = task["description"] if task["description"] else ""
        print(f"{task['id']:<5} | {status:<10} | {task['title']:<20} | {desc}")
    return tasks

def complete_task(task_id, db_path=DB_NAME):
    conn = get_db_connection(db_path)
    with conn:
        cursor = conn.execute(
            'UPDATE tasks SET completed = 1 WHERE id = ?',
            (task_id,)
        )
        if cursor.rowcount == 0:
            print(f"Task ID {task_id} not found.")
            success = False
        else:
            print(f"Task ID {task_id} marked as complete.")
            success = True
    conn.close()
    return success

def delete_task(task_id, db_path=DB_NAME):
    conn = get_db_connection(db_path)
    with conn:
        cursor = conn.execute(
            'DELETE FROM tasks WHERE id = ?',
            (task_id,)
        )
        if cursor.rowcount == 0:
            print(f"Task ID {task_id} not found.")
            success = False
        else:
            print(f"Task ID {task_id} deleted.")
            success = True
    conn.close()
    return success

def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", type=str, help="Title of the task")
    parser_add.add_argument("-d", "--description", type=str, help="Description of the task", default="")

    # List command
    parser_list = subparsers.add_parser("list", help="List tasks")
    parser_list.add_argument("-a", "--all", action="store_true", help="List all tasks, including completed ones")

    # Complete command
    parser_complete = subparsers.add_parser("complete", help="Mark a task as complete")
    parser_complete.add_argument("id", type=int, help="ID of the task to complete")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    init_db()

    if args.command == "add":
        add_task(args.title, args.description)
    elif args.command == "list":
        list_tasks(args.all)
    elif args.command == "complete":
        complete_task(args.id)
    elif args.command == "delete":
        delete_task(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
