# Daily Project - 2026-06-16

## Overview

Today, I built a **Time-based One-Time Password (TOTP) Generator** from scratch in Python.

This utility implements the TOTP algorithm defined in [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238) and the underlying HOTP algorithm from [RFC 4226](https://datatracker.ietf.org/doc/html/rfc4226). It demonstrates how 2FA (Two-Factor Authentication) apps like Google Authenticator or Authy generate the 6-digit codes used for logging into secure services.

## Why I Built This

I chose to implement this from scratch to deep dive into cryptographic standards. Understanding how `hmac` (Hash-based Message Authentication Code), `struct` (binary data packing/unpacking), and time-based rolling windows work together provides valuable insight into the mechanics of modern authentication systems. Instead of relying on a third-party library like `pyotp`, building it natively ensures zero dependencies and full control over the process.

## How It Works

The TOTP generator works by taking a shared secret (encoded in Base32) and the current Unix timestamp to generate a dynamic code.

1.  **Time Window:** The current timestamp is divided by the time interval (default 30 seconds) to create a rolling counter.
2.  **HMAC-SHA1:** An HMAC-SHA1 hash is generated using the decoded secret key and the 8-byte big-endian representation of the counter.
3.  **Dynamic Truncation:** The algorithm extracts a 4-byte dynamic binary code from the HMAC hash using an offset derived from the last nibble of the hash.
4.  **Formatting:** The integer value of the 4-byte code is taken modulo $10^{\text{digits}}$ (usually $10^6$ for a 6-digit code) and zero-padded to return the final string.

## Usage

You can run the script to see a generated secret and its corresponding TOTP code:

```bash
python3 totp.py
```

### Running Tests

The test suite validates the implementation against the official test vectors provided in RFC 6238 Appendix B. To run the tests:

```bash
PYTHONPATH=. python3 -m unittest test_totp.py
```
