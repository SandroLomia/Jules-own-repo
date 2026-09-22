# Daily Project - 2026-09-22

## Overview

Today's project is a cryptographically secure random password generator implemented in Python. It utilizes the `secrets` module, which is preferred for generating secure tokens, passwords, and other security-sensitive data compared to the standard `random` module.

The password generator ensures that:
- It relies on `secrets.SystemRandom` to securely choose characters.
- A cryptographically secure shuffle (`secrets.SystemRandom().shuffle()`) is performed on the generated password array as an added layer of randomization before returning the string.

## Features

- **Customizable Length**: You can define the length of the generated password (default is 16).
- **Character Configuration**: You can include or exclude uppercase letters, numbers, and symbols. (Lowercase letters are always included to ensure at least one character set is available).

## Usage

```python
from password_generator import generate_password

# Default: 16 characters, includes uppercase, numbers, and symbols
print(generate_password())
# Example Output: j!M3L$9bK@1vP#7z

# Custom length: 24 characters
print(generate_password(length=24))

# Only lowercase and numbers:
print(generate_password(use_uppercase=False, use_symbols=False))
```

## Running Tests

To run the unit tests, execute the following from the root of the repository:

```bash
PYTHONPATH=project_2026-09-22 python3 -m unittest project_2026-09-22/test_password_generator.py
```
