import argparse
import secrets
import string

def generate_password(length: int = 16, include_upper: bool = True, include_digits: bool = True, include_special: bool = True) -> str:
    """Generates a cryptographically secure password."""
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_upper else ""
    digits = string.digits if include_digits else ""
    special = string.punctuation if include_special else ""

    all_chars = lower + upper + digits + special
    if not all_chars:
        raise ValueError("At least one character set must be selected.")

    # Ensure at least one character from each selected set is included
    password_chars = []
    if lower:
        password_chars.append(secrets.choice(lower))
    if upper:
        password_chars.append(secrets.choice(upper))
    if digits:
        password_chars.append(secrets.choice(digits))
    if special:
        password_chars.append(secrets.choice(special))

    # Fill the rest with random choices from all allowed characters
    if length < len(password_chars):
        # We need a smaller password than the mandatory character sets
        password_chars = password_chars[:length]
    else:
        while len(password_chars) < length:
            password_chars.append(secrets.choice(all_chars))

    # Shuffle the characters to prevent predictable patterns
    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)

def main():
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-special", action="store_true", help="Exclude special characters")

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            include_upper=not args.no_upper,
            include_digits=not args.no_digits,
            include_special=not args.no_special
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
