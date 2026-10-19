# Daily Project - 2026-10-19: Secure Password Generator

## Overview

Today's project is a **Secure Password Generator** built in Python.

### What
A Python utility that generates highly customizable passwords of variable length. It supports enforcing or excluding uppercase letters, numbers, and symbols.

### Why
Generating strong, unpredictable passwords is a common and important task. To ensure cryptographic security, this project intentionally uses Python's `secrets` module instead of the standard `random` module. The `secrets` module uses the most secure source of randomness that the operating system provides (e.g., `/dev/urandom` on Unix), making it suitable for generating passwords and security tokens.

### How
The core function `generate_password` allows users to specify the desired length and character sets. It guarantees that at least one character from each requested set is included, then fills the remaining length randomly. Finally, it uses `secrets.SystemRandom().shuffle()` to securely randomize the order of the characters.

## How to Run

To run the password generator script directly:
```bash
python3 password_generator.py
```

To run the unit tests:
```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
