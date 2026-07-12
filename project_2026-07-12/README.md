# Daily Project - 2026-07-12

## Overview

Today's project is a **Secure Password Generator** utility.

It is written in Python and uses the cryptographically secure `secrets` module to generate strong, random passwords. Unlike the standard `random` module which produces pseudo-random numbers meant for simulations, `secrets` provides access to the most secure source of randomness that the operating system provides, making it suitable for generating passwords, security tokens, and related secrets.

## Features

*   **Customizable Length:** Generate passwords of any desired length.
*   **Character Set Selection:** Toggle the inclusion of uppercase letters, lowercase letters, digits, and special symbols.
*   **Entropy Calculation:** Includes a utility function to estimate the Shannon entropy of the generated password, giving an indication of its strength.

## How to Use

```python
from secure_password_generator import generate_password, calculate_entropy

# Generate a default 16-character password with all character sets
password = generate_password()
print(f"Generated Password: {password}")

# Generate a 32-character password with only alphanumeric characters
alpha_pass = generate_password(length=32, use_symbols=False)
print(f"Alphanumeric Password: {alpha_pass}")

# Calculate entropy
entropy = calculate_entropy(password)
print(f"Entropy: {entropy:.2f} bits")
```

## Running Tests

Unit tests are provided using the built-in `unittest` framework. To run the tests from the repository root, execute:

```bash
PYTHONPATH=project_2026-07-12 python3 -m unittest project_2026-07-12/test_secure_password_generator.py
```
