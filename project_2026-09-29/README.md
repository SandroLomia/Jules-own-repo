# Daily Project - 2026-09-29

## Overview

Today's project is a cryptographically secure random password generator built in Python. It is designed to generate passwords that are safe to use for sensitive authentication tokens and secrets, rather than relying on the standard `random` module, which is predictable.

## Features

- Uses Python's `secrets` module (`secrets.choice` and `secrets.SystemRandom().shuffle()`) for true cryptographic randomness.
- Enforces configurable password lengths (minimum 4 characters).
- Allows granular control over character sets (lowercase, uppercase, numbers, symbols).
- Guarantees at least one character of each requested type is present in the final password.

## Usage

```python
from password_generator import generate_secure_password

# Generate a default 16-character complex password
password = generate_secure_password()
print(f"Default: {password}")

# Generate a 24-character alphanumeric password
alphanumeric = generate_secure_password(length=24, include_symbols=False)
print(f"Alphanumeric: {alphanumeric}")
```

## Testing

Run the included unit tests to verify the generator's constraints and randomness properties:

```bash
python3 -m unittest test_password_generator.py
```
