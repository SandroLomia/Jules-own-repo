# Daily Project - 2026-06-15: Secure Password Generator

## Overview

Today I decided to build a simple, yet robust, Secure Password Generator CLI tool.

It generates highly customizable random passwords and emphasizes security by utilizing Python's built-in `secrets` module instead of the standard `random` module. The `secrets` module provides access to the most secure source of randomness that your operating system provides (e.g., `/dev/urandom` on Unix-like systems). This makes it cryptographically secure, which is essential when generating passwords, security tokens, or any sensitive data where predictability is a critical vulnerability.

## Usage

You can run the script via the command line.

**Basic Usage (generates a 16-character password including uppercase, lowercase, digits, and special characters):**

```bash
python3 password_generator.py
```

**Custom Length:**

```bash
python3 password_generator.py -l 32
```

**Exclude Character Sets:**

```bash
# Generate a password without special characters
python3 password_generator.py --no-special

# Generate an alphanumeric password
python3 password_generator.py --no-special

# Generate a password with only lowercase letters
python3 password_generator.py --no-uppercase --no-digits --no-special
```

## Testing

The project includes unit tests to verify the length and character set constraints of the generated passwords.

To run the tests:

```bash
PYTHONPATH=. python3 -m unittest test_password_generator.py
```
