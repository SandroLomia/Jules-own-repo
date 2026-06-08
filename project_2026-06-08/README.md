# Daily Project - 2026-06-08

## Overview

Today's project is a **Cryptographically Secure Password Generator** built in Python.

As security is paramount, it is important to generate random strings using a cryptographically secure random number generator rather than standard pseudo-random generators (like Python's built-in `random` module). This project utilizes the `secrets` module introduced in Python 3.6 to generate robust and secure passwords.

## Features

* **Customizable Length**: Generates passwords of any length (minimum 8 characters).
* **Character Toggles**: Easily include or exclude uppercase letters, numbers, and special characters to meet various password requirements.
* **Cryptographically Secure**: Uses `secrets.choice()` for true randomness suitable for managing secrets.

## Usage

You can run the script directly to generate a few example passwords:

```bash
python3 password_generator.py
```

Or you can import it into your own scripts:

```python
from password_generator import generate_password

# Default (16 chars, all character types)
secure_pwd = generate_password()

# Custom settings
custom_pwd = generate_password(length=32, use_special=False)
```

## Running Tests

Unit tests are included to verify functionality and ensure the password generator behaves correctly under different constraints. Run the tests using the following command from the repository root:

```bash
PYTHONPATH=project_2026-06-08 python3 -m unittest project_2026-06-08/test_password_generator.py
```
