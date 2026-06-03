# Daily Project - 2026-06-03

## Secure Password and Passphrase Generator

This project is a lightweight, cryptographically secure command-line tool written in Python to generate passwords and passphrases. It leverages Python's built-in `secrets` module, ensuring that the generated values are secure against prediction attacks, making them suitable for use as actual credentials.

### Features
*   **Password Generator:** Generates random passwords of customizable length. Users can specify whether to include uppercase letters, digits, and symbols.
*   **Passphrase Generator:** Generates passphrases consisting of random words selected from an embedded wordlist. Users can specify the number of words and the separator character.
*   **Cryptographically Secure:** Uses the `secrets` module instead of `random`, making it safe for cryptographic use.

### Usage

The tool uses a CLI interface powered by `argparse`.

#### Generate a Password

Basic usage (generates a 16-character password with mixed case, digits, and symbols):
```bash
python3 cli.py password
```

Customized usage (e.g., 20 characters, no symbols):
```bash
python3 cli.py password -l 20 --no-symbols
```

#### Generate a Passphrase

Basic usage (generates a 4-word passphrase separated by hyphens):
```bash
python3 cli.py passphrase
```

Customized usage (e.g., 6 words separated by spaces):
```bash
python3 cli.py passphrase -w 6 -s " "
```

### Running Tests

To run the unit tests, use the following command from the root of the repository:
```bash
PYTHONPATH=project_2026-06-03 python3 -m unittest project_2026-06-03/test_generator.py
```
