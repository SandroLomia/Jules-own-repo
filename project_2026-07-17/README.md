# Daily Project - 2026-07-17

## Overview

Today's project is a utility tool: **Secure Password Generator**.

This utility generates cryptographically secure passwords using Python's built-in `secrets` module, ensuring randomness suitable for security and cryptography applications, avoiding the predictably pseudo-random standard `random` module.

It provides functionality to customize password length and inclusion of character sets like uppercase letters, numbers, and special symbols.

## Files

- `secure_password_generator.py`: Contains the `generate_password` and `shuffle_string` functions.
- `test_secure_password_generator.py`: Contains extensive unit tests to verify the behavior of the generator.

## Usage

To generate a password directly from the command line:

```bash
python3 secure_password_generator.py
```

To use it in your code:

```python
from secure_password_generator import generate_password

# Default: 12 chars, includes uppercase, numbers, and special characters
password = generate_password()
print(password)

# Custom: 20 chars, lowercase and numbers only
custom_password = generate_password(length=20, use_uppercase=False, use_special=False)
print(custom_password)
```

## Testing

Run tests by executing:

```bash
PYTHONPATH=. python3 -m unittest test_secure_password_generator.py
```
