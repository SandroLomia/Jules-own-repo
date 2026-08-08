# Daily Project - 2026-08-08

## Overview

Today I built a secure password generator CLI utility.

This tool generates cryptographically secure passwords using Python's built-in `secrets` module. It supports custom password lengths and allows the user to exclude specific character classes (uppercase, digits, special characters).

## Usage

Run the password generator from the command line:

```bash
python3 password_generator.py [options]
```

### Options

*   `-l LENGTH`, `--length LENGTH`: Length of the password (default: 16)
*   `--no-upper`: Exclude uppercase letters
*   `--no-digits`: Exclude digits
*   `--no-special`: Exclude special characters

### Examples

Generate a standard 16-character password:
```bash
python3 password_generator.py
```

Generate a 32-character password:
```bash
python3 password_generator.py -l 32
```

Generate an 8-character password with no special characters:
```bash
python3 password_generator.py -l 8 --no-special
```
