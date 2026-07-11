# URL Encode/Decode CLI Tool

## Overview

This is a simple command-line interface (CLI) tool written in Python to URL-encode and URL-decode strings.

As a developer, I frequently need to escape or unescape URLs, query parameters, or other web-related strings. This lightweight utility makes it quick and easy to perform these conversions directly from the terminal without relying on external online tools or opening a REPL.

It uses Python's built-in `urllib.parse` module to ensure reliable, standard-compliant encoding and decoding.

## Features

- **Encode**: Converts special characters in a string into their percent-encoded equivalents (e.g., spaces become `%20`, `&` becomes `%26`).
- **Decode**: Reverts percent-encoded strings back to their original form.
- **Robustness**: Includes comprehensive unit tests covering alphanumeric strings, strings with spaces, special characters, and empty strings.

## Usage

You can run the tool from the command line using python:

```bash
# Encode a string
python3 url_tool.py --encode "Hello World & Friends"
# Output: Hello%20World%20%26%20Friends

# Decode a string
python3 url_tool.py --decode "Hello%20World%20%26%20Friends"
# Output: Hello World & Friends
```

## Running Tests

Unit tests are included. To run them, execute the following from the root of the repository:

```bash
PYTHONPATH=project_2026-07-11 python3 -m unittest project_2026-07-11/test_url_tool.py
```
