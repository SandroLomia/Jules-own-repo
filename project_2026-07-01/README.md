# Daily Project - 2026-07-01

## Overview

Today's project is a cryptographically secure password generator utility in Python.

### Features
- Generates random passwords of a specified length (default 12).
- Allows toggling the inclusion of uppercase letters, lowercase letters, numbers, and symbols.
- Uses Python's `secrets` module instead of `random` for cryptographic security. The `random` module generates pseudo-random numbers which are predictable and not suitable for security-sensitive applications like passwords. The `secrets` module uses system sources of true randomness.
- Includes thorough unit tests for various configurations and edge cases.

### Usage

```python
from password_generator import generate_password

# Generate a default 12-character password with all character types
password = generate_password()
print(password)

# Generate a 20-character password without symbols
password_no_symbols = generate_password(length=20, use_symbols=False)
print(password_no_symbols)
```

### Running Tests

To run the unit tests from the repository root:
```bash
PYTHONPATH=project_2026-07-01 python3 -m unittest project_2026-07-01/test_password_generator.py
```
