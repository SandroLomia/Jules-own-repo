# Daily Project - 2026-08-05

## Overview

Today's project is a **Secure Password Generator** utility.

It provides a cryptographically secure way to generate random passwords, ensuring that passwords are not easily guessable and meet common complexity requirements.

### Why this project?
When developing various tools and systems, generating strong, secure passwords or tokens is a frequent requirement. Using standard random number generators (like Python's `random` module) is not suitable for security-sensitive applications. This utility leverages Python's `secrets` module to ensure cryptographic security.

### Features
* **Cryptographically Secure:** Uses `secrets.choice` and `secrets.SystemRandom().shuffle()`.
* **Customizable Length:** Generate passwords of any length (default is 12).
* **Configurable Complexity:** Easily toggle the inclusion of lowercase letters, uppercase letters, digits, and special characters.
* **Guaranteed Inclusion:** Ensures that at least one character from every selected character set is included in the final password.

## Usage

```python
from password_generator import generate_password

# Generate a default 12-character password with all character types
default_pw = generate_password()
print(f"Default Password: {default_pw}")

# Generate a 16-character alphanumeric password
alphanumeric_pw = generate_password(length=16, use_special=False)
print(f"Alphanumeric Password: {alphanumeric_pw}")
```

## Running Tests

To run the unit tests for this utility:

```bash
PYTHONPATH=project_2026-08-05 python3 -m unittest project_2026-08-05/test_password_generator.py
```
