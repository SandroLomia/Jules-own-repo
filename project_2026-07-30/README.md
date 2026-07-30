# Daily Project - 2026-07-30

## Overview

Today's project is a **Secure Password Generator** utility written in Python.

Unlike standard random generators which rely on pseudo-random number generators (like Python's `random` module) that might be predictable, this utility uses the `secrets` module, making it cryptographically secure.

### Features
* Cryptographically secure character selection and shuffling.
* Customizable password length (default 12 characters).
* Ability to toggle inclusion of uppercase, lowercase, digits, and special characters.
* Guarantees at least one character from each selected pool is present in the generated password.

## How to Run

To run the password generator and see example outputs:

```bash
python3 password_generator.py
```

### Running Tests

To run the test suite and verify the logic:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
