import string
import secrets
import argparse

def generate_password(length: int = 16, include_uppercase: bool = True, include_numbers: bool = True, include_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Minimum is 4.
        include_uppercase (bool): Whether to include uppercase letters.
        include_numbers (bool): Whether to include numbers.
        include_symbols (bool): Whether to include symbols.

    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    symbols = string.punctuation if include_symbols else ""

    all_characters = lowercase + uppercase + numbers + symbols

    if not all_characters:
        raise ValueError("At least one character set must be enabled.")

    # Ensure at least one character from each enabled set is included
    password = []
    password.append(secrets.choice(lowercase))
    if include_uppercase:
        password.append(secrets.choice(uppercase))
    if include_numbers:
        password.append(secrets.choice(numbers))
    if include_symbols:
        password.append(secrets.choice(symbols))

    # Fill the rest of the password
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(secrets.choice(all_characters))

    # Cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password)

def main():
    parser = argparse.ArgumentParser(description="Generate a cryptographically secure random password.")
    parser.add_argument("-l", "--length", type=int, default=16, help="The length of the password. Default is 16. Minimum is 4.")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters.")
    parser.add_argument("--no-numbers", action="store_true", help="Exclude numbers.")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols.")

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            include_uppercase=not args.no_uppercase,
            include_numbers=not args.no_numbers,
            include_symbols=not args.no_symbols
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
