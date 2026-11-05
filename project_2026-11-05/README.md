# Daily Project - 2026-11-05

## Overview

Today's project is a secure password generator in Python. It provides a highly configurable way to generate random passwords using the cryptographically secure `secrets` module, rather than the standard `random` module which is not suitable for security purposes.

The project features a main `generate_password` function that allows customization of:
- Total length of the password
- Inclusion of uppercase letters
- Inclusion of lowercase letters
- Inclusion of digits
- Inclusion of symbols (punctuation)

The function guarantees that if a character type is selected, at least one character of that type will be present in the final generated password. The output is securely shuffled before being returned.

## Usage

You can import the function into your project:

```python
from password_generator import generate_password

# Generate a default 12-character secure password
print(generate_password())

# Generate a 16-character password with only letters and digits
print(generate_password(length=16, use_symbols=False))
```

## Testing
Run the provided unit tests to verify behavior:
```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
