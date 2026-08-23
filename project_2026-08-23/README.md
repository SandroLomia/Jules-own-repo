# Daily Project - 2026-08-23

## Overview

Today's project is a Cryptographically Secure Password Generator CLI.
It is built in Python to generate strong, unpredictable random passwords using Python's `secrets` module, which is designed specifically for cryptography, as opposed to the predictable standard `random` module.

### Features
- Generates a random password of a customizable length.
- Customisable inclusions: toggle uppercase, lowercase, numbers, and special characters.
- Ensures at least one character of each selected type is included (unless the length is shorter than the number of types selected).
- Secure random selection and shuffling using `secrets`.

## Usage

```bash
python3 password_generator.py [options]
```

### Options

- `-l`, `--length`: Length of the password (default: 16)
- `--no-upper`: Exclude uppercase letters
- `--no-lower`: Exclude lowercase letters
- `--no-numbers`: Exclude numbers
- `--no-special`: Exclude special characters

### Examples

Generate a standard 16 character password (all character types):
```bash
python3 password_generator.py
```

Generate a 32 character password with no special characters:
```bash
python3 password_generator.py -l 32 --no-special
```

Generate an 8 character PIN (numbers only):
```bash
python3 password_generator.py -l 8 --no-upper --no-lower --no-special
```
