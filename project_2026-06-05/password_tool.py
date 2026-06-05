import secrets
import string

def generate_password(length=16):
    """
    Generates a secure, random password of a given length.
    Ensures the password contains at least one lowercase letter, one uppercase letter,
    one digit, and one special character.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
            return password

def check_strength(password):
    """
    Evaluates the strength of a password and returns a score from 0 to 4,
    along with a descriptive string.
    """
    score = 0
    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    descriptions = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong"
    }

    return score, descriptions[score]

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="A secure password generator and strength checker.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate a new password")
    gen_parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")

    # Check command
    check_parser = subparsers.add_parser("check", help="Check the strength of a password")
    check_parser.add_argument("password", type=str, help="The password to check")

    args = parser.parse_args()

    if args.command == "generate":
        try:
            pwd = generate_password(args.length)
            print(f"Generated Password: {pwd}")
            score, desc = check_strength(pwd)
            print(f"Strength: {desc} ({score}/4)")
        except ValueError as e:
            print(f"Error: {e}")
    elif args.command == "check":
        score, desc = check_strength(args.password)
        print(f"Password Strength: {desc} ({score}/4)")
    else:
        parser.print_help()
