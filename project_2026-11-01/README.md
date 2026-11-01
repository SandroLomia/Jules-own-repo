# MarkdownConverter

`MarkdownConverter` is a Python utility that provides a simple and secure way to convert basic Markdown text to HTML.

## Features
- **Headers:** `#` through `######` to `<h1>` through `<h6>`.
- **Bold Text:** `**text**` or `__text__` to `<strong>`.
- **Italic Text:** `*text*` or `_text_` to `<em>`.
- **Paragraphs:** Blocks separated by empty lines are wrapped in `<p>` tags.
- **Security:** All input is sanitized using `html.escape()` to prevent Cross-Site Scripting (XSS) vulnerabilities.

## Usage

```python
from markdown_converter import MarkdownConverter

converter = MarkdownConverter()

markdown_text = """
# Welcome

This is a **bold** statement with some _italic_ words.

<script>alert('XSS')</script>
"""

html_output = converter.convert(markdown_text)
print(html_output)
```

## Running Tests

To run the unit tests, execute the following command from the repository root:

```bash
PYTHONPATH=project_2026-11-01 python3 -m unittest project_2026-11-01/test_markdown_converter.py
```