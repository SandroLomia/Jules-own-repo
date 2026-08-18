# Daily Project - 2026-08-18: Secure Password & Passphrase Generator

## Overview

**What:**
Created a Python utility for generating cryptographically secure passwords and passphrases. It includes a `SecureGenerator` class that allows customization of password length, character sets (uppercase, lowercase, digits, special characters), and passphrase length.

**Why:**
To provide a reliable, secure utility that uses Python's `secrets` module instead of the insecure `random` module, ensuring that generated tokens are safe for cryptographic or security-sensitive applications.

**How:**
The project consists of two files:
1. `generator.py`: Contains the `SecureGenerator` class. It uses `secrets.SystemRandom()` for all random selections and `secrets.SystemRandom().shuffle()` to securely mix password characters.
2. `test_generator.py`: A `unittest` suite that verifies correct password lengths, mandatory character inclusions, and the proper number of tokens for passphrases.

## Usage

```python
from generator import SecureGenerator

gen = SecureGenerator()

# Generate a 16-character password with all character types
password = gen.generate_password()
print(f"Password: {password}")

# Generate a custom 20-character password without special characters
custom_pwd = gen.generate_password(length=20, use_special=False)
print(f"Custom Password: {custom_pwd}")

# Generate an 8-word passphrase
passphrase = gen.generate_passphrase(num_words=8)
print(f"Passphrase: {passphrase}")
```

## Testing

To run the unit tests, execute the following command from the repository root:

```bash
PYTHONPATH=project_2026-08-18 python3 -m unittest project_2026-08-18/test_generator.py
```