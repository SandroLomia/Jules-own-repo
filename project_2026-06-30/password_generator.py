import argparse
import secrets
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_special=True):
    if not any([use_uppercase, use_lowercase, use_numbers, use_special]):
        raise ValueError("At least one character set must be selected.")
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    character_pool = ""
    guaranteed_chars = []

    if use_uppercase:
        character_pool += string.ascii_uppercase
        guaranteed_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        character_pool += string.ascii_lowercase
        guaranteed_chars.append(secrets.choice(string.ascii_lowercase))
    if use_numbers:
        character_pool += string.digits
        guaranteed_chars.append(secrets.choice(string.digits))
    if use_special:
        character_pool += string.punctuation
        guaranteed_chars.append(secrets.choice(string.punctuation))

    if length < len(guaranteed_chars):
        raise ValueError(f"Password length must be at least {len(guaranteed_chars)} to satisfy all character set requirements.")

    # Fill the rest of the password length
    remaining_length = length - len(guaranteed_chars)
    password_chars = guaranteed_chars + [secrets.choice(character_pool) for _ in range(remaining_length)]

    # Shuffle the characters using secrets.SystemRandom()
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

def main():
    parser = argparse.ArgumentParser(description="Generate a cryptographically secure random password.")
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of the password (default: 12)")
    parser.add_argument("--no-upper", action="store_true", help="Do not include uppercase letters")
    parser.add_argument("--no-lower", action="store_true", help="Do not include lowercase letters")
    parser.add_argument("--no-numbers", action="store_true", help="Do not include numbers")
    parser.add_argument("--no-special", action="store_true", help="Do not include special characters")

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
