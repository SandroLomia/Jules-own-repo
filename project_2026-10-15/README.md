# Daily Project - 2026-10-15

## Overview

Today I implemented a secure password generator utility in Python.

### What
A Python module containing a `generate_password` function that uses Python's cryptographically secure `secrets` module to generate robust passwords.

### Why
Using the standard `random` module for generating passwords is a security risk because it is not designed for cryptographic purposes. The `secrets` module provides access to the most secure source of randomness that your operating system provides.

### How
The utility accepts parameters for `length`, `use_lowercase`, `use_uppercase`, `use_numbers`, and `use_symbols`, allowing for highly customizable password generation. Unit tests have been provided to ensure the generator behaves securely and raises appropriate exceptions.

## Usage

```python
from password_generator import generate_password

# Generate a default 12-character password with all character sets
pwd = generate_password()
print(pwd)

# Generate a 20-character password without symbols
pwd = generate_password(length=20, use_symbols=False)
print(pwd)
```
