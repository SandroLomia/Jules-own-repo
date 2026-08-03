# Daily Project - 2026-08-03: Cryptographically Secure Password Generator

## Overview

This project provides a simple yet highly secure password generator written in Python.

Standard random number generators (like Python's built-in `random` module) are not suitable for security purposes such as generating passwords or security tokens because they are deterministic and predictable.

This utility uses Python's `secrets` module, which is designed specifically for cryptography and relies on the operating system's secure sources of random numbers (e.g., `/dev/urandom` on Unix-like systems). It also uses `secrets.SystemRandom().shuffle()` to securely randomize the order of characters in the generated password, ensuring maximum entropy.

## Features

* **High Security:** Uses the `secrets` module for cryptographically strong random generation.
* **Customizable:** Allows you to specify the exact length of the password and precisely which character sets to include (uppercase, lowercase, digits, symbols).
* **Guaranteed Complexity:** Ensures that at least one character from each selected character set is included in the final password.

## How to Run

To use the generator in your own Python script:

```python
from password_generator import generate_password

# Default: 12 characters, all character sets
print(generate_password())

# Custom: 16 characters, alphanumeric only
print(generate_password(length=16, use_symbols=False))
```

To run the unit tests, use the following command from the repository root:

```bash
PYTHONPATH=project_2026-08-03 python3 -m unittest project_2026-08-03/test_password_generator.py
```
