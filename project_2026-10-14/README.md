# Daily Project - 2026-10-14

## Overview

Today's project is a cryptographically secure random password generator implemented in Python. It utilizes the built-in `secrets` module to generate secure strings, ensuring the generated passwords are safe for security-sensitive applications.

## Usage

You can run the generator directly to see some examples:

```bash
python3 password_generator.py
```

## Testing

Unit tests are included to verify the length and content of the generated passwords. Run the tests with:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
