import string
import secrets
import argparse
import sys

def generate_password(length: int, use_upper: bool, use_lower: bool, use_numbers: bool, use_special: bool) -> str:
    """
    Generate a cryptographically secure random password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    if not any([use_upper, use_lower, use_numbers, use_special]):
        raise ValueError("At least one character type must be selected")

    char_pool = []
    password_chars = []

    if use_upper:
        pool = list(string.ascii_uppercase)
        char_pool.extend(pool)
        password_chars.append(secrets.choice(pool))

    if use_lower:
        pool = list(string.ascii_lowercase)
        char_pool.extend(pool)
        password_chars.append(secrets.choice(pool))

    if use_numbers:
        pool = list(string.digits)
        char_pool.extend(pool)
        password_chars.append(secrets.choice(pool))

    if use_special:
        pool = list(string.punctuation)
        char_pool.extend(pool)
        password_chars.append(secrets.choice(pool))

    if len(password_chars) > length:
        # If length is smaller than number of requested character types,
        # shuffle and truncate.
        secrets.SystemRandom().shuffle(password_chars)
        password_chars = password_chars[:length]
    else:
        # Fill the rest of the password length with random characters from the pool
        remaining_length = length - len(password_chars)
        password_chars.extend([secrets.choice(char_pool) for _ in range(remaining_length)])

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)

def main():
    parser = argparse.ArgumentParser(description="Generate a cryptographically secure random password.")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-numbers", action="store_true", help="Exclude numbers")
    parser.add_argument("--no-special", action="store_true", help="Exclude special characters")

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_upper=not args.no_upper,
            use_lower=not args.no_lower,
            use_numbers=not args.no_numbers,
            use_special=not args.no_special
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
