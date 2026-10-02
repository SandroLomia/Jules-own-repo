# Daily Project - 2026-10-02

## Overview

Today's project is a cryptographically secure random password generator built using Python's `secrets` module. It features an `argparse`-powered Command Line Interface (CLI) allowing users to easily customize their generated passwords by specifying length and character sets (uppercase, lowercase, digits, symbols).

## How to Run

You can run the password generator from the command line:

```bash
# Generate a default 16-character password using all character types
python3 password_generator.py

# Generate a 32-character password
python3 password_generator.py --length 32

# Generate a password without symbols
python3 password_generator.py --no-symbols

# Generate an alphanumeric password
python3 password_generator.py --no-symbols --no-upper
```

## Running Tests

To run the unit tests for the password generator:

```bash
PYTHONPATH=project_2026-10-02 python3 -m unittest project_2026-10-02/test_password_generator.py
```
