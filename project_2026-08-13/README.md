# Daily Project - 2026-08-13

## Overview

This project implements a **Secure Password Generator** in Python.

### What
A utility tool that generates highly customizable, cryptographically secure passwords. It allows users to specify the exact length and toggle the inclusion of uppercase letters, lowercase letters, digits, and symbols.

### Why
When generating sensitive random values, such as passwords or security tokens, Python's standard `random` module is insufficient as it uses a pseudo-random number generator designed for modeling and simulation, not security. I chose to build this tool to demonstrate the correct usage of the `secrets` module, which relies on the operating system's strongest cryptographic randomness source (e.g., `/dev/urandom`). It specifically showcases `secrets.choice()` for secure selection and `secrets.SystemRandom().shuffle()` for secure permutation.

### How
The core logic resides in `secure_password_generator.py`.
It ensures at least one character of each requested type is included to meet password complexity requirements. It fills the remaining requested length with random choices from the combined permitted character pool. Crucially, it then performs a cryptographic shuffle on the resulting list of characters before returning the final string.

## Running the Code

To run the example generator:
```bash
python3 secure_password_generator.py
```

To run the unit tests:
```bash
PYTHONPATH=. python3 -m unittest test_secure_password_generator.py
```