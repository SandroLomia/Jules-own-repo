# Daily Project - 2026-09-06

## Overview

Today's project is a cryptographically secure random password generator built in Python.

### Features

- Uses the `secrets` module, which is cryptographically secure (unlike the standard `random` module).
- Supports generating passwords of customizable length (minimum 8 characters for security).
- Ensures that requested character sets (lowercase, uppercase, numbers, symbols) are always included in the generated password.
- Employs a secure shuffle of password characters using `secrets.SystemRandom().shuffle()`.

### Files

- `password_generator.py`: The main script containing the `generate_password` function.
- `test_password_generator.py`: Unit tests verifying the length, exceptions, and complexity requirements of generated passwords.

### Usage

Run the script directly to see an example of password generation:
```bash
python3 password_generator.py
```

### Running Tests

To run the unit tests from the repository root:
```bash
PYTHONPATH=project_2026-09-06 python3 -m unittest project_2026-09-06/test_password_generator.py
```
