import argparse
import secrets
import string

def generate_password(length: int = 12, include_uppercase: bool = True, include_lowercase: bool = True, include_digits: bool = True, include_special: bool = True) -> str:
    """
    Generate a cryptographically secure random password.

    Args:
        length (int): Total length of the generated password (minimum 4 to accommodate all character types).
        include_uppercase (bool): Whether to include uppercase letters.
        include_lowercase (bool): Whether to include lowercase letters.
        include_digits (bool): Whether to include digits.
        include_special (bool): Whether to include special characters.

    Returns:
        str: The generated password.
    """
    if not (include_uppercase or include_lowercase or include_digits or include_special):
        raise ValueError("At least one character type must be selected.")

    # Build the pool of allowed characters and ensure at least one of each requested type is present
    pool = ""
    password_chars = []

    if include_uppercase:
        pool += string.ascii_uppercase
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if include_lowercase:
        pool += string.ascii_lowercase
        password_chars.append(secrets.choice(string.ascii_lowercase))
    if include_digits:
        pool += string.digits
        password_chars.append(secrets.choice(string.digits))
    if include_special:
        pool += string.punctuation
        password_chars.append(secrets.choice(string.punctuation))

    if length < len(password_chars):
        raise ValueError(f"Password length must be at least {len(password_chars)} based on selected options.")

    # Fill the rest of the password length with random characters from the combined pool
    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    # Cryptographically secure shuffle of the selected characters
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a cryptographically secure random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("--no-upper", action="store_true", help="Do NOT include uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Do NOT include lowercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Do NOT include digits")
    parser.add_argument("--no-special", action="store_true", help="Do NOT include special characters")

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            include_uppercase=not args.no_upper,
            include_lowercase=not args.no_lower,
            include_digits=not args.no_digits,
            include_special=not args.no_special
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}")
