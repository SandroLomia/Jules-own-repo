# Daily Project - 2026-11-03

## Overview

Today's project is a **Secure Password Generator**. It provides a simple, cryptographically secure way to generate random passwords using Python's `secrets` module, rather than the non-secure `random` module.

The utility allows customization of the password length and character sets used (lowercase, uppercase, digits, and special characters).

### Features
* Generates cryptographically secure passwords.
* Customizable password length (default: 12).
* Toggleable inclusion of character sets:
    * Lowercase letters
    * Uppercase letters
    * Digits
    * Special characters

### Usage

You can run the script directly to see some example outputs:

```bash
python3 secure_password_generator.py
```

To use it in your code:

```python
from secure_password_generator import generate_password

# Generate a default 12-character password
password = generate_password()
print(password)

# Generate a 20-character alphanumeric password
alphanumeric = generate_password(length=20, use_special=False)
print(alphanumeric)
```

### Running Tests

To run the unit tests from the repository root:

```bash
PYTHONPATH=project_2026-11-03 python3 -m unittest project_2026-11-03/test_secure_password_generator.py
```
