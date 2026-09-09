# Daily Project - 2026-09-09

## Overview

Today's project is a cryptographically secure Password Generator utility.

Generating random values for security-sensitive applications (like passwords, tokens, or cryptographic keys) should never rely on the standard `random` module, as it is predictable. This utility utilizes Python's built-in `secrets` module, providing access to the most secure source of randomness available on the operating system.

## Features

- Generates passwords using a combination of uppercase letters, lowercase letters, digits, and special characters.
- Highly customizable: Choose the exact length and toggle which character types to include.
- Uses `secrets.choice()` for random selection and `secrets.SystemRandom().shuffle()` for cryptographically secure shuffling of the generated characters.
- Ensures at least one character from each selected pool is included in the final password.

## Usage

```python
from password_generator import PasswordGenerator

# Generate a default 12-character password with all character types
password = PasswordGenerator.generate_password()
print(f"Default Password: {password}")

# Generate a 16-character alphanumeric password
alphanumeric = PasswordGenerator.generate_password(length=16, use_special=False)
print(f"Alphanumeric: {alphanumeric}")

# Generate an 8-character PIN
pin = PasswordGenerator.generate_password(length=8, use_upper=False, use_lower=False, use_special=False)
print(f"PIN: {pin}")
```

## Running Tests

To run the unit tests for this project, execute the following from the repository root:

```bash
PYTHONPATH=project_2026-09-09 python3 -m unittest project_2026-09-09/test_password_generator.py
```
