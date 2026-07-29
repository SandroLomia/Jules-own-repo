# Secure Generator

A simple Python utility providing cryptographically secure random string generation functions.

## Features

- **`generate_password`**: Generates a secure, randomized password containing a mix of lowercase, uppercase, digits, and symbol characters. Character pools and length are highly customizable. Uses `secrets.SystemRandom().shuffle()` to guarantee a cryptographically secure character distribution instead of relying on the predictable `random` module.
- **`generate_token`**: Generates a secure URL-safe token (useful for API keys, session IDs, etc.), wrapping `secrets.token_urlsafe()`.

## Usage

```python
from secure_generator import generate_password, generate_token

# Generate a 16-character complex password
password = generate_password()
print(f"Secure Password: {password}")

# Generate a 24-character password without symbols
easy_type_password = generate_password(length=24, use_symbols=False)
print(f"No-symbol Password: {easy_type_password}")

# Generate a URL-safe token (32 bytes of entropy)
token = generate_token(length=32)
print(f"Secure Token: {token}")
```

## Testing

Run the included unit tests using:

```bash
PYTHONPATH=. python3 -m unittest test_secure_generator.py
```
