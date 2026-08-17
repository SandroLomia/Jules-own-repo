# Daily Project - 2026-08-17: Secure Password Generator

## Overview

Today's project is a robust, cryptographically secure password generator utility built in Python.

## Why this direction?

When generating passwords, tokens, or security-sensitive random values in Python, the standard `random` module is insufficient because it is a pseudo-random number generator designed for modeling and simulation, not security. To guarantee high entropy and unpredictability, it is essential to use the built-in `secrets` module. This script demonstrates how to securely select characters and how to securely shuffle them using `secrets.SystemRandom().shuffle()`.

## Features

- **Cryptographically Secure:** Uses Python's `secrets` module for all random selections and shuffling.
- **Guaranteed Character Sets:** Every generated password (minimum length 4) is guaranteed to contain at least one:
  - Lowercase letter
  - Uppercase letter
  - Digit
  - Punctuation mark
- **Customizable Length:** Generates passwords of any length (>= 4), defaulting to 12.

## How to Run

To run the password generator and see an example output:
```bash
python3 password_generator.py
```

To run the test suite:
```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
