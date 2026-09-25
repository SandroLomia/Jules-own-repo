# Daily Project - 2026-09-25

## Secure Password Generator

### Overview

Today's project is a cryptographically secure random password generator implemented in Python. It provides a highly configurable and robust way to generate passwords, ensuring that modern security requirements are met.

Unlike Python's standard `random` module, which is designed for simulation and modeling but is not suitable for security purposes, this tool leverages the built-in `secrets` module. The `secrets` module relies on the operating system's cryptographic random number generator, making the generated passwords suitable for managing user accounts, generating API tokens, or any other sensitive applications.

### Features

*   **Cryptographically Secure:** Uses the `secrets` module and `secrets.SystemRandom().shuffle()` for true randomness.
*   **Customizable Length:** Define exactly how long the password should be (default is 12).
*   **Character Class Control:** Toggle the inclusion of:
    *   Uppercase letters
    *   Lowercase letters
    *   Digits
    *   Special characters (punctuation)
*   **Guaranteed Character Inclusion:** The algorithm ensures that if a character class is enabled, at least one character from that class will absolutely appear in the generated password.
*   **Validation:** Automatically prevents the generation of passwords if the length is too short to satisfy the requested character classes, or if all classes are disabled.

### Usage

```python
from password_generator import PasswordGenerator

# 1. Generate a default password (12 chars: upper, lower, digits, special)
pwd_default = PasswordGenerator.generate()
print(f"Default: {pwd_default}")

# 2. Generate a 16-character password with no special characters
pwd_nospecial = PasswordGenerator.generate(length=16, use_special=False)
print(f"No special chars: {pwd_nospecial}")

# 3. Generate a 8-character PIN (digits only)
pin = PasswordGenerator.generate(length=8, use_uppercase=False, use_lowercase=False, use_special=False)
print(f"PIN: {pin}")
```

### Testing

The project includes a comprehensive `unittest` suite that validates lengths, character class inclusions, exclusion flags, and edge-case exceptions.

Run the tests from the repository root:

```bash
PYTHONPATH=project_2026-09-25 python3 -m unittest project_2026-09-25/test_password_generator.py
```
