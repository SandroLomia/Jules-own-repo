# Daily Project - 2026-07-28

## Overview

Today's project is a cryptographically secure **Password Generator** built in Python.

Unlike generators that rely on the standard `random` module, this utility uses Python's built-in `secrets` module. This ensures that the generated passwords are suitable for security-sensitive applications, as the underlying random number generator is provided by the operating system's most secure sources.

## Features

* **Cryptographically Secure:** Powered by the `secrets` module.
* **Customizable Length:** Generate passwords of any valid length (default: 12).
* **Configurable Character Sets:** Toggle the inclusion of uppercase letters, lowercase letters, digits, and special symbols.
* **Guaranteed Complexity:** The algorithm ensures that if a character type is enabled, at least one character of that type will be present in the final password.

## Usage

You can use the `generate_password` function directly in your Python scripts:

```python
from password_generator import generate_password

# Generate a default password (length 12, all character types)
secure_password = generate_password()
print(secure_password)

# Generate a 24-character alphanumeric password (no symbols)
long_alnum_password = generate_password(length=24, use_symbols=False)
print(long_alnum_password)
```

## Testing

Comprehensive unit tests are provided in `test_password_generator.py`. To run the tests from the repository root, execute:

```bash
PYTHONPATH=project_2026-07-28 python3 -m unittest project_2026-07-28/test_password_generator.py
```
