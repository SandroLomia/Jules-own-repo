# Daily Project - 2026-08-27: SecurePass CLI

## Overview

SecurePass CLI is a Python-based utility tool built to address a common and critical security need: generating cryptographically secure passwords and accurately evaluating password strength.

### What
A command-line interface (CLI) application with two main features:
1.  **Generate**: Creates highly secure, customizable random passwords utilizing Python's cryptographically secure `secrets` module, including `secrets.SystemRandom().shuffle()`.
2.  **Evaluate**: Analyzes a given password based on entropy to calculate a strength score and provide actionable feedback.

### Why
Many existing password generators rely on the standard `random` module, which is unsuitable for security purposes. Generating secure passwords is a fundamental requirement in modern development. By implementing this utility, the repository gains a practical, reusable, and secure tool that adheres to cryptographic best practices.

### How
-   **Core Logic (`securepass.py`)**: Uses `secrets.choice()` for secure random character selection and `secrets.SystemRandom().shuffle()` for secure shuffling of characters. The evaluation logic computes Shannon entropy based on the length and character sets used in the password.
-   **CLI Interface (`cli.py`)**: Built with Python's standard `argparse` library to provide intuitive subcommands (`generate`, `evaluate`) and flags (e.g., `-l`, `--no-special`).
-   **Testing (`test_securepass.py`)**: Comprehensive unit tests cover generation constraints (length, character inclusion/exclusion), invalid inputs, and strength evaluation boundaries.

## Usage

Run the CLI utility using Python:

```bash
# Generate a default 16-character secure password
python3 cli.py generate

# Generate an 8-character password without special characters
python3 cli.py generate -l 8 --no-special

# Evaluate the strength of a specific password
python3 cli.py evaluate "mySup3rS3cr3tP@ssw0rd!"
```
