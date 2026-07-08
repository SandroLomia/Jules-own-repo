# Daily Project - 2026-07-08

## Overview

Today's project is a command-line interface (CLI) To-Do List Manager written in Python. It allows users to quickly manage a list of tasks directly from the terminal, providing a simple and efficient way to track daily activities.

## Features

- **Add tasks**: Create new to-do items.
- **List tasks**: View all tasks with their current completion status.
- **Complete tasks**: Mark specific tasks as completed.
- **Delete tasks**: Remove tasks from the list entirely.
- **Persistent storage**: Tasks are saved to a local JSON file (`tasks.json` by default), ensuring data is kept between sessions.

## How to use

Run the script using Python:

```bash
# Add a task
python3 todo_manager.py add "Buy groceries"

# List all tasks
python3 todo_manager.py list

# Mark a task as complete (using its ID)
python3 todo_manager.py complete 1

# Delete a task (using its ID)
python3 todo_manager.py delete 1
```

You can specify a custom JSON file using the `--file` argument:

```bash
python3 todo_manager.py --file my_tasks.json add "Read a book"
```
