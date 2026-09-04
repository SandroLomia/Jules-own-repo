# Daily Project - 2026-09-04

## Overview

This project implements a **Cryptographically Secure Password Generator** utility in Python.

It provides both a reusable module and a command-line interface to generate robust passwords according to user-specified constraints (length, inclusion of uppercase letters, lowercase letters, numbers, and symbols).

It utilizes the built-in Python `secrets` module, which is designed to be cryptographically secure for generating sensitive data, unlike the standard `random` module.

## Usage

You can run the script directly from the command line:

```bash
python3 password_generator.py [options]
```

### Options

- `-l, --length`: Specifies the length of the password (default: 16).
- `--no-upper`: Excludes uppercase letters from the generated password.
- `--no-lower`: Excludes lowercase letters from the generated password.
- `--no-numbers`: Excludes numbers from the generated password.
- `--no-symbols`: Excludes symbols from the generated password.

### Examples

Generate a default 16-character password (includes all character types):
```bash
python3 password_generator.py
```

Generate a 32-character password:
```bash
python3 password_generator.py -l 32
```

Generate a 12-character password using only lowercase letters and numbers:
```bash
python3 password_generator.py -l 12 --no-upper --no-symbols
```

## Testing

Run the included unit tests using:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
