# Daily Project - 2026-05-19

## Overview

Today's project is a command-line interface (CLI) Directory Tree Generator built using Python.

The goal of this project was to create a useful visualization tool from scratch that helps users quickly understand the directory structure of their projects. It provides a visual representation of files and folders in a tree-like format, similar to the Unix `tree` command.

## Features

- **Visual Tree Generation:** Recursively generates a clean, readable tree structure of any given directory.
- **Max Depth Limit:** Optionally pass the `-d` or `--depth` argument to limit how deep the recursion should go.
- **Ignore Directories:** Automatically ignores hidden files/directories by default, and allows users to pass an ignore list (`-i` or `--ignore`) to skip directories like `node_modules`, `venv`, `__pycache__`, or `.git`.
- **Directory Sorting:** Sorts output so that directories appear first, followed by files, mimicking a clean IDE file explorer.

## Usage

You can run the script with python.

```bash
# Generate tree for the current directory
python3 tree_gen.py

# Generate tree for a specific path
python3 tree_gen.py /path/to/directory

# Generate tree up to a depth of 1 (current dir + immediate children)
python3 tree_gen.py /path/to/directory -d 1

# Ignore specific directories
python3 tree_gen.py /path/to/directory -i dir1 dir2
```

## Running Tests

Unit tests are included to ensure tree generation, max depth limiting, and directory ignoring work as expected.

```bash
python3 -m unittest test_tree_gen.py
```