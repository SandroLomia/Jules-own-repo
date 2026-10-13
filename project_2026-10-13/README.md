# Daily Project - 2026-10-13

## Overview

This project implements a cryptographically secure random password generator in Python. It uses the `secrets` module, which is designed for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

## Features

*   **Cryptographically Secure:** Uses `secrets.choice()` and `secrets.SystemRandom().shuffle()` to ensure unpredictability and security.
*   **Customizable Length:** Allows you to specify the exact length of the generated password.
*   **Configurable Character Classes:** You can toggle the inclusion of uppercase letters, numbers, and special characters.
*   **Guaranteed Character Inclusion:** Ensures that at least one character from each selected class is included in the final password.

## Usage

You can import and use the `generate_password` function in your scripts:

```python
from password_generator import generate_password

# Generate a default 12-character password (includes all character types)
password = generate_password()
print(f"Default Password: {password}")

# Generate a 20-character password without special characters
password_no_special = generate_password(length=20, use_special=False)
print(f"Alphanumeric Password: {password_no_special}")

# Generate an 8-character numeric PIN (only lowercase and numbers allowed, but we turn off lowercase)
pin = generate_password(length=8, use_uppercase=False, use_special=False)
print(f"Alphanumeric lowercase PIN: {pin}")
```

## Testing

To run the unit tests, use the following command from the root of the repository:

```bash
PYTHONPATH=project_2026-10-13 python3 -m unittest project_2026-10-13/test_password_generator.py
```
