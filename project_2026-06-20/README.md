# Daily Project - 2026-06-20

## Overview

Today's project is a cryptographically secure **Password Generator** tool written in Python.

### Why
Generating strong and secure passwords is an essential security practice. Relying on default Python `random` module for generating sensitive information like passwords is not secure as it's deterministic. This tool utilizes the Python `secrets` module, which uses the operating system's most secure source of randomness, providing a reliable way to generate passwords, tokens, and other sensitive materials.

### Features
* **Cryptographically Secure:** Uses the `secrets` module for secure randomness.
* **Customizable Length:** Define the desired length of the password.
* **Character Set Options:** Toggle the inclusion of uppercase, lowercase, digits, and symbols to meet varying password policies.
* **Guaranteed Inclusions:** Ensures at least one character from each selected character type is present in the final password.

### Usage
You can run the script directly to see a sample 16-character password:

```bash
python3 password_generator.py
```

Or import it into your own modules:
```python
from password_generator import generate_password

# Default 12-character password
print(generate_password())

# 20-character password with only letters and digits
print(generate_password(length=20, include_symbols=False))
```

### Testing
Unit tests are provided using the `unittest` module. To run the tests:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
