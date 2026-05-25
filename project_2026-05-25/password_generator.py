import argparse
import secrets
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    """
    Generates a random password based on the provided parameters.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    number_chars = string.digits
    symbol_chars = string.punctuation

    # Build the pool of allowed characters and ensure at least one of each requested type is included
    pool = lowercase_chars
    password_chars = [secrets.choice(lowercase_chars)]

    if use_uppercase:
        pool += uppercase_chars
        password_chars.append(secrets.choice(uppercase_chars))
    if use_numbers:
        pool += number_chars
        password_chars.append(secrets.choice(number_chars))
    if use_symbols:
        pool += symbol_chars
        password_chars.append(secrets.choice(symbol_chars))

    if length < len(password_chars):
        raise ValueError(f"Length must be at least {len(password_chars)} to satisfy the constraints")

    # Fill the rest of the password length with random characters from the pool
    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    # Shuffle the characters to ensure the guaranteed characters aren't always at the beginning
    # Use secrets.SystemRandom() to get cryptographically strong shuffling
    secure_random = secrets.SystemRandom()
    secure_random.shuffle(password_chars)

    return ''.join(password_chars)

def main():
    parser = argparse.ArgumentParser(description="Generate a secure random password.")
    parser.add_argument(
        "-l", "--length",
        type=int,
        default=12,
        help="Length of the password (default: 12)"
    )
    parser.add_argument(
        "--no-uppercase",
        action="store_false",
        dest="use_uppercase",
        help="Exclude uppercase letters from the password"
    )
    parser.add_argument(
        "--no-numbers",
        action="store_false",
        dest="use_numbers",
        help="Exclude numbers from the password"
    )
    parser.add_argument(
        "--no-symbols",
        action="store_false",
        dest="use_symbols",
        help="Exclude symbols from the password"
    )

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_uppercase=args.use_uppercase,
            use_numbers=args.use_numbers,
            use_symbols=args.use_symbols
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
