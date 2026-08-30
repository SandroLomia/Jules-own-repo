# Daily Project - 2026-08-30

## Overview

Today's project is a **Markdown Table of Contents (TOC) Generator**. It parses Markdown text, extracts headings (levels 2-6 by default), and generates a TOC with appropriate indentation and anchor links. It also correctly ignores any markdown headings that appear inside code blocks.

## How to use

Run the script from the command line, passing the markdown file you want to parse:

```bash
python3 toc_generator.py <markdown_file>
```

This will output the generated TOC to `stdout`.

## Testing

Run the included unit tests to verify the script handles typical headings, ignores code blocks, and correctly handles special characters in anchor links:

```bash
python3 -m unittest test_toc_generator.py
```
