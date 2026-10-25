# Daily Project - 2026-10-25

## Overview

Today's project is a Secure Password Generator built in Python.

It provides a `generate_password` function that utilizes the cryptographically secure `secrets` module (rather than the standard `random` module) to generate random passwords.

## Features

- Generates passwords of customizable length (default: 12).
- Options to include or exclude uppercase letters, lowercase letters, numbers, and symbols.
- Guarantees at least one character from each selected character type (if length permits).
- Cryptographically secure randomness for reliable security.

## Usage

```python
from password_generator import generate_password

# Default password (12 characters, all types included)
print(generate_password())

# Custom password (16 characters, letters and numbers only)
print(generate_password(length=16, use_symbols=False))
```

## Testing

Run the unit tests from the repository root:

```bash
PYTHONPATH=project_2026-10-25 python3 -m unittest project_2026-10-25/test_password_generator.py
```
