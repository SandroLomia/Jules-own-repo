# Secure Password Generator (project_2026-10-28)

This project contains a Python utility for generating cryptographically secure random passwords using the built-in `secrets` module.

## Features

- Configurable length (default 16 characters).
- Toggle inclusion of uppercase letters, lowercase letters, numbers, and symbols.
- Guarantees at least one character of each requested type is present in the final password.
- Cryptographically secure shuffling using `secrets.SystemRandom().shuffle()`.

## Usage

```python
from secure_password_generator import generate_password

# Generate a default 16-character password with all character types
default_password = generate_password()
print(f"Default Password: {default_password}")

# Generate a 32-character password using only uppercase and lowercase letters
letters_only = generate_password(length=32, use_numbers=False, use_symbols=False)
print(f"Letters Only: {letters_only}")
```

## Running Tests

To run the unit tests, execute the following from the root of the repository:

```bash
PYTHONPATH=project_2026-10-28 python3 -m unittest project_2026-10-28/test_secure_password_generator.py
```
