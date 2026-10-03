# Daily Project - 2026-10-03

## Overview

Today's project is a fast duplicate file finder utility written in Python. It efficiently identifies identical files within a given directory tree by first grouping them by file size, and then performing a SHA-256 hash comparison on the files that have the same size.

This two-step process minimizes the number of expensive hashing operations, allowing for quick scanning of large directories.

## Features

- **Fast & Efficient**: Only hashes files that share the exact same byte size.
- **Thorough**: Recursively scans all subdirectories.
- **Accurate**: Uses SHA-256 to guarantee content matches.

## How to Run

You can run the script from the command line, providing the directory you want to scan as an argument:

```bash
python3 duplicate_finder.py /path/to/directory
```

If duplicate files are found, it will group them together and print their paths. If no duplicates are found, it will let you know.

## Running Tests

To run the unit tests, use the following command from the repository root:

```bash
PYTHONPATH=project_2026-10-03 python3 -m unittest project_2026-10-03/test_duplicate_finder.py
```
