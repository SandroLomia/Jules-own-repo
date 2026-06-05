# Daily Project - 2026-06-05: Secure Password Tool

## Overview

Today's project is a **Secure Password Generator and Strength Checker** built entirely in Python.
It uses the cryptographically secure `secrets` module instead of the standard `random` module to ensure that the generated passwords are safe for security-sensitive applications.

## Features

- **Secure Password Generation:** Generates passwords of customizable lengths that are guaranteed to include at least one lowercase letter, one uppercase letter, one digit, and one special character.
- **Password Strength Evaluation:** Assesses a given password based on length and character variety, assigning a score from 0 to 4 with descriptive ratings ("Very Weak" to "Strong").
- **Command Line Interface (CLI):** Easy to use from the terminal for generating passwords on the fly or checking the strength of existing ones.

## Usage

You can use the tool via the command line:

### 1. Generate a Password

To generate a new password (default length is 16):
```bash
python3 password_tool.py generate
```

To specify a custom length:
```bash
python3 password_tool.py generate -l 24
```

### 2. Check Password Strength

To evaluate the strength of an existing password:
```bash
python3 password_tool.py check "YourPasswordHere!"
```

## Testing

Unit tests are included to verify functionality. To run the tests from the repository root:
```bash
PYTHONPATH=project_2026-06-05 python3 -m unittest project_2026-06-05/test_password_tool.py
```
