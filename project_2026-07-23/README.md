# Daily Project - 2026-07-23

## Overview

Today's project is the `SecurePassphraseGenerator`, a Python utility designed to generate highly secure, memorable passphrases. It leverages Python's cryptographically secure `secrets` module to ensure true randomness, avoiding the predictability vulnerabilities of standard pseudorandom number generators (like the default `random` module).

### Key Features
*   **Cryptographically Secure:** Uses `secrets.choice` for independent word selection and `secrets.SystemRandom().shuffle` for unique word sets.
*   **Customizable Word Lists:** Bring your own word list or use the built-in default.
*   **Unique Word Selection:** Option to ensure words do not repeat within a generated passphrase.
*   **Entropy Evaluation:** Calculates the theoretical entropy (in bits) of generated passphrases to evaluate their strength.

### Usage Example

```python
from passphrase_generator import SecurePassphraseGenerator

# Initialize with default word list
generator = SecurePassphraseGenerator()

# Generate a standard 4-word passphrase
passphrase = generator.generate_passphrase()
print(f"Passphrase: {passphrase}")

# Generate a 6-word passphrase with underscores, ensuring unique words
unique_passphrase = generator.generate_passphrase(num_words=6, separator='_', unique=True)
print(f"Unique Passphrase: {unique_passphrase}")

# Calculate entropy for a 6-word passphrase
entropy = generator.evaluate_entropy(6)
print(f"Entropy: {entropy:.2f} bits")
```

### Running Tests

To run the unit tests for this project, navigate to the repository root and execute:

```bash
PYTHONPATH=project_2026-07-23 python3 -m unittest project_2026-07-23/test_passphrase_generator.py
```
