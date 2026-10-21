# Daily Project - 2026-10-21: Memorable Password Generator

## Overview

Today's project is a utility tool designed to create memorable, secure passphrases. Instead of relying on a random string of characters which are difficult to remember, this tool strings together random words from a provided wordlist.

To ensure cryptographic security, the random selection process utilizes Python's built-in `secrets` module instead of the standard `random` module.

## Usage

```python
from password_generator import generate_passphrase

wordlist = ["correct", "horse", "battery", "staple"]

# Generate a default 4-word passphrase separated by hyphens
passphrase = generate_passphrase(wordlist)
print(passphrase) # e.g., "horse-battery-correct-staple"

# Generate a custom passphrase
custom_passphrase = generate_passphrase(wordlist, num_words=3, separator="_")
print(custom_passphrase) # e.g., "staple_correct_horse"
```
