# Secure Password & Passphrase Generator

## Overview

This project provides a cryptographically secure random password and passphrase generator using Python's `secrets` module. It includes a core generation module and an easy-to-use Command Line Interface (CLI) wrapper.

## Features

- **Passwords**: Generates random passwords with customizable length and optional inclusion/exclusion of uppercase, lowercase, digits, and symbols.
- **Passphrases**: Generates random multi-word passphrases chosen from a built-in dictionary, with customizable word counts and separators.
- **Security**: Built purely using the `secrets` module which is designed for cryptographic applications, ensuring high entropy compared to the standard `random` module.

## Usage

You can use the generator via the provided CLI:

### Generate a Password

Generate a standard password (default length 16, using all character types):
```bash
python cli.py password
```

Generate a 20-character password without symbols:
```bash
python cli.py password --length 20 --no-symbols
```

### Generate a Passphrase

Generate a standard passphrase (default 4 words, separated by '-'):
```bash
python cli.py passphrase
```

Generate a 6-word passphrase separated by underscores:
```bash
python cli.py passphrase --words 6 --separator _
```

## Running Tests

To run the unit tests from the repository root:

```bash
PYTHONPATH=project_2026-07-09 python3 -m unittest project_2026-07-09/test_generator.py
```
