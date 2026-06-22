# Daily Project - 2026-06-22

## Overview

Today's project is a secure **Password Generator** utility written in Python.

This utility generates strong, random passwords utilizing Python's built-in `secrets` module, which provides cryptographically secure pseudo-random number generation suitable for managing secrets like passwords, authentication tokens, and related secrets.

## Features

- Configurable password length.
- Options to include or exclude uppercase letters, numbers, and symbols.
- Guarantees at least one character of each requested type is present in the final password.
- Uses `secrets.SystemRandom().shuffle()` for secure character randomization.

## Usage

```python
from password_generator import generate_password

# Default: 12 chars, includes uppercase, numbers, and symbols
print(generate_password())

# Custom length: 16 chars
print(generate_password(length=16))

# Only letters and numbers
print(generate_password(include_symbols=False))
```

## Running Tests

From the repository root, you can run the unit tests with the following command:

```bash
PYTHONPATH=project_2026-06-22 python3 -m unittest project_2026-06-22/test_password_generator.py
```
