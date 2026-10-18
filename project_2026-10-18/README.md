# Daily Project - 2026-10-18

## Overview

Today's project is a **Secure Password Generator**. It provides a utility class `SecurePasswordGenerator` in Python for generating cryptographically secure passwords and evaluating their strength.

### Key Features
* Uses the Python `secrets` module, making it cryptographically secure and suitable for generating real-world passwords and tokens (as opposed to the standard `random` module).
* Allows customization of password complexity requirements (uppercase, lowercase, digits, special characters).
* Provides a strength evaluator based on password length and complexity, classifying passwords as Weak, Medium, or Strong.

## How to use

You can use the generator within your own Python scripts:

```python
from password_generator import SecurePasswordGenerator

generator = SecurePasswordGenerator()
password = generator.generate_password(length=16)
print(f"Generated Password: {password}")

strength = generator.evaluate_strength(password)
print(f"Password Strength: {strength}")
```

## Running Tests

To verify the functionality, run the unittests:

```bash
PYTHONPATH=project_2026-10-18 python3 -m unittest project_2026-10-18/test_password_generator.py
```
