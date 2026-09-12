# Daily Project - 2026-09-12

## Overview

This project implements a Secure Password Generator in Python. The generator creates passwords of a customizable length, built from a selectable pool of character types (uppercase, lowercase, digits, and special characters).

Importantly, it uses the Python `secrets` module instead of the standard `random` module, ensuring that the generated passwords are cryptographically secure.

## Features

- **Customizable Length**: Generate a password of any length (must be large enough to include selected character types).
- **Selectable Character Types**: Toggle the inclusion of uppercase, lowercase, digits, and punctuation characters.
- **Cryptographically Secure**: Utilizes `secrets.choice` and `secrets.SystemRandom().shuffle()` to pick and shuffle characters securely.

## Example Usage

```python
from password_generator import generate_password

# Generate a 16-character secure password using all default character types
secure_pass = generate_password(16)
print(f"Generated Password: {secure_pass}")

# Generate a 12-character secure password using only uppercase, lowercase, and digits
alphanumeric_pass = generate_password(12, use_special=False)
print(f"Alphanumeric Password: {alphanumeric_pass}")
```

## Running Tests

From the repository root, you can run the unit tests as follows:
```bash
PYTHONPATH=project_2026-09-12 python3 -m unittest project_2026-09-12/test_password_generator.py
```
