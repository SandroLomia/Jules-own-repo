import secrets
import string
import argparse

def generate_password(length: int = 16, use_upper: bool = True, use_lower: bool = True, use_digits: bool = True, use_symbols: bool = True) -> str:
    """
    Generate a cryptographically secure random password.
    """
    if not any([use_upper, use_lower, use_digits, use_symbols]):
        raise ValueError("At least one character type must be selected.")

    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = "".join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure password.")
    parser.add_argument("--length", type=int, default=16, help="Length of the password.")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters.")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters.")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits.")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols.")

    args = parser.parse_args()

    use_upper = not args.no_upper
    use_lower = not args.no_lower
    use_digits = not args.no_digits
    use_symbols = not args.no_symbols

    try:
        password = generate_password(
            length=args.length,
            use_upper=use_upper,
            use_lower=use_lower,
            use_digits=use_digits,
            use_symbols=use_symbols
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
