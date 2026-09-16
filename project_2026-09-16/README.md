# Daily Project - 2026-09-16
## Secure Password Generator

### Overview

This project implements a cryptographically secure password generator in Python. It uses the `secrets` module instead of the standard `random` module to ensure that the generated passwords are secure and suitable for cryptographic purposes.

### Features

- Configurable password length (default is 12 characters).
- Options to include or exclude uppercase letters, lowercase letters, numbers, and special characters.
- Ensures that at least one character from each selected category is included in the final password.
- Cryptographically secure generation and shuffling using `secrets.choice` and `secrets.SystemRandom().shuffle()`.

### Usage

You can use the generator by importing it into your Python project or running it directly.

```python
from password_generator import generate_password

# Generate a default 12-character password
password = generate_password()
print(password)

# Generate a 16-character password with only letters and numbers
custom_password = generate_password(length=16, use_special=False)
print(custom_password)
```

To run the script directly and print a default password:
```bash
python3 password_generator.py
```

### Testing

Unit tests are included to verify the length, character constraints, and edge cases (such as invalid lengths).

To run the tests from the root of the repository, execute:
```bash
PYTHONPATH=project_2026-09-16 python3 -m unittest project_2026-09-16/test_password_generator.py
```
