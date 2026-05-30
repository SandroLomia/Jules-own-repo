import secrets
import string
import argparse

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    """
    Generates a cryptographically secure random password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    character_pool = ""
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_numbers:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-numbers", action="store_true", help="Exclude numbers")
    parser.add_argument("--no-special", action="store_true", help="Exclude special characters")

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_uppercase=not args.no_upper,
            use_lowercase=not args.no_lower,
            use_numbers=not args.no_numbers,
            use_special=not args.no_special
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
