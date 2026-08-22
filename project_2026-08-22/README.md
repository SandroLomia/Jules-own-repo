# Secure Password Generator

This is a utility script that provides a simple function to generate cryptographically secure random passwords.

## What is this?
The `password_generator.py` script contains a `generate_password` function that allows you to specify the length and the types of characters (uppercase, lowercase, numbers, specials) to include in the generated password.

## Why is it secure?
Instead of using Python's standard `random` module, which is suitable for simulations but not for generating security tokens or passwords, this script leverages the built-in `secrets` module. The `secrets` module provides access to the most secure source of randomness that the operating system provides (e.g., `/dev/urandom` on Unix-like systems). This ensures the generated passwords are not predictable.

## How to use it
You can import the `generate_password` function into your own Python scripts:

```python
from password_generator import generate_password

# Generate a default 16-character password (includes all character types)
pwd = generate_password(16)
print(pwd)

# Generate a 20-character password with only letters and numbers
pwd2 = generate_password(20, use_specials=False)
print(pwd2)
```

## Running tests
You can run the unit tests with:
```bash
python3 -m unittest test_password_generator.py
```
