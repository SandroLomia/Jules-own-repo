# Daily Project - 2026-09-19

## Overview

Today's project is a Secure Password Generator built in Python. It allows users to generate cryptographically secure random passwords based on specified criteria such as length and character types (uppercase, lowercase, numbers, and special characters).

## Technical Details

The generator leverages Python's built-in `secrets` module, which provides access to the most secure source of randomness that the operating system provides. This is critical for generating passwords, tokens, and other security-sensitive data, as it prevents predictability that could be exploited by attackers.

Specifically, the script uses:
- `secrets.choice()` to securely select characters from a defined pool.
- `secrets.SystemRandom().shuffle()` to cryptographically shuffle the final password string.

## Usage

```python
from password_generator import generate_password

# Generate a default 12-character password with all character types
password = generate_password()
print(password)

# Generate a 16-character alphanumeric password
alphanumeric_password = generate_password(length=16, special=False)
print(alphanumeric_password)

# Generate an 8-digit PIN
pin = generate_password(length=8, uppercase=False, lowercase=False, special=False)
print(pin)
```
