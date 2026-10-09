# Daily Project - 2026-10-09: Secure Password Generator

## Overview

This project implements a cryptographically secure random password generator using Python's built-in `secrets` module. By leveraging the `secrets` module and `secrets.SystemRandom().shuffle()`, this utility ensures that the generated passwords are unpredictable and secure for cryptographic and security-sensitive applications, unlike the standard `random` module.

The generator supports customizing the password length and toggling the inclusion of uppercase letters, numbers, and symbols. It guarantees that at least one character of each requested type is present in the final password.

## How to Run

To run the password generator script and see an example output, navigate to the `project_2026-10-09` directory and execute:

```bash
python3 password_generator.py
```

## Running Tests

To execute the unit tests and verify the password generator's functionality, run the following command from the repository root:

```bash
PYTHONPATH=project_2026-10-09 python3 -m unittest project_2026-10-09/test_password_generator.py
```
