# Daily Project - 2026-08-29

## Overview

Today's project is a Cryptographically Secure Password Generator utility written in Python.

### Why
Generating secure tokens and passwords is a common requirement. Relying on the standard `random` module in Python is insecure for security-sensitive purposes. This utility leverages the built-in `secrets` module to ensure that the randomness source is cryptographically secure.

### Technical Details
- **Generator**: Uses `secrets.choice()` to pick characters and `secrets.SystemRandom().shuffle()` to securely shuffle the resulting password pool.
- **Constraints**: Enforces length and character type constraints, ensuring that if multiple character types are requested, at least one of each is guaranteed to be in the final password.
- **Testing**: Includes a comprehensive test suite using the `unittest` framework to verify exact length requirements, constraints on character types, and validation error handling.

### How to Run

1. Run the script directly to output a generated password:
   ```bash
   python3 project_2026-08-29/password_generator.py
   ```

2. Run the test suite:
   ```bash
   PYTHONPATH=project_2026-08-29 python3 -m unittest project_2026-08-29/test_password_generator.py
   ```
