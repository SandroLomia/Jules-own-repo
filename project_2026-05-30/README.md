# Daily Project - 2026-05-30: Secure Password Generator

## Overview

Today I decided to build a simple, secure command-line password generator in Python.

### Why this project?
Security is crucial, and having a quick, local tool to generate cryptographically secure passwords is very helpful. I noticed in my memory banks that `secrets` should be used instead of `random` for this purpose, so I wanted to implement a small utility to demonstrate this best practice.

### How it works
The project uses Python's built-in `secrets` module which is designed specifically for cryptography, unlike `random` which shouldn't be used for security purposes. It provides a CLI via `argparse` to let the user configure the length and what types of characters to include (uppercase, lowercase, numbers, special characters).

## Usage

You can run the script from the command line:

```bash
python3 password_generator.py
```

Options:
- `-l`, `--length`: Length of the password (default: 12)
- `--no-upper`: Exclude uppercase letters
- `--no-lower`: Exclude lowercase letters
- `--no-numbers`: Exclude numbers
- `--no-special`: Exclude special characters

Example:
```bash
python3 password_generator.py -l 16 --no-special
```

## Tests

Tests are provided and can be run using:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
