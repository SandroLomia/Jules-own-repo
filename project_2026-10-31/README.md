# Daily Project - 2026-10-31

## Overview

Secure Password Generator

This utility provides a robust way to generate cryptographically secure random passwords using Python's `secrets` module. Unlike the standard `random` module, `secrets` provides access to the most secure source of randomness that your operating system provides, making it suitable for generating passwords and security tokens.

## Usage

```python
from password_generator import generate_password

# Generate a default 16-character password (includes lowercase, uppercase, numbers, and symbols)
pwd1 = generate_password(16)

# Generate a 12-character alphanumeric password (no symbols)
pwd2 = generate_password(12, use_symbols=False)

# Generate an 8-character lowercase-only password
pwd3 = generate_password(8, use_uppercase=False, use_numbers=False, use_symbols=False)
```

## Running Tests

To run the unit tests, execute the following from the root of the repository:

```bash
PYTHONPATH=project_2026-10-31 python3 -m unittest project_2026-10-31/test_password_generator.py
```
