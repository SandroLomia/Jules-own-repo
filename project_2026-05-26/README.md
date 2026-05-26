# Daily Project - 2026-05-26

## Overview

Today's project is a command-line **File Hasher** utility. It allows you to easily calculate cryptographic hashes of files to verify their integrity or check for duplicates.

It supports multiple hashing algorithms including MD5, SHA-1, SHA-256, SHA-512, SHA3-256, and BLAKE2b.

## How to use

You can run the script from the command line, providing the path to the file you want to hash.

```bash
python file_hasher.py <path_to_file>
```

By default, it uses the SHA-256 algorithm.

### Options

*   `-a`, `--algorithm`: Specify the hashing algorithm to use.
    *   Choices: `md5`, `sha1`, `sha256`, `sha512`, `sha3_256`, `blake2b`
    *   Default: `sha256`

### Examples

Calculate the default SHA-256 hash of a file:

```bash
python file_hasher.py my_document.pdf
```

Calculate the MD5 hash of a file:

```bash
python file_hasher.py my_archive.zip -a md5
```

Calculate the BLAKE2b hash of a file:

```bash
python file_hasher.py video.mp4 --algorithm blake2b
```

## Testing

Unit tests are included in `test_file_hasher.py`. Run them using the `unittest` module:

```bash
PYTHONPATH=. python3 -m unittest test_file_hasher.py
```
