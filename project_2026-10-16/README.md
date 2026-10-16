# Daily Project - 2026-10-16

## Overview

Today's project is a **Secure Password Generator and Evaluator**.

### What
A Python utility that generates cryptographically secure passwords using customizable character sets (uppercase, lowercase, digits, special characters) and a function to evaluate the strength of a given password based on length and character diversity.

### Why
To enhance the repository's suite of utility scripts with a secure, robust tool for generating passwords, utilizing Python's `secrets` module instead of the standard `random` module to ensure cryptographic security.

### How to Run

1. **Run the tests:**
   ```bash
   PYTHONPATH=project_2026-10-16 python3 -m unittest project_2026-10-16/test_password_utils.py
   ```

2. **Use in your code:**
   ```python
   from password_utils import generate_password, evaluate_strength

   # Generate a default 12-character password
   pwd = generate_password()
   print(f"Password: {pwd}")
   print(f"Strength: {evaluate_strength(pwd)}")
   ```
