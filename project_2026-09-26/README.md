# Daily Project - 2026-09-26

## Overview

Today's project is a secure password generator and strength evaluator utility written in Python. It provides a way to generate cryptographically secure passwords based on customizable criteria (length, uppercase letters, numbers, and special characters) using Python's `secrets` module. It also includes a strength evaluator that scores passwords from 0 to 4 based on their length and complexity.

## Features

- **Secure Generation:** Uses the `secrets` module (specifically `secrets.choice` and `secrets.SystemRandom().shuffle`) instead of the insecure `random` module.
- **Customizable:** Allows specifying the length and which character sets to include (uppercase, numbers, special characters).
- **Strength Evaluation:** Simple heuristic-based strength scoring (0-4).

## How to run tests

To execute the unit tests for this utility, run the following command from the repository root:

```bash
PYTHONPATH=project_2026-09-26 python3 -m unittest project_2026-09-26/test_password_utils.py
```
