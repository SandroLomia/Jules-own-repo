# Daily Project - 2026-06-11

## Overview

This project implements a cryptographically secure password generator in Python. It utilizes the built-in `secrets` module to generate strong, random passwords suitable for security-sensitive applications.

The password generator provides options to:
- Customize password length.
- Include or exclude uppercase letters.
- Include or exclude digits.
- Include or exclude special characters.

## Files

- `password_generator.py`: The main module containing the password generation logic.
- `test_password_generator.py`: Unit tests validating the functionality of the password generator.

## Usage

You can run the script directly to see example outputs:

```bash
python3 password_generator.py
```

Or you can import it into another Python script:

```python
from password_generator import generate_password

# Generate a default 16-character password
password = generate_password()
print(password)

# Generate a 20-character password without special characters
custom_password = generate_password(length=20, use_special=False)
print(custom_password)
```

## Tests

To run the unit tests, ensure you are in the project directory and run:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
