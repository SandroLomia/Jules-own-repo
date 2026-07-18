# Daily Project - 2026-07-18

## Overview

Today's project is a utility script that easily converts formatted data (CSV or Python dictionaries) into well-structured Markdown tables. This is especially useful for programmatic documentation generation and rendering raw data for reports.

## Files

- `markdown_table_generator.py`: Contains the `MarkdownTableGenerator` class with two primary methods:
    - `generate_from_csv(csv_string)`: Parses a string of CSV formatted text into a Markdown table.
    - `generate_from_dicts(data)`: Parses a list of dictionary objects into a Markdown table, using keys from the first dictionary as the column headers.

- `test_markdown_table_generator.py`: Unit tests validating empty states, missing keys/columns, and correct parsing logic.

## Usage

```python
from markdown_table_generator import MarkdownTableGenerator

# From CSV
csv_data = "Name,Age,City\\nAlice,30,New York\\nBob,25,Los Angeles"
md_table_csv = MarkdownTableGenerator.generate_from_csv(csv_data)
print(md_table_csv)

# From Dictionaries
dict_data = [
    {"Task": "Write Code", "Status": "Done"},
    {"Task": "Write Tests", "Status": "In Progress"}
]
md_table_dict = MarkdownTableGenerator.generate_from_dicts(dict_data)
print(md_table_dict)
```
