# Daily Project - 2026-09-03

## Overview

Today's project is a **Cryptographically Secure Password Generator** utility written in Python.

### What
Implemented a command-line password generator that outputs secure, random passwords.

### Why
To provide a secure way to generate random passwords using cryptographically secure random number generation (via Python's `secrets` module), fulfilling the daily project goal of creating a new utility.

### How
Created a Python script `password_generator.py` utilizing the `secrets` module to generate passwords from customizable character sets (letters, digits, and punctuation) and ensuring they are cryptographically secure, utilizing `secrets.SystemRandom().shuffle()` to randomly order the characters. Added robust unit tests with the `unittest` module in `test_password_generator.py` to verify lengths, minimum limits, and character inclusion.

## Running the Code

To generate a password with default settings (12 characters, all character sets enabled):

```bash
python3 password_generator.py
```

## Running the Tests

To run the unit tests:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
