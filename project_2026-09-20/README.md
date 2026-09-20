# Daily Project - 2026-09-20

## Overview

Today's project is a **Secure Password Generator** built in Python. It provides a simple utility function to generate cryptographically strong random passwords of customizable length and character composition.

### Why use `secrets` instead of `random`?

The standard `random` module in Python is designed for modeling and simulation, not security or cryptography. Its pseudo-random number generator is predictable if an attacker has enough previous outputs.

This project uses Python's built-in `secrets` module which provides access to the most secure source of randomness that your operating system provides (e.g. `/dev/urandom` on Unix). By leveraging `secrets.choice()` for selecting characters and `secrets.SystemRandom().shuffle()` for shuffling, the generated passwords are unpredictable and suitable for security-sensitive applications like account generation, tokens, or encryption keys.

## Features

- Configurable password length (default 12).
- Options to include or omit uppercase letters, numbers, and symbols.
- Guarantees at least one character from each selected set is included (if the requested length allows it).
- Includes comprehensive unit tests.

## Usage

You can run the script directly to generate a default 12-character password:

```bash
python3 secure_password_generator.py
```

You can also import it in your Python code:

```python
from secure_password_generator import generate_password

# Generate a default 12-character password
print(generate_password())

# Generate a 16-character password without symbols
print(generate_password(length=16, include_symbols=False))
```

## Running Tests

To run the unit tests:

```bash
PYTHONPATH=. python3 -m unittest test_secure_password_generator.py
```
