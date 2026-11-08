# Secure Password Generator

This module provides a cryptographically secure random password generator in Python. It uses the `secrets` module instead of `random` to ensure that generated passwords are suitable for security-sensitive applications.

## Usage

```python
from password_generator import generate_password

# Generate a default 16-character password (includes lowercase, uppercase, digits, and special characters)
password = generate_password()
print(password)

# Generate a 20-character password
long_password = generate_password(length=20)
print(long_password)

# Generate an 8-character PIN (only digits)
pin = generate_password(length=8, use_uppercase=False, use_digits=True, use_special=False)
# NOTE: The generate_password function forces lowercase characters. A PIN function is best separated.
```

## Running tests

Run tests from the root of the repository:

```bash
PYTHONPATH=project_2026-11-08 python3 -m unittest project_2026-11-08/test_password_generator.py
```
