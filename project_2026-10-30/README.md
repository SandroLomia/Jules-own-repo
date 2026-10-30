# Daily Project - 2026-10-30

## Overview

Today's project is a cryptographically secure **Password Generator** utility. It leverages Python's built-in `secrets` module to generate strong, random passwords.

## Features

- Generates passwords with customizable length.
- Options to include or exclude uppercase letters, numbers, and symbols.
- Uses `secrets.SystemRandom().shuffle()` for cryptographically secure randomization.
- Ensures at least one character of each selected type is included in the generated password.

## Usage

```python
from password_generator import generate_password

# Generate a default password (12 characters, all types included)
print(generate_password())

# Generate a custom password
print(generate_password(length=16, use_symbols=False))
```

## Testing

Run the tests using the built-in `unittest` module:

```bash
PYTHONPATH=project_2026-10-30 python3 -m unittest project_2026-10-30/test_password_generator.py
```
