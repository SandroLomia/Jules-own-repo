# Daily Project - 2026-07-20

## Overview

Today's project is a **Secure Password Generator and Analyzer CLI**.

It allows users to generate cryptographically secure passwords from the command line, with options to specify length and character sets. It also features a password strength analyzer that evaluates a given password and rates it as Weak, Medium, or Strong based on its complexity and length.

### Features
*   Cryptographically secure password generation using Python's `secrets` module.
*   Customizable password length and character inclusions/exclusions.
*   Password strength analysis.

### Usage

**Generate a Password:**

By default, it generates a 16-character password including uppercase, lowercase, numbers, and symbols:

```bash
python3 cli.py generate
```

You can customize the generation:

```bash
python3 cli.py generate -l 24 --no-symbols
```

**Analyze a Password:**

```bash
python3 cli.py analyze "MySuperSecretPassw0rd!"
```
