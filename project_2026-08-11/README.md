# Daily Project - 2026-08-11: Secure Password Generator

## Overview

This project implements a cryptographically secure password generator in Python. It is designed to generate random passwords using the `secrets` module, which is suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

Unlike the standard `random` module, which is designed for modeling and simulation, the `secrets` module generates numbers and choices in a way that makes it practically impossible for an attacker to predict the output.

## Features

- **Cryptographically Secure**: Utilizes `secrets.choice()` for character selection and `secrets.SystemRandom().shuffle()` for sequence randomization.
- **Customizable**: Allows configuration of password length.
- **Flexible Character Sets**: Users can include or exclude uppercase letters, lowercase letters, digits, and special characters.
- **Validation**: Enforces a minimum length for security and ensures at least one character type is selected.

## Files

- `secure_password_generator.py`: Contains the `generate_password` function and logic.
- `test_secure_password_generator.py`: Contains unit tests for the password generator.

## How to Run

You can run the script directly to see a generated password example:

```bash
python3 secure_password_generator.py
```

### Running Tests

To run the unit tests, use the following command from the project root:

```bash
PYTHONPATH=project_2026-08-11 python3 -m unittest project_2026-08-11/test_secure_password_generator.py
```
