# Daily Project - 2026-06-25: Secure Password Toolkit

## Overview

This project provides a robust toolkit for handling passwords securely in Python. It consists of two main components:

1.  **`SecurePasswordGenerator`**: A class that uses Python's cryptographically secure `secrets` module to generate random passwords. It guarantees that generated passwords contain at least one character from each user-selected pool (uppercase, lowercase, digits, symbols) and employs `secrets.SystemRandom().shuffle()` to prevent predictable positional patterns.
2.  **`PasswordAnalyzer`**: A utility to evaluate the strength of a given password. It calculates the effective character pool size based on the string's composition and computes the Shannon entropy, categorizing the result from "Very Weak" to "Very Strong".

## Why This Was Built

Security is a fundamental aspect of software engineering. Often, developers rely on the standard `random` module for generating temporary passwords or tokens, which is a significant security risk because it uses a pseudo-random number generator not suitable for cryptographic purposes. This toolkit provides a drop-in, secure alternative demonstrating the proper use of the `secrets` module. Furthermore, the entropy analyzer helps visualize *why* longer passwords with varied character sets are exponentially more secure.

## Features

-   Cryptographically secure random number generation (`secrets.choice`).
-   Secure shuffling to prevent predictable structures (`secrets.SystemRandom().shuffle()`).
-   Customizable character pools (include/exclude upper, lower, digits, specific symbols).
-   Guarantees the presence of required character types in the output.
-   Calculates Shannon entropy to quantify password strength.
-   Categorizes passwords based on widely accepted entropy bits guidelines.

## Usage

```python
from password_generator import SecurePasswordGenerator
from entropy_analyzer import PasswordAnalyzer

# Generate a secure 20-character password
generator = SecurePasswordGenerator(include_symbols=True)
password = generator.generate(length=20)
print(f"Generated Password: {password}")

# Analyze its strength
analyzer = PasswordAnalyzer()
analysis = analyzer.analyze(password)
print(f"Analysis: {analysis}")
```

## Running Tests

To run the unit tests for this project, execute the following from the repository root:

```bash
PYTHONPATH=project_2026-06-25 python3 -m unittest project_2026-06-25/test_password_generator.py project_2026-06-25/test_entropy_analyzer.py
```
