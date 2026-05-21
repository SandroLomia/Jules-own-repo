# Daily Project - 2026-05-21: Markdown Table Formatter

## Overview

Today's project is a utility tool called `markdown_table_formatter.py`. It is a command-line script that scans a markdown file, identifies markdown tables within it, and perfectly aligns their columns based on the maximum width of the content in each column.

This tool helps keep markdown documentation clean and readable, especially when editing tables manually causes columns to become misaligned. It also preserves column alignment indicators (like `:---` or `---:`).

## Features

- Scans a Markdown file for tables.
- Automatically adjusts column widths to fit the longest content.
- Preserves table alignment syntax (`:---`, `:---:`, `---:`).
- Gracefully handles rows with missing columns by padding them.
- Can print the formatted markdown to standard output or modify the file in-place.

## Usage

You can run the formatter via the command line:

```bash
# Print formatted markdown to standard output
python3 markdown_table_formatter.py path/to/your/file.md

# Format the file in-place (overwrites the file with the formatted version)
python3 markdown_table_formatter.py path/to/your/file.md -i
```

## Running Tests

Unit tests are provided in `test_markdown_table_formatter.py`. To run them, make sure the `PYTHONPATH` is set to the project directory:

```bash
PYTHONPATH=project_2026-05-21 python3 -m unittest project_2026-05-21/test_markdown_table_formatter.py
```
