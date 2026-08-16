import argparse
import secrets
import string
import sys

def generate_password(length=16, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): Length of the password.
        use_upper (bool): Include uppercase letters.
        use_lower (bool): Include lowercase letters.
        use_digits (bool): Include digits.
        use_special (bool): Include special characters.

    Returns:
        str: The generated password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    # Ensure at least one character from each selected category
    password_chars = []
    if use_upper:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        password_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        password_chars.append(secrets.choice(string.digits))
    if use_special:
        password_chars.append(secrets.choice(string.punctuation))

    # Fill the rest of the password
    if length < len(password_chars):
        # If length is shorter than required character types, we can't guarantee all
        # We just pick randomly from the selected ones to reach the length
        password_chars = [secrets.choice(characters) for _ in range(length)]
    else:
        remaining_length = length - len(password_chars)
        password_chars.extend([secrets.choice(characters) for _ in range(remaining_length)])

    # Perform cryptographically secure shuffle
    sys_random = secrets.SystemRandom()
    sys_random.shuffle(password_chars)

    return "".join(password_chars)

def main():
    parser = argparse.ArgumentParser(description="Generate a cryptographically secure password.")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    parser.add_argument("--no-upper", action="store_false", dest="use_upper", help="Do not include uppercase letters")
    parser.add_argument("--no-lower", action="store_false", dest="use_lower", help="Do not include lowercase letters")
    parser.add_argument("--no-digits", action="store_false", dest="use_digits", help="Do not include digits")
    parser.add_argument("--no-special", action="store_false", dest="use_special", help="Do not include special characters")

    args = parser.parse_args()

    try:
        password = generate_password(
            length=args.length,
            use_upper=args.use_upper,
            use_lower=args.use_lower,
            use_digits=args.use_digits,
            use_special=args.use_special
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
