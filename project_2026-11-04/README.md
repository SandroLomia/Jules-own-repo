# Daily Project - 2026-11-04

## Overview

Today's project is a cryptographically secure random password generator implemented in Python. It utilizes the built-in `secrets` module to ensure high entropy suitable for generating passwords or tokens.

## Features

- **Secure Generation**: Uses `secrets.choice` and `secrets.SystemRandom().shuffle()` for cryptographically strong randomness.
- **Customizable**: Control the password length and character sets included (uppercase, lowercase, digits, special characters).
- **Guaranteed Inclusion**: Ensures that at least one character from each selected character set is present in the final password.

## Usage

```python
from password_generator import generate_password

# Generate a default 16-character password with all character types
password = generate_password()
print(password)

# Generate a 24-character password with only uppercase and digits
custom_password = generate_password(
    length=24,
    use_lowercase=False,
    use_special=False
)
print(custom_password)
```

## Testing

Run the unit tests from the root directory:

```bash
PYTHONPATH=project_2026-11-04 python3 -m unittest project_2026-11-04/test_password_generator.py
```
