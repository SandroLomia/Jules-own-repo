# Daily Project - 2026-07-13: SecurePassGen

## Overview

Today's project is **SecurePassGen**, a cryptographic utility class designed to generate highly secure passwords and passphrases. It leverages Python's built-in `secrets` module rather than the standard `random` module, ensuring that the random values produced are cryptographically strong and suitable for security-sensitive applications like account creation, API key generation, and token management.

## Features

- **Secure Password Generation:** Generates passwords of customizable length, with the ability to selectively include uppercase, lowercase, digits, and special characters. It guarantees at least one character of each requested type.
- **Secure Passphrase Generation:** Generates passphrases by randomly selecting a specified number of words from a provided wordlist, joined by a custom separator (defaulting to a hyphen `-`).
- **Cryptographic Shuffling:** Uses `secrets.SystemRandom().shuffle()` to securely randomize the characters of the generated password, defeating potential pattern analysis.

## Usage

```python
from secure_pass_gen import PasswordGenerator

# Generate a default 16-character secure password (all char types included)
password = PasswordGenerator.generate_password()
print(f"Password: {password}")

# Generate a 24-character alphanumeric password
alpha_num_pwd = PasswordGenerator.generate_password(length=24, use_special=False)
print(f"Alphanumeric Password: {alpha_num_pwd}")

# Generate a passphrase from a custom wordlist
wordlist = ["correct", "horse", "battery", "staple"]
passphrase = PasswordGenerator.generate_passphrase(num_words=4, wordlist=wordlist, separator="-")
print(f"Passphrase: {passphrase}")
```
