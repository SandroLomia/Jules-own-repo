# Daily Project - 2026-09-10

## Overview

Today's project is a **Markdown Table of Contents (TOC) Generator**.

This utility parses Markdown documents to automatically generate a nested Table of Contents based on the headers (e.g., `# Header`, `## Subheader`). It safely ignores headers that are written inside code blocks to prevent false positives and can inject the generated TOC directly into the document string using a placeholder.

## Features

- Generates GitHub-flavored Markdown compatible slugs for anchor links.
- Creates properly nested lists reflecting the header hierarchy (H1 to H6).
- Safely excludes Markdown headers found inside triple-backtick (`` ``` ``) code blocks.
- Provides an `inject_toc` method to automatically replace a customizable placeholder (`<!-- TOC -->` by default) with the generated Table of Contents.

## Usage

```python
from markdown_toc_generator import MarkdownTOCGenerator

markdown_text = \"\"\"
# Project Title

<!-- TOC -->

## Introduction
Some intro text.

## API Reference
```python
# This comment won't appear in the TOC
def do_something(): pass
```

### Endpoints
List of endpoints.
\"\"\"

# Inject the TOC into the markdown text
updated_markdown = MarkdownTOCGenerator.inject_toc(markdown_text)
print(updated_markdown)
```

## Running Tests

To run the unit tests for this project, execute the following from the repository root:

```bash
PYTHONPATH=project_2026-09-10 python3 -m unittest project_2026-09-10/test_markdown_toc_generator.py
```
