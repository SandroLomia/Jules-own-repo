import argparse
from generator import generate_password, generate_passphrase

def main():
    parser = argparse.ArgumentParser(description="Secure Password and Passphrase Generator")
    subparsers = parser.add_subparsers(dest="command", help="Choose what to generate")

    # Password parser
    pwd_parser = subparsers.add_parser("password", help="Generate a random password")
    pwd_parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    pwd_parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    pwd_parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    pwd_parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")

    # Passphrase parser
    phrase_parser = subparsers.add_parser("passphrase", help="Generate a random passphrase")
    phrase_parser.add_argument("-w", "--words", type=int, default=4, help="Number of words (default: 4)")
    phrase_parser.add_argument("-s", "--separator", type=str, default="-", help="Separator between words (default: '-')")

    args = parser.parse_args()

    if args.command == "password":
        try:
            pwd = generate_password(
                length=args.length,
                use_uppercase=not args.no_upper,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols
            )
            print(f"Generated Password: {pwd}")
        except ValueError as e:
            print(f"Error: {e}")

    elif args.command == "passphrase":
        try:
            phrase = generate_passphrase(
                num_words=args.words,
                separator=args.separator
            )
            print(f"Generated Passphrase: {phrase}")
        except ValueError as e:
            print(f"Error: {e}")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
