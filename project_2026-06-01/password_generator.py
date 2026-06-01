import secrets
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generates a cryptographically secure random password.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    character_pool = ""
    required_characters = []

    if use_lowercase:
        character_pool += string.ascii_lowercase
        required_characters.append(secrets.choice(string.ascii_lowercase))
    if use_uppercase:
        character_pool += string.ascii_uppercase
        required_characters.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        character_pool += string.digits
        required_characters.append(secrets.choice(string.digits))
    if use_special:
        character_pool += string.punctuation
        required_characters.append(secrets.choice(string.punctuation))

    if not character_pool:
        raise ValueError("At least one character set must be selected.")

    if length < len(required_characters):
        raise ValueError(f"Password length must be at least {len(required_characters)} for the selected character sets.")

    # Fill the rest of the password length
    password = required_characters
    for _ in range(length - len(required_characters)):
        password.append(secrets.choice(character_pool))

    # Shuffle the characters to ensure randomness since the first characters were predictably selected from each pool
    # The `secrets` module does not have a shuffle method, so we use SystemRandom().shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Cryptographically Secure Password Generator")
    parser.add_argument("--length", type=int, default=16, help="Length of the password to generate")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-special", action="store_true", help="Exclude special characters")

    args = parser.parse_args()

    try:
        pwd = generate_password(
            length=args.length,
            use_lowercase=not args.no_lower,
            use_uppercase=not args.no_upper,
            use_digits=not args.no_digits,
            use_special=not args.no_special
        )
        print(f"Generated Password: {pwd}")
    except ValueError as e:
        print(f"Error: {e}")
