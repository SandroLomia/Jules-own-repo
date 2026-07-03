import argparse
import secrets
import string

class SecurePasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation

    def generate(self, length=16, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")

        char_pool = ""
        required_chars = []

        if use_lower:
            char_pool += self.lowercase
            required_chars.append(secrets.choice(self.lowercase))
        if use_upper:
            char_pool += self.uppercase
            required_chars.append(secrets.choice(self.uppercase))
        if use_digits:
            char_pool += self.digits
            required_chars.append(secrets.choice(self.digits))
        if use_symbols:
            char_pool += self.symbols
            required_chars.append(secrets.choice(self.symbols))

        if not char_pool:
            raise ValueError("At least one character type must be selected.")

        if length < len(required_chars):
            raise ValueError(f"Password length must be at least {len(required_chars)} to include all selected character types.")

        # Fill the rest of the password length
        remaining_length = length - len(required_chars)
        random_chars = [secrets.choice(char_pool) for _ in range(remaining_length)]

        # Combine required and random characters
        password_chars = required_chars + random_chars

        # Shuffle cryptographically securely
        secrets.SystemRandom().shuffle(password_chars)

        return "".join(password_chars)

def main():
    parser = argparse.ArgumentParser(description="Generate a cryptographically secure random password.")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase characters")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase characters")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")

    args = parser.parse_args()

    generator = SecurePasswordGenerator()
    try:
        password = generator.generate(
            length=args.length,
            use_lower=not args.no_lower,
            use_upper=not args.no_upper,
            use_digits=not args.no_digits,
            use_symbols=not args.no_symbols
        )
        print(password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
