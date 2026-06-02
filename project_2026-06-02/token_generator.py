import secrets

def generate_hex_token(nbytes=32):
    """
    Generates a cryptographically secure random text string, in hexadecimal.
    Each byte is converted to two hex digits.
    """
    if nbytes <= 0:
        raise ValueError("nbytes must be greater than 0.")
    return secrets.token_hex(nbytes)

def generate_urlsafe_token(nbytes=32):
    """
    Generates a cryptographically secure random URL-safe text string.
    The string is base64 encoded and safe to use in URLs.
    """
    if nbytes <= 0:
        raise ValueError("nbytes must be greater than 0.")
    return secrets.token_urlsafe(nbytes)

def generate_bytes_token(nbytes=32):
    """
    Generates a cryptographically secure random sequence of bytes.
    """
    if nbytes <= 0:
        raise ValueError("nbytes must be greater than 0.")
    return secrets.token_bytes(nbytes)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Cryptographically Secure Token Generator")
    parser.add_argument("--type", choices=['hex', 'urlsafe', 'bytes'], default='urlsafe', help="Type of token to generate")
    parser.add_argument("--bytes", type=int, default=32, help="Number of random bytes used to generate the token")

    args = parser.parse_args()

    try:
        if args.type == 'hex':
            print(generate_hex_token(args.bytes))
        elif args.type == 'urlsafe':
            print(generate_urlsafe_token(args.bytes))
        elif args.type == 'bytes':
            print(generate_bytes_token(args.bytes).hex()) # printing bytes as hex for readability in CLI
    except ValueError as e:
        print(f"Error: {e}")
