import secrets
import string
import argparse

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    """
    Generates a cryptographically secure random password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Build the pool of allowed characters and ensure at least one from each selected set
    pool = lowercase
    password_chars = [secrets.choice(lowercase)]

    if include_uppercase:
        pool += uppercase
        password_chars.append(secrets.choice(uppercase))
    if include_numbers:
        pool += numbers
        password_chars.append(secrets.choice(numbers))
    if include_symbols:
        pool += symbols
        password_chars.append(secrets.choice(symbols))

    # If requested length is smaller than the required chars, raise an error or adjust
    # Here, we'll truncate if someone asked for a length shorter than the number of active sets
    # However, for a generic secure generator, typically we want length >= sum(active sets)
    if length < len(password_chars):
        raise ValueError(f"Password length ({length}) is too short to satisfy all character set constraints ({len(password_chars)}).")

    # Fill the remaining length with random choices from the combined pool
    remaining_length = length - len(password_chars)
    password_chars.extend(secrets.choice(pool) for _ in range(remaining_length))

    # Cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

def main():
    parser = argparse.ArgumentParser(description="Cryptographically Secure Password Generator")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-numbers", action="store_true", help="Exclude numbers")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")

    args = parser.parse_args()

    try:
        pwd = generate_password(
            length=args.length,
            include_uppercase=not args.no_upper,
            include_numbers=not args.no_numbers,
            include_symbols=not args.no_symbols
        )
        print(pwd)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
