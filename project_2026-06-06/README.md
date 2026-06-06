# Daily Project - 2026-06-06: File Hash Calculator

## Overview

This project provides a simple command-line utility and Python module to calculate the cryptographic hash of a file. It is useful for verifying file integrity, checking for modifications, or just computing checksums.

## Features

- Supports **SHA-256** (default), **SHA-1**, and **MD5**.
- Can be used as a standalone Python script from the CLI.
- Can be imported as a module (`calculate_hash` function) in other Python projects.
- Includes comprehensive unit tests using the standard `unittest` framework.

## Usage

### Command Line

You can run the script directly from the terminal.

```bash
# Default (SHA-256)
python3 file_hasher.py /path/to/your/file.txt

# Specify an algorithm (e.g., md5)
python3 file_hasher.py /path/to/your/file.txt -a md5
python3 file_hasher.py /path/to/your/file.txt --algorithm sha1
```

### Python Module

```python
from file_hasher import calculate_hash

file_path = "example.txt"

# Default is SHA-256
sha256_hash = calculate_hash(file_path)
print(f"SHA-256: {sha256_hash}")

# Specify algorithm
md5_hash = calculate_hash(file_path, algorithm='md5')
print(f"MD5: {md5_hash}")
```

## Testing

To run the unit tests, use the following command from the repository root:

```bash
PYTHONPATH=project_2026-06-06 python3 -m unittest project_2026-06-06/test_file_hasher.py
```
