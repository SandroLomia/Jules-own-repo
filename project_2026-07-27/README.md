# Daily Project - 2026-07-27

## Overview

Today's project is a Python utility to convert between JSON-like lists of dictionaries and Markdown tables.
It provides a robust way to generate tabular data in Markdown format from structured data, and to parse Markdown tables back into structured Python data.

### Features
* `json_to_markdown_table(data: list[dict]) -> str`: Generates a Markdown table string from a list of dictionaries.
* `markdown_table_to_json(markdown_table: str) -> list[dict]`: Parses a Markdown table string back into a list of dictionaries, with basic type coercion for booleans, integers, and floats.
* Handles escaped pipe characters (`\|`) within table cell values.

## Usage

```python
from markdown_table import json_to_markdown_table, markdown_table_to_json

data = [
    {"name": "Alice", "role": "Engineer", "active": True},
    {"name": "Bob", "role": "Designer", "active": False}
]

# Generate Markdown Table
markdown_str = json_to_markdown_table(data)
print(markdown_str)
# Output:
# | name | role | active |
# | --- | --- | --- |
# | Alice | Engineer | True |
# | Bob | Designer | False |

# Parse back to JSON
parsed_data = markdown_table_to_json(markdown_str)
print(parsed_data)
# Output:
# [{'name': 'Alice', 'role': 'Engineer', 'active': True}, {'name': 'Bob', 'role': 'Designer', 'active': False}]
```

## Running Tests

Unit tests are included to ensure correct handling of edge cases, empty datasets, and data round-tripping.

Run the tests from the root directory of the repository with:
```bash
PYTHONPATH=project_2026-07-27 python3 -m unittest project_2026-07-27/test_markdown_table.py
```