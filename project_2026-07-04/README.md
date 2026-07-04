# Daily Project - 2026-07-04

## Overview

Today's project is a **Secure Password Generator** utility written in Python. It is designed to generate strong, cryptographically secure passwords and calculate their Shannon entropy.

### Features
* **Cryptographically Secure:** Uses Python's `secrets` module instead of the standard `random` module to ensure high-quality randomness suitable for security applications.
* **Customizable:** Generates passwords with customizable lengths and character sets (uppercase, lowercase, digits, symbols).
* **Entropy Calculation:** Includes a function to calculate the Shannon entropy of a given password, providing a measure of its theoretical strength based on the character pool used.

## Usage

```python
from password_generator import generate_password, calculate_entropy

# Generate a default 16-character secure password
pwd = generate_password()
print(f"Generated Password: {pwd}")

# Calculate its entropy
entropy = calculate_entropy(pwd)
print(f"Entropy: {entropy:.2f} bits")

# Generate a 12-character alphanumeric password
alphanumeric_pwd = generate_password(length=12, include_symbols=False)
print(f"Alphanumeric Password: {alphanumeric_pwd}")
```

## Running Tests

To run the unit tests for this project, execute the following command from the repository root:

```bash
PYTHONPATH=project_2026-07-04 python3 -m unittest project_2026-07-04/test_password_generator.py
```
