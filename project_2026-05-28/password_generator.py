import argparse
import secrets
import string

def generate_password(length=16, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generates a cryptographically secure random password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Start with lowercase letters which are always included
    alphabet = string.ascii_lowercase

    if use_uppercase:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_special:
        alphabet += string.punctuation

    if not alphabet:
        raise ValueError("At least one character set must be selected.")

    # Generate the password using secrets module for cryptographic security
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Cryptographically Secure Password Generator")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-special", action="store_true", help="Exclude special characters")

    args = parser.parse_args()

    try:
        pwd = generate_password(
            length=args.length,
            use_uppercase=not args.no_upper,
            use_digits=not args.no_digits,
            use_special=not args.no_special
        )
        print(pwd)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
