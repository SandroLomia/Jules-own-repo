# Daily Project - 2026-10-20: Secure Password Generator

## Overview

This project provides a robust, cryptographically secure password generator utility in Python.

### What
A Python module (`password_generator.py`) containing a `generate_password()` function that creates secure passwords based on customizable criteria (length, inclusion of uppercase, digits, and symbols).

### Why
Generating secure random values in Python requires the use of the `secrets` module rather than the standard `random` module to ensure cryptographic security. This utility encapsulates best practices, providing a simple, reliable way to generate passwords for other scripts, automation tasks, or user provisioning.

### How
The implementation relies on `secrets.choice()` to pick random characters from defined character pools (`string.ascii_letters`, `string.digits`, `string.punctuation`). It guarantees that at least one character of each requested type is included by initially picking one of each, filling the remaining length from a combined pool, and then securely shuffling the result using `secrets.SystemRandom().shuffle()`.

## Usage

```python
from password_generator import generate_password

# Default: 12 chars, upper, lower, digits, symbols
password = generate_password()
print(f"Default secure password: {password}")

# Custom length and complexity
custom_password = generate_password(length=16, use_symbols=False)
print(f"Alphanumeric password: {custom_password}")
```

## Running Tests

From the repository root, run:
```bash
PYTHONPATH=project_2026-10-20 python3 -m unittest project_2026-10-20/test_password_generator.py
```
