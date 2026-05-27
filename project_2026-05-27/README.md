# Daily Project - 2026-05-27: Secure Password Generator

## Overview

This project implements a cryptographically secure random password generator using Python's built-in `secrets` module.

It provides a function `generate_password()` that allows customization of:
- Password length (minimum 4)
- Inclusion of uppercase letters
- Inclusion of digits
- Inclusion of special characters

The password is guaranteed to contain at least one character of each specified type if the length permits. The function handles parameter combinations appropriately and uses a secure random number generator to shuffle the output, preventing predictable patterns.

## Usage

You can run the script directly to see an example generated password:

```bash
python3 password_generator.py
```

To use it in another project, simply import the function:

```python
from password_generator import generate_password

# Default 12-character password
print(generate_password())

# Custom 20-character alphanumeric password
print(generate_password(length=20, include_special=False))
```

## Testing

Unit tests are included to verify functionality and constraints. You can run them with:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
