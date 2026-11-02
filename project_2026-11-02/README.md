# Daily Project - 2026-11-02

## Overview

Today's project is a **Markdown Table Generator** utility written in Python. It takes a 2D array (list of lists) of strings and formats it into a neatly aligned Markdown table.

### Features
- Properly aligns columns based on the maximum width of data in each column.
- Handles uneven row lengths gracefully.
- Ensures a minimum column width for visually pleasing Markdown separators.
- Returns an empty string for empty input data.

### Usage

```python
from markdown_table_generator import MarkdownTableGenerator

data = [
    ["Name", "Age", "City"],
    ["Alice", "30", "New York"],
    ["Bob", "25", "San Francisco"]
]

generator = MarkdownTableGenerator(data)
markdown_table = generator.generate()
print(markdown_table)
```

### Output

```markdown
| Name  | Age | City          |
|-------|-----|---------------|
| Alice | 30  | New York      |
| Bob   | 25  | San Francisco |
```
