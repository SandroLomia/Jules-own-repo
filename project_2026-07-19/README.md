# Daily Project - 2026-07-19

## Overview

This project implements a `SecureGenerator` utility class designed to generate cryptographically secure values in Python.

It provides a safer alternative to the standard `random` module (which is not meant for security/cryptography) by leveraging Python's built-in `secrets` module.

## Features

- **Secure Password Generation:** Generates random passwords of customizable length, with or without symbols, using `secrets.choice`.
- **Secure List Shuffling:** Performs a cryptographically secure in-place shuffle of a list using `secrets.SystemRandom().shuffle()`.

## Usage

```python
from secure_generator import SecureGenerator

# Generate a 20-character password with symbols
password = SecureGenerator.generate_password(length=20, use_symbols=True)
print(password)

# Securely shuffle a list of sensitive data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
SecureGenerator.secure_shuffle(data)
print(data)
```

## Running Tests

From the repository root, run the following command to execute the unit tests:

```bash
PYTHONPATH=project_2026-07-19 python3 -m unittest project_2026-07-19/test_secure_generator.py
```