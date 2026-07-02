# Daily Project - 2026-07-02

## Overview

Today's project is an in-memory **Secure URL Shortener** built in Python.

It provides a lightweight utility class to create mapping between long URLs and shortened 6-character alphanumeric tokens. It guarantees unique mappings and uses the Python `secrets` module for cryptographically secure randomization when generating the short codes, avoiding predictable sequences.

## Features

- Shortens long URLs into unique 6-character random alphanumeric string codes.
- Caches short codes to return identical codes if the same long URL is submitted again.
- Secure token generation using `secrets.choice`.
- Handles expanding valid codes and safely returns `None` for invalid/unknown codes.

## How to Test

Run the included unit tests from the repository root:

```bash
PYTHONPATH=project_2026-07-02 python3 -m unittest project_2026-07-02/test_url_shortener.py
```
