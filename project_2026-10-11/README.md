# Daily Project - 2026-10-11

## Overview

This project implements a secure, basic Markdown to HTML converter in Python.

The tool converts common markdown syntax to HTML while mitigating Cross-Site Scripting (XSS) vulnerabilities.

### Features

- **XSS Prevention**: Automatically escapes dangerous HTML characters (like `<script>`) to safe HTML entities.
- **Headers**: Supports conversion of `#` tags (H1 through H6) to corresponding HTML tags (`<h1>` - `<h6>`).
- **Bold Text**: Converts `**text**` to `<strong>text</strong>`.
- **Italic Text**: Converts `*text*` to `<em>text</em>`.

### Usage

```python
from markdown_to_html import convert_markdown

# Safe conversion
markdown = "# Hello World\\nThis is **bold** and *italic*."
html_output = convert_markdown(markdown)
print(html_output)

# XSS mitigation
malicious = "<script>alert(1)</script>"
safe_output = convert_markdown(malicious)
print(safe_output)
# Outputs: &lt;script&gt;alert(1)&lt;/script&gt;
```

### Running Tests

To verify the functionality and security constraints, run the unittest suite:

```bash
PYTHONPATH=project_2026-10-11 python3 -m unittest project_2026-10-11/test_markdown_to_html.py
```
