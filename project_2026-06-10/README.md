# Daily Project - 2026-06-10

## Overview

Today's project is a cryptographically secure random password generator module written in Python. It provides a simple API to generate passwords with customizable lengths and character set constraints (uppercase, numbers, and special characters).

The module is designed using the built-in `secrets` library instead of `random` to ensure that generated passwords are unpredictable and secure against cryptographic attacks.

## Usage

You can import the module or run it directly.

```python
from generator import generate_password

# Generate a default 12-character password
password = generate_password()

# Generate a customized password
custom_password = generate_password(
    length=16,
    use_upper=True,
    use_numbers=True,
    use_special=False
)
```

To run a quick demonstration:
```bash
python3 generator.py
```

## Tests

The project includes a comprehensive suite of unit tests. To run them, execute the following from the root directory:

```bash
PYTHONPATH=project_2026-06-10 python3 -m unittest project_2026-06-10/test_generator.py
```
