# Daily Project - 2026-05-18

## Overview

Today's project is a command-line interface (CLI) Task Manager built using Python and SQLite.

The goal of this project was to create a robust, entirely new mini-project from scratch that leverages persistent local storage while remaining lightweight and easy to use from the terminal.

## Features

- **Add:** Create new tasks with a title and an optional description.
- **List:** View all pending tasks, or use the `-a` flag to see all tasks (including completed ones).
- **Complete:** Mark a task as done by its ID.
- **Delete:** Permanently remove a task from the database.

## Usage

You can interact with the Task Manager by running the script with python.

```bash
# Add a task
python3 task_manager.py add "Buy Groceries" -d "Milk, Eggs, Bread"

# List pending tasks
python3 task_manager.py list

# List all tasks
python3 task_manager.py list -a

# Complete a task
python3 task_manager.py complete 1

# Delete a task
python3 task_manager.py delete 1
```

## Running Tests

Unit tests are included to ensure database operations perform as expected.

```bash
python3 -m unittest test_task_manager.py
```
