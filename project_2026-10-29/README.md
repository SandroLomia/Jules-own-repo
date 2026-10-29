# Daily Project - 2026-10-29

## Overview

Secure Password Generator

This project provides a simple yet effective tool for generating cryptographically secure random passwords in Python.

## Features

* **Cryptographically Secure:** Uses Python's `secrets` module instead of the standard `random` module, ensuring that the generated passwords are unpredictable and suitable for security-sensitive applications.
* **Customizable Length:** You can specify the exact length of the password you need (default is 12 characters).
* **Character Set Control:** You can choose to include or exclude:
  * Uppercase letters (A-Z)
  * Lowercase letters (a-z)
  * Digits (0-9)
  * Special characters (!, @, #, etc.)

## Usage

```python
from password_generator import generate_password

# Generate a default 12-character password
password = generate_password()
print(password)

# Generate a 20-character password with only letters and numbers
password = generate_password(length=20, use_special=False)
print(password)
```

## Running Tests

From the repository root, run:
```bash
PYTHONPATH=project_2026-10-29 python3 -m unittest project_2026-10-29/test_password_generator.py
```
