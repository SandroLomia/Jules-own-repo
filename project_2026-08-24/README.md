# Secure Password Generator

This project provides a simple, zero-dependency Python utility for generating cryptographically secure random passwords.

## What it is

A Python module that utilizes the built-in `secrets` module to generate robust passwords. It ensures that the generated passwords are unpredictable and suitable for security-sensitive applications, unlike the standard `random` module which is predictable.

## Features

*   **Cryptographically Secure:** Uses `secrets.choice()` and `secrets.SystemRandom().shuffle()` for secure generation and randomization.
*   **Customizable Length:** Define the exact length of the password you need.
*   **Character Sets:** Toggle the inclusion of uppercase letters, lowercase letters, digits, and special characters.
*   **Guaranteed Types:** If a character type (e.g., uppercase) is requested, the generator guarantees that at least one character of that type will be included in the final password.

## How to use

You can run the script directly for some example outputs:

```bash
python3 secure_password_generator.py
```

Or you can import the function into your own Python scripts:

```python
from secure_password_generator import generate_password

# Generate a default 12-character password
my_password = generate_password()
print(my_password)

# Generate a 16-character alphanumeric password
alpha_num = generate_password(length=16, use_special=False)
print(alpha_num)

# Generate an 8-digit PIN
pin = generate_password(length=8, use_uppercase=False, use_lowercase=False, use_special=False)
print(pin)
```

## Running Tests

To run the unit tests, execute the following command from the repository root:

```bash
PYTHONPATH=project_2026-08-24 python3 -m unittest project_2026-08-24/test_secure_password_generator.py
```
