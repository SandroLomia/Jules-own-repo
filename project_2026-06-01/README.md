# Daily Project - 2026-06-01

## Overview

Today's project is a cryptographically secure random password generator built in Python.

It generates secure passwords by:
- Using the `secrets` module, which is designed specifically for cryptography and security uses, ensuring randomness is cryptographically strong compared to the standard `random` module.
- Allowing customizable lengths and selectable character sets (lowercase letters, uppercase letters, digits, and special characters).
- Enforcing that at least one character from each selected character set is included in the generated password.
- Providing a command-line interface for ease of use.

## Usage

You can use the password generator from the command line:

```bash
# Generate a default password (length 16, all character sets)
python3 password_generator.py

# Generate a password of length 20
python3 password_generator.py --length 20

# Generate a password excluding special characters and digits
python3 password_generator.py --no-special --no-digits
```

## Running Tests

Unit tests are included to verify functionality, including proper character inclusion and edge-case handling.

Run tests using:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
