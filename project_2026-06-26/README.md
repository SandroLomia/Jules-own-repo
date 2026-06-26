# Daily Project - 2026-06-26

## Overview

Today's project is **TaskMaster**, a simple yet effective Command Line Interface (CLI) task management utility written in Python. It allows users to easily add, list, complete, and delete tasks directly from their terminal.

This project was built to explore lightweight data persistence using JSON files and CLI argument parsing using the standard `argparse` library. It includes full unit test coverage using Python's `unittest` framework.

## Features

- **Add tasks:** Create new tasks with a description.
- **List tasks:** View all tasks along with their current completion status.
- **Complete tasks:** Mark existing tasks as completed.
- **Delete tasks:** Remove tasks entirely from the list.
- **Data Persistence:** Tasks are stored locally in a `tasks.json` file.

## Usage

You can interact with TaskMaster using the following commands:

```bash
# Add a new task
python3 taskmaster.py add "Buy groceries"
python3 taskmaster.py add "Finish the report"

# List all tasks
python3 taskmaster.py list

# Mark a task as completed (using its ID)
python3 taskmaster.py complete 1

# Delete a task (using its ID)
python3 taskmaster.py delete 2
```

## Running Tests

To run the unit tests for TaskMaster, execute the following command from the root of the repository:

```bash
PYTHONPATH=project_2026-06-26 python3 -m unittest project_2026-06-26/test_taskmaster.py
```
