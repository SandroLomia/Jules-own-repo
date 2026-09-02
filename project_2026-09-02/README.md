# Daily Project - 2026-09-02: Cryptographically Secure Password Generator

## Overview

This project provides a robust, cryptographically secure password generator CLI utility written in Python. It generates passwords that are suitable for high-security environments, avoiding the pitfalls of pseudo-random number generators like `random`.

## Why `secrets` over `random`?

Python's standard `random` module uses the Mersenne Twister algorithm as its core generator. It is designed for modeling and simulation, not security or cryptography. Its internal state can be deduced, making outputs predictable.

This utility uses the built-in `secrets` module, which provides access to the most secure source of randomness that your operating system provides (e.g., `/dev/urandom` on Unix-like systems, `CryptGenRandom()` on Windows). Using `secrets` ensures that the generated passwords cannot be easily predicted or bruteforced based on the generator's state.

## Features

- **Cryptographically Secure:** Uses `secrets.choice` and `secrets.SystemRandom().shuffle()` for secure character selection and scrambling.
- **Customizable Complexity:** Toggle uppercase letters, numbers, and symbols.
- **Guaranteed Character Sets:** Ensures that at least one character from each selected pool is present in the final password.

## Usage

You can run the script directly via command line:

```bash
# Generate a default 12-character password including lower, upper, numbers, and symbols
python3 password_generator.py

# Generate a 20-character password
python3 password_generator.py -l 20

# Generate a 16-character password with no symbols
python3 password_generator.py -l 16 --no-symbols

# Generate an 8-character password with lowercase letters and numbers only
python3 password_generator.py -l 8 --no-upper --no-symbols
```

## Testing

To run the test suite:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
