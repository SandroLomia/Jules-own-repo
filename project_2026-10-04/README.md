# Daily Project - 2026-10-04

## Secure Password Generator

This project is a utility tool that securely generates passwords with configurable requirements. It is built using Python's `secrets` module, which provides cryptographically secure random values suitable for managing data such as passwords, account authentication, security tokens, and related secrets. This is in contrast to the `random` module, which is designed for modeling and simulation, not security or cryptography. The shuffling is done securely using `secrets.SystemRandom().shuffle()`.

### Features

- Configurable password length (defaults to 12).
- Options to include or exclude uppercase letters, numbers, and symbols.
- Guarantees at least one character of each requested type is included (if length permits).
- Cryptographically secure generation.

### How to Run

To run the password generator and see some example outputs:

```bash
python3 password_generator.py
```

### Running Tests

To run the unit tests, execute the following command from the root of the repository:

```bash
PYTHONPATH=project_2026-10-04 python3 -m unittest project_2026-10-04/test_password_generator.py
```
