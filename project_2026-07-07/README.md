# Daily Project - 2026-07-07

## Overview

Today's project is a **Secure Password Generator**. It provides a simple, flexible CLI utility for generating cryptographically secure random passwords using Python's built-in `secrets` module instead of the deterministic `random` module.

The script ensures that when you specify the need for uppercase, lowercase, digits, and special characters, it securely selects characters from those pools and shuffles them cryptographically, making it ideal for creating strong tokens or user passwords.

## How to Run

You can run the script via the command line interface:

```bash
python3 password_generator.py
```

By default, this generates a 12-character password using uppercase, lowercase, digits, and special characters.

### CLI Flags

You can customize the generated password using the following flags:

- `-l`, `--length`: Set the desired password length (e.g., `-l 20`). The default is 12.
- `--no-upper`: Exclude uppercase letters.
- `--no-lower`: Exclude lowercase letters.
- `--no-digits`: Exclude digits.
- `--no-special`: Exclude special characters.

### Examples

Generate a 24-character password:
```bash
python3 password_generator.py -l 24
```

Generate a 16-character alphanumeric password (no special characters):
```bash
python3 password_generator.py -l 16 --no-special
```

Generate an 8-character numeric PIN:
```bash
python3 password_generator.py -l 8 --no-upper --no-lower --no-special
```
