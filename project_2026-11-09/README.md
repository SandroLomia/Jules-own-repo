# Daily Project - 2026-11-09: Secure Password Generator

## Overview

Today's project is a robust and cryptographically secure password generator utility in Python.

### Features
* **Cryptographically Secure:** Utilizes Python's `secrets` module instead of `random` to ensure unpredictable selection and secure shuffling of characters.
* **Customizable Length:** Generates passwords of any requested length (minimum 4).
* **Configurable Character Sets:** Allows the user to toggle uppercase letters, numbers, and special characters on or off depending on password requirements.
* **Guaranteed Inclusion:** Ensures that if a character set is selected, at least one character from that set is guaranteed to be present in the final password.

### Usage
```python
from password_generator import generate_password

# Default: 12 chars, includes uppercase, numbers, and specials
print(generate_password())

# Custom length
print(generate_password(length=16))

# Alphanumeric only
print(generate_password(use_special=False))
```

### Testing
Run the unit tests from the repository root:
```bash
PYTHONPATH=project_2026-11-09 python3 -m unittest project_2026-11-09/test_password_generator.py
```
