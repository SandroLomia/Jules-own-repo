# Cryptographically Secure Password Generator

This project is a daily build to create a command-line utility for generating cryptographically secure random passwords.

## What

This is a Python script (`password_generator.py`) that uses the standard library `secrets` module, instead of the basic `random` module, to guarantee secure randomness. It is configurable, allowing the user to specify length and which character sets (uppercase, lowercase, digits, special characters) to include.

## Why

Many simple password generators rely on the `random` module, which is predictable and unfit for generating security-sensitive data. This utility addresses that flaw by utilizing `secrets.SystemRandom().shuffle()` to ensure robust, secure passwords.

## How to use

The script can be run from the command line:

```bash
# Generate a default password (16 chars, all types)
python3 password_generator.py

# Generate a password of length 24
python3 password_generator.py -l 24

# Generate a password without special characters
python3 password_generator.py --no-special

# Generate a password with only uppercase letters and digits
python3 password_generator.py --no-lower --no-special
```

Run tests using:
```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
