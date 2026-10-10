# Daily Project - 2026-10-10

## Overview

Today I built a Secure Password Generator utility in Python.

This tool provides a cryptographically secure way to generate random passwords using Python's built-in `secrets` module, rather than the standard `random` module, to ensure high-security randomness suitable for generating passwords and security tokens.

### Features

- `generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True)`: Generates a secure password.
- Customizable character sets (uppercase, lowercase, digits, special characters).
- Guarantees at least one character from each selected set is included.
- Utilizes `secrets.choice()` for secure character selection and `secrets.SystemRandom().shuffle()` for cryptographically secure shuffling of the final password characters.

### Usage

```python
from password_generator import generate_password

# Generate a default 12-character secure password
password = generate_password()
print(password)

# Generate a 20-character password with only letters and numbers
password_alpha_num = generate_password(length=20, use_special=False)
print(password_alpha_num)
```

### Technical Details

The generator leverages `secrets.choice` to pick random characters from the allowed pools and ensures requirements are met by picking exactly one required character per allowed type first. It then fills the remainder of the password and securely shuffles it in-place using `secrets.SystemRandom().shuffle()`.
