# Daily Project - 2026-07-24

## Cryptographically Secure Password Generator

### Overview

Today's project is a Python-based utility for generating cryptographically secure random passwords. It allows users to customize the length and complexity of the passwords generated (uppercase, lowercase, digits, and symbols).

I chose to build this because generating secure passwords is a common and important utility. The implementation relies on the Python `secrets` module instead of the standard `random` module to ensure cryptographic security, in both character selection and shuffling.

### Features
- Cryptographically secure character selection and shuffling using `secrets`.
- Customizable length.
- Toggleable inclusion of:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Symbols (punctuation)
- Enforces minimum length based on enabled constraints.
- Validates that at least one character type is selected.

### Usage

```python
from password_generator import PasswordGenerator

generator = PasswordGenerator()

# Generate a default password (length 12, all character types enabled)
password = generator.generate()
print(password)

# Generate a custom password
custom_password = generator.generate(length=16, use_symbols=False)
print(custom_password)
```

### Running Tests

To run the unit tests, execute the following command from the repository root:

```bash
PYTHONPATH=project_2026-07-24 python3 -m unittest project_2026-07-24/test_password_generator.py
```
