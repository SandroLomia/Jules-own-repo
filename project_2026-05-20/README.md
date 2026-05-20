# Daily Project - 2026-05-20

## Overview

Today's project is a command-line interface (CLI) Markdown TODO Extractor built using Python.

The goal of this project was to create a robust, entirely new utility tool from scratch that scans an entire project's markdown files to collect all pending and completed TODO tasks.

## Features

- **Extracts Checkboxes:** Recursively scans directories to parse `- [ ]` and `- [x]` style checkbox items from `.md` files.
- **Grouped Summary Output:** Groups found items cleanly by the file they originated from.
- **JSON Support:** Supports exporting the extracted data as JSON using the `--json` flag for programmatic parsing or piping into other commands.

## Usage

You can interact with the TODO Extractor by running the script with Python.

```bash
# Scan the current directory for markdown TODOs
python3 todo_extractor.py

# Scan a specific directory
python3 todo_extractor.py /path/to/my/notes

# Output as JSON
python3 todo_extractor.py --json
```

## Running Tests

Unit tests are included to ensure correct parsing and that non-markdown files are ignored.

```bash
# Assuming you run from the repo root
PYTHONPATH=project_2026-05-20 python3 -m unittest project_2026-05-20/test_todo_extractor.py
```