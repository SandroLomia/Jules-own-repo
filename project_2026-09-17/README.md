# Daily Project - 2026-09-17: Secure Password Generator

## Overview

Today I decided to create a secure password generator utility because it is a practical tool that enforces security best practices. It's built in Python and utilizes the cryptographically secure `secrets` module (specifically `secrets.SystemRandom().shuffle()`) instead of the standard `random` module, ensuring that the generated passwords are safe for sensitive use cases.

## Features

- Generates cryptographically secure random passwords.
- Customizable password length (minimum 4 characters, default 16).
- Options to include/exclude uppercase letters, numbers, and symbols.
- Command Line Interface (CLI) for easy usage.

## Usage

You can run the password generator from the command line:

```bash
# Generate a password with default settings (length 16, all character types included)
python3 password_generator.py

# Generate a password of length 32
python3 password_generator.py -l 32

# Generate a password excluding symbols
python3 password_generator.py --no-symbols

# Generate a password with only lowercase and numbers
python3 password_generator.py --no-uppercase --no-symbols
```

## Testing

Unit tests are provided to ensure the generator works as expected and handles edge cases appropriately.

Run the tests using the following command from the repository root:

```bash
PYTHONPATH=project_2026-09-17 python3 -m unittest project_2026-09-17/test_password_generator.py
```
