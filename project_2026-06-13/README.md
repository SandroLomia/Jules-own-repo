# Daily Project - 2026-06-13: Secure Password Generator

## Overview

This project provides a cryptographically secure random password generator utility. It uses Python's built-in `secrets` module, which is the most secure module available for generating pseudo-random numbers suitable for managing secrets, such as passwords, account authentication, security tokens, and related secrets.

Unlike the standard `random` module, which is designed for modeling and simulation and is completely predictable, `secrets` provides access to the most secure source of randomness that your operating system provides.

## Features

- Generates passwords of customizable length.
- Allows configuration of character sets:
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Special characters (punctuation)
- Completely secure using cryptographic random generators.

## Usage

You can use the `PasswordGenerator` class in your own Python scripts:

```python
from password_generator import PasswordGenerator

# Create a generator with default settings (all character types enabled)
generator = PasswordGenerator()

# Generate a 16-character password
print(generator.generate(16))

# Create a generator for PIN codes (digits only)
pin_generator = PasswordGenerator(use_lower=False, use_upper=False, use_special=False)
print(pin_generator.generate(6))
```

## Running Tests

To run the unit tests for the password generator, navigate to the repository root and execute:

```bash
PYTHONPATH=project_2026-06-13 python3 -m unittest project_2026-06-13/test_password_generator.py
```
