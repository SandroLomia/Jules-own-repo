# Daily Project - 2026-08-15: Secure Password Generator

## Overview

Today's project is a robust, cryptographically secure password generator utility built in Python.

Unlike generators that rely on the standard `random` module (which is pseudo-random and unsuitable for security purposes), this utility utilizes Python's built-in `secrets` module. This ensures that the generated passwords are unpredictable and safe for use as account passwords, API tokens, and other security-sensitive applications.

## Features

- **Cryptographically Secure:** Uses `secrets.choice()` for random selection and `secrets.SystemRandom().shuffle()` for secure list shuffling.
- **Customizable Length:** Generate passwords of any length (default is 12).
- **Customizable Complexity:** Toggle the inclusion of uppercase letters, numbers, and special symbols to meet varying password policies.
- **Guaranteed Inclusion:** Ensures that at least one character from each selected category (lowercase, uppercase, numbers, symbols) is present in the output, provided the requested length is sufficient.

## Usage

```python
from secure_password_generator import generate_password

# Generate a default 12-character password with all character types
password = generate_password()
print(f"Default Password: {password}")

# Generate a 20-character alphanumeric password (no symbols)
alpha_num_password = generate_password(length=20, use_symbols=False)
print(f"Alphanumeric Password: {alpha_num_password}")

# Generate a 16-character lowercase only password
lowercase_password = generate_password(length=16, use_uppercase=False, use_numbers=False, use_symbols=False)
print(f"Lowercase Password: {lowercase_password}")
```

## Running Tests

To run the unit tests for this utility from the repository root:

```bash
PYTHONPATH=project_2026-08-15 python3 -m unittest project_2026-08-15/test_secure_password_generator.py
```
