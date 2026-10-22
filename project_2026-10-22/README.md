# Daily Project - 2026-10-22

## Overview

Today's project is a **Markdown to HTML Converter** script written in Python. It provides a straightforward function to convert basic Markdown syntax into valid HTML, while also ensuring robust XSS (Cross-Site Scripting) protection by escaping HTML entities in the input.

### Features
*   **Header Support:** Converts `#` through `######` into `<h1>` to `<h6>` tags.
*   **Text Formatting:** Supports bold text (`**` or `__`) and italic text (`*` or `_`).
*   **Paragraph Wrapping:** Automatically wraps basic text lines in `<p>` tags.
*   **XSS Sanitization:** Uses `html.escape()` on all input text before parsing markdown, ensuring that any malicious `<script>` or HTML tags are safely encoded.

### Files
*   `markdown_converter.py`: Contains the `convert_to_html` function which implements the parsing and conversion logic.
*   `test_markdown_converter.py`: Comprehensive test suite verifying the conversion rules and XSS sanitization using `unittest`.

### How to use

```python
from markdown_converter import convert_to_html

markdown_text = "# Hello World\nThis is a **bold** statement."
html_output = convert_to_html(markdown_text)
print(html_output)
# Output:
# <h1>Hello World</h1>
# <p>This is a <b>bold</b> statement.</p>
```

### Running Tests

To run the test suite, use the following command from the root of the repository:

```bash
PYTHONPATH=project_2026-10-22 python3 -m unittest project_2026-10-22/test_markdown_converter.py
```
