# Daily Project - 2026-06-02

## Overview

Today's project is a **Cryptographically Secure Token Generator**, built in Python using the built-in `secrets` module.

It provides utility functions and a command-line interface to generate different types of secure tokens:
- Hexadecimal tokens
- URL-safe base64 tokens
- Raw byte tokens

## Usage

You can use the token generator via the command line. The tool defaults to producing a 32-byte URL-safe token.

```bash
# Generate a default URL-safe token (32 bytes)
python3 token_generator.py

# Generate a hex token using 16 bytes
python3 token_generator.py --type hex --bytes 16

# Generate a urlsafe token using 64 bytes
python3 token_generator.py --type urlsafe --bytes 64

# Generate a bytes token (printed as hex in CLI for readability)
python3 token_generator.py --type bytes --bytes 24
```

## Testing

Unit tests are included and can be run with the following command:

```bash
PYTHONPATH=project_2026-06-02 python3 -m unittest project_2026-06-02/test_token_generator.py
```
