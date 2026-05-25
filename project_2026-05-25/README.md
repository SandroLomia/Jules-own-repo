# Daily Project - 2026-05-25: Password Generator

## Overview

Today's project is a highly customizable, secure Password Generator implemented in Python.

### Why this project?
Security is paramount, and generating strong, unpredictable passwords is a common necessity for both users and systems. This utility provides a simple, robust CLI interface allowing users to generate passwords tailored to their specific constraint requirements, serving as an excellent foundational utility that can be imported by other projects or run standalone.

### How it's implemented

The core logic lives in `password_generator.py`. It uses Python's cryptographically secure `secrets` module alongside `string` constants (ascii letters, digits, punctuation).
The `generate_password` function guarantees that at least one character of each requested type (lowercase, uppercase, number, symbol) is included in the output. The remaining length is filled with a randomized pool of the allowed characters, and the final list is shuffled to prevent predictable placement of the guaranteed character types.

The application utilizes `argparse` to provide a user-friendly CLI.

Comprehensive unit tests cover the generator in `test_password_generator.py`, verifying constraints, lengths, and edge cases.

## Usage

You can run the script directly from the terminal to generate a default password (length 12, including uppercase, numbers, and symbols):

```bash
python3 password_generator.py
```

### Options

* `-l`, `--length`: Set the desired password length.
* `--no-uppercase`: Exclude uppercase letters.
* `--no-numbers`: Exclude numbers.
* `--no-symbols`: Exclude special symbol characters.

### Examples

Generate a 20-character password:
```bash
python3 password_generator.py -l 20
```

Generate a 16-character alphanumeric password (no symbols):
```bash
python3 password_generator.py -l 16 --no-symbols
```

## Running Tests

To run the test suite, use the `unittest` module from the project root:

```bash
PYTHONPATH=project_2026-05-25 python3 -m unittest project_2026-05-25/test_password_generator.py
```
