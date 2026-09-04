import string
import secrets
import argparse
import sys

def generate_password(length=16, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): Length of the password.
        use_upper (bool): Whether to include uppercase letters.
        use_lower (bool): Whether to include lowercase letters.
        use_numbers (bool): Whether to include numbers.
        use_symbols (bool): Whether to include symbols.

    Returns:
        str: The generated password.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one character type must be selected.")

    return ''.join(secrets.choice(chars) for _ in range(length))

def main():
    parser = argparse.ArgumentParser(description="Cryptographically secure password generator.")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    parser.add_argument("--no-upper", action="store_true", help="Do not include uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Do not include lowercase letters")
    parser.add_argument("--no-numbers", action="store_true", help="Do not include numbers")
    parser.add_argument("--no-symbols", action="store_true", help="Do not include symbols")

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_numbers=not args.no_numbers,
            use_symbols=not args.no_symbols
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
