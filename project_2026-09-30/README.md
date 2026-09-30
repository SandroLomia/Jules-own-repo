# Project 2026-09-30

This project contains a lightweight Markdown to HTML converter utility.

## md_to_html.py

The `md_to_html.py` script provides a `convert_markdown_to_html(markdown_text)` function that converts basic Markdown syntax to HTML.

### Supported Features:
* Headers (`#` to `######`)
* Bold text (`**text**`)
* Italic text (`*text*` or `_text_`)
* Unordered lists (`* item`)
* Paragraphs

### Usage Example:
```python
from md_to_html import convert_markdown_to_html

markdown_input = """
# Welcome

This is **bold** and this is *italic*.

* Item 1
* Item 2
"""

html_output = convert_markdown_to_html(markdown_input)
print(html_output)
```

## Running Tests
To run the unit tests for the converter, run the following from the root directory:
```bash
PYTHONPATH=project_2026-09-30 python3 -m unittest project_2026-09-30/test_md_to_html.py
```
