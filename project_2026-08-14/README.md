# Daily Project - 2026-08-14

## Overview

Today I built a secure **Password Generator** in Python. It's a useful utility script relying on cryptographically secure methods (`secrets` module instead of `random`).

It allows generating passwords of customizable length, and allows specifying whether to include uppercase letters, numbers, and special characters.

## Files

*   `password_generator.py`: Contains the `generate_password` function.
*   `test_password_generator.py`: Contains the unit tests for the password generator.

## How to run the code

You can use the function in your Python code:

```python
from password_generator import generate_password

# Default: 16 chars, with uppercase, numbers, and special chars
password = generate_password()
print(password)

# Custom length, letters only
password = generate_password(length=12, use_numbers=False, use_special=False)
print(password)
```

## How to run tests

From the root of the repository, run the following command:

```bash
PYTHONPATH=project_2026-08-14 python3 -m unittest project_2026-08-14/test_password_generator.py
```
