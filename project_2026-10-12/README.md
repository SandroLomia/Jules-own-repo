# Daily Project - 2026-10-12

## Overview

This project implements a cryptographically secure random password generator in Python. It uses the `secrets` module, specifically `secrets.choice` and `secrets.SystemRandom().shuffle()`, to guarantee high-quality randomness suitable for security applications.

Features:
- Configurable password length.
- Optional inclusion of symbols (punctuation).
- Guarantees the presence of at least one lowercase letter, one uppercase letter, and one digit (and one symbol if enabled) when the length is sufficient (>= 4).
- Covered by unit tests.

## Usage

```python
from password_generator import generate_password

# Generate a 16-character password with symbols
print(generate_password(16))

# Generate a 12-character password without symbols
print(generate_password(12, use_symbols=False))
```

## Running Tests

From the repository root:

```bash
PYTHONPATH=project_2026-10-12 python3 -m unittest project_2026-10-12/test_password_generator.py
```
