# Daily Project - 2026-09-28: Secure Password Generator

## Overview

A cryptographically secure password generator implemented in Python. It uses the `secrets` module, which provides access to the most secure source of randomness that the operating system provides, rather than the pseudo-random `random` module.

## Features

- Generates passwords with customizable lengths.
- Options to include or exclude:
  - Uppercase letters
  - Numbers
  - Symbols
- Cryptographically secure character selection (`secrets.choice`).
- Cryptographically secure shuffling of the final password (`secrets.SystemRandom().shuffle()`) to ensure no predictable patterns in character placement.

## Usage

```python
from password_generator import PasswordGenerator

generator = PasswordGenerator()

# Generate a default password (length 12, includes upper, numbers, symbols)
password = generator.generate_password()
print(password)

# Generate a 16-character password with only letters and numbers
alphanumeric = generator.generate_password(length=16, use_symbols=False)
print(alphanumeric)
```

## Testing

Run the tests using the `unittest` framework:
```bash
PYTHONPATH=project_2026-09-28 python3 -m unittest project_2026-09-28/test_password_generator.py
```
