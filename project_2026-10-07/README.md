# Daily Project - 2026-10-07

## Overview

A secure, customizable random password generator implemented in Python.
It uses the cryptographically secure `secrets` module to ensure that generated passwords are safe for use in secure applications.

### Features
* Customizable length (default is 12).
* Toggleable character sets (uppercase, lowercase, digits, symbols).
* Raises appropriate errors for invalid configurations (e.g., zero length or no character sets selected).
* Cryptographically secure.

### How to Run
To run the script and see some example generated passwords:

```bash
python3 password_generator.py
```

### How to use as a module
```python
from password_generator import generate_password

# Default 12 characters, all types
password = generate_password()

# 16 characters, alphanumeric only
alphanumeric = generate_password(length=16, use_symbols=False)

# 6 character pin
pin = generate_password(length=6, use_uppercase=False, use_lowercase=False, use_symbols=False)
```

### Running Tests
To run the unit tests:
```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
