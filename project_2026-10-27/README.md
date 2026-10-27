# Daily Project - 2026-10-27

## Overview

Today's project is a robust **Markdown Link Checker** utility built in Python.
It helps automate the process of verifying links within Markdown files.

### Features
* Extracts all markdown links matching the `[text](url)` syntax.
* Validates external URLs via HTTP HEAD requests to ensure they are reachable (handling redirects and common connection issues).
* Validates internal relative file paths to ensure local files actually exist.
* Properly handles fragment/anchor links (e.g. `file.md#section`).

### Usage

```python
from markdown_link_checker import check_markdown_links

with open("my_document.md", "r") as f:
    content = f.read()

# Checks links and uses the current directory as the base for internal paths
results = check_markdown_links(content, base_dir=".")

print("Valid links:", results['valid'])
print("Broken links:", results['invalid'])
```

### Testing

Tests can be run from the root of the repository:

```bash
PYTHONPATH=project_2026-10-27 python3 -m unittest project_2026-10-27/test_markdown_link_checker.py
```
