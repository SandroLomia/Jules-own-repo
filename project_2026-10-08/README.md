# Daily Project - 2026-10-08

## Overview

Today I created `dir_stats.py`, a simple Python utility that analyzes a directory and provides statistics about disk usage based on file extensions. It recursively scans a given directory and sums up the total byte size of files, grouping them by their extensions.

This is useful for quickly identifying which types of files are consuming the most space within a repository or project.

## How it works

The utility uses Python's standard `os` module (specifically `os.walk` and `os.path.getsize`) to traverse the directory tree. It normalizes extensions to lowercase, ignores symlinks to prevent circular scanning, and handles missing file permissions gracefully.

## Usage

You can run the script directly from the command line, providing a directory path as an argument. If no path is provided, it defaults to the current directory (`.`).

```bash
# Analyze the current directory
python3 dir_stats.py

# Analyze a specific directory
python3 dir_stats.py /path/to/some/directory
```

### Example Output

```
Directory Statistics for: .
----------------------------------------
.pack          :   12.50 MB
.idx           :  240.12 KB
.py            :   15.40 KB
.md            :    2.10 KB
<no extension> :  512 bytes
```

## Tests

The project includes a unit test suite to verify the size calculation logic:

```bash
PYTHONPATH=project_2026-10-08 python3 -m unittest project_2026-10-08/test_dir_stats.py
```