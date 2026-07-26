# Daily Project - 2026-07-26: Secure Password Generator

## Overview

Today I decided to create a Secure Password Generator utility in Python.

**Why:** The standard Python `random` module is not meant for security or cryptographic purposes. Building a dedicated tool using the `secrets` module ensures that generated passwords and passphrases are cryptographically secure and resistant to prediction.

**What:** This utility provides two functions:
- `generate_password()`: Creates a completely random string of a specified length using a mix of character pools (uppercase, lowercase, numbers, and symbols). It explicitly guarantees that at least one character from every selected pool is present in the final password.
- `generate_passphrase()`: Creates a random passphrase consisting of multiple words joined by a separator, making it easier for humans to remember while still maintaining high entropy.

**How:** The implementation uses Python's built-in `secrets` module (`secrets.choice` and `secrets.SystemRandom().shuffle()`) to securely pick and scramble characters and words.

## Usage

```python
from secure_password_generator import generate_password, generate_passphrase

# Generate a 16-character password with all character types
password = generate_password(length=16, uppercase=True, lowercase=True, numbers=True, symbols=True)
print(f"Password: {password}")

# Generate a 4-word passphrase
passphrase = generate_passphrase(num_words=4)
print(f"Passphrase: {passphrase}")
```
