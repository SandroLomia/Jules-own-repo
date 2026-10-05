# Daily Project - 2026-10-05: Markdown to HTML Converter

## Overview
This is a simple Python utility that converts a subset of Markdown text to HTML.

## Features
- Converts Markdown headers (`#` to `######`) to HTML headers (`<h1>` to `<h6>`).
- Converts Markdown paragraphs to HTML `<p>` tags.
- Converts Markdown bold (`**text**`) and italic (`*text*`) to HTML `<strong>` and `<em>` tags.
- Includes XSS prevention by automatically sanitizing input HTML using `html.escape()`.

## Usage
```python
from markdown_converter import convert_to_html

markdown_text = "# Hello World\n\nThis is a **bold** and *italic* paragraph."
html_text = convert_to_html(markdown_text)

print(html_text)
# Output:
# <h1>Hello World</h1>
# <p>This is a <strong>bold</strong> and <em>italic</em> paragraph.</p>
```

## Testing
To run the tests for this project, you can use the built-in `unittest` module:
```bash
PYTHONPATH=project_2026-10-05 python3 -m unittest project_2026-10-05/test_markdown_converter.py
```
