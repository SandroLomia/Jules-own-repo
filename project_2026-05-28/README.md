# Daily Project - 2026-05-28

## Overview

Today's project is a **Secure Password Generator CLI Tool**.

This tool is designed to generate cryptographically secure passwords using Python's `secrets` module, ensuring that the generated passwords are safe for sensitive use cases (unlike the standard `random` module).

## Features

- Generates passwords of customizable length.
- Options to include or exclude uppercase letters, digits, and special characters.
- Uses `secrets` module for cryptographically secure pseudo-random number generation (CSPRNG).
- Fully covered by unit tests using Python's `unittest`.

## Usage

You can run the script via the command line.

```bash
# Generate a default 16-character password with all character sets
python3 password_generator.py

# Generate a 32-character password
python3 password_generator.py -l 32
python3 password_generator.py --length 32

# Exclude uppercase letters
python3 password_generator.py --no-upper

# Exclude digits and special characters
python3 password_generator.py --no-digits --no-special
```

## Testing

To run the unit tests, use the following command from the repository root:

```bash
PYTHONPATH=project_2026-05-28 python3 -m unittest project_2026-05-28/test_password_generator.py
```
