# Daily Project - 2026-06-30

## Overview

Today's project is a cryptographically secure random password generator utility. It uses Python's built-in `secrets` module to safely generate passwords with combinations of uppercase letters, lowercase letters, numbers, and special characters.

### Features
- Configurable password length.
- Optional inclusion/exclusion of character types (uppercase, lowercase, numbers, special characters).
- Guarantees at least one character from each selected character set is included in the output.
- Cryptographically secure shuffling.

## Usage

You can use the script from the command line:

```bash
# Generate a default 12-character password
python3 password_generator.py

# Generate a 20-character password
python3 password_generator.py -l 20

# Generate an 8-character password with only numbers and letters (no special chars)
python3 password_generator.py -l 8 --no-special

# Generate a 16-character password with only lowercase and numbers
python3 password_generator.py -l 16 --no-upper --no-special
```

## Running Tests

Run the unit tests from the root of the repository:

```bash
PYTHONPATH=project_2026-06-30 python3 -m unittest project_2026-06-30/test_password_generator.py
```
