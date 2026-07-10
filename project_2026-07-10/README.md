# Daily Project - 2026-07-10

## Overview

Today's project is a **Directory Tree Generator CLI**. It is a Python utility that recursively traverses a specified directory and prints out its structure in a visually appealing, ASCII-art tree format.

This tool is useful for documenting project structures, understanding complex nested directories, and generating visual representations of file systems.

## Features

*   **Customizable Path:** Generates a tree for any given directory path.
*   **Depth Control:** Allows limiting the traversal depth (e.g., only show top-level directories).
*   **Exclusion List:** Provides an option to exclude specific files or directories (like `.git` or `__pycache__`) from the generated tree.
*   **Output Redirection:** Outputs the tree structure to the console by default, but can also write it directly to a file.

## Usage

You can run the CLI using Python:

```bash
python3 cli.py [OPTIONS]
```

### Options

*   `--path`: The path to the directory to generate the tree for. (Default: current directory `.`)
*   `--depth`: The maximum depth to traverse. (Default: unlimited `-1`)
*   `--exclude`: A space-separated list of directories or files to exclude.
*   `--output`: The file to write the tree to. If not provided, it prints to the console.

### Examples

Generate a tree for the current directory:

```bash
python3 cli.py
```

Generate a tree for a specific path, limiting depth to 2 levels:

```bash
python3 cli.py --path /path/to/project --depth 2
```

Generate a tree, excluding the `.git` and `node_modules` directories:

```bash
python3 cli.py --exclude .git node_modules
```

Generate a tree and save it to a file:

```bash
python3 cli.py --output project_structure.txt
```
