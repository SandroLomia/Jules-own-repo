# Daily Project - 2026-06-04

## Overview

Today's project is a cryptographically secure random password generator built in Python.

It leverages the built-in `secrets` module instead of `random` to ensure that the generated values are secure and not predictable.

### Features

- Configurable length (minimum 4 characters)
- Options to include/exclude uppercase letters
- Options to include/exclude digits
- Options to include/exclude punctuation symbols
- Guarantees at least one character of each selected type is included
- Comprehensive unit tests included

### Usage

```python
from password_generator import generate_password

# Generate a default 12-character password
password = generate_password()
print(password)

# Generate a 20-character password without symbols
password = generate_password(length=20, use_symbols=False)
print(password)
```

### Testing

Run the included unit tests using:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
