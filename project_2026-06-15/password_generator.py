import secrets
import string
import argparse

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

    # Ensure at least one character from each selected category is included (if length allows)
    # To keep it truly random, we just sample from the entire alphabet.
    # For a simple utility, this is usually sufficient, but we can do a naive check if needed.
    # We will stick to simple sampling from the combined alphabet.

    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Cryptographically Secure Password Generator")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-special", action="store_true", help="Exclude special characters")

    args = parser.parse_args()

    try:
        pwd = generate_password(
            length=args.length,
            use_uppercase=not args.no_uppercase,
            use_digits=not args.no_digits,
            use_special=not args.no_special
        )
        print(pwd)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
