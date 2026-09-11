# Daily Project - 2026-09-11

## Overview

Today's project is a cryptographically secure random password generator implemented in Python. It provides a simple utility to generate strong passwords of customizable length and complexity using the built-in `secrets` module rather than the insecure `random` module.

### Features
* Customizable length (default 16 characters).
* Options to include or exclude:
  * Uppercase letters (`string.ascii_uppercase`)
  * Numbers (`string.digits`)
  * Special characters (`string.punctuation`)
* Uses `secrets.choice()` for secure character selection and `secrets.SystemRandom().shuffle()` for cryptographically secure randomization of the final string.
* Ensures at least one character from each selected complexity pool is present in the final password.

## How to use

```python
from secure_password_generator import generate_password

# Generate a default secure password (length 16, all character types)
pwd = generate_password()
print(pwd)

# Generate a 32-character password without special characters
long_pwd = generate_password(length=32, use_special_chars=False)
print(long_pwd)
```

## Testing

Unit tests are provided using the `unittest` framework to verify correct length, character inclusion constraints, and randomization variation.

Run the tests from the repository root:
```bash
PYTHONPATH=project_2026-09-11 python3 -m unittest project_2026-09-11/test_secure_password_generator.py
```
