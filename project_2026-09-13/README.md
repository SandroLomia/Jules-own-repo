# Daily Project - 2026-09-13: Cryptographically Secure Password Generator

## Overview

This project provides a simple, cryptographically secure password generator in Python. It utilizes Python's `secrets` module, rather than the standard `random` module, to ensure that the generated passwords are unpredictable and secure enough for cryptographic use.

## Features

- Configurable length (default 16 characters).
- Optional inclusion of uppercase letters, numbers, and special characters.
- Guarantees at least one character of each selected type is included in the final password.
- Employs a cryptographically secure shuffle (`secrets.SystemRandom().shuffle()`) to randomize the character positions.

## Usage

You can use the `generate_password` function directly in your Python code:

```python
from password_generator import generate_password

# Generate a default 16-character password with all character types
print(generate_password())

# Generate a 20-character password without special characters
print(generate_password(length=20, use_special=False))
```

## Running Tests

To run the unit tests, execute the following command from the repository root:

```bash
PYTHONPATH=project_2026-09-13 python3 -m unittest project_2026-09-13/test_password_generator.py
```
