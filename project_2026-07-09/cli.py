import argparse
from generator import generate_password, generate_passphrase

def main():
    parser = argparse.ArgumentParser(
        description="Secure Password and Passphrase Generator",
        epilog="Examples:\n"
               "  python cli.py password --length 20 --no-symbols\n"
               "  python cli.py passphrase --words 5 --separator _",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="command", required=True, help="Command to execute")

    # Password subparser
    pw_parser = subparsers.add_parser("password", help="Generate a random password")
    pw_parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    pw_parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    pw_parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    pw_parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    pw_parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")

    # Passphrase subparser
    pp_parser = subparsers.add_parser("passphrase", help="Generate a random passphrase")
    pp_parser.add_argument("-w", "--words", type=int, default=4, help="Number of words in the passphrase (default: 4)")
    pp_parser.add_argument("-s", "--separator", type=str, default="-", help="Separator between words (default: '-')")

    args = parser.parse_args()

    try:
        if args.command == "password":
            password = generate_password(
                length=args.length,
                use_upper=not args.no_upper,
                use_lower=not args.no_lower,
                use_digits=not args.no_digits,
                use_symbols=not args.no_symbols
            )
            print(password)
        elif args.command == "passphrase":
            passphrase = generate_passphrase(
                num_words=args.words,
                separator=args.separator
            )
            print(passphrase)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
