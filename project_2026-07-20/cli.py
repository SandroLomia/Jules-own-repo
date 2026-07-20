import argparse
from password_utils import generate_password, analyze_strength

def main():
    parser = argparse.ArgumentParser(description="Secure Password Generator and Analyzer CLI")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # Generate command
    gen_parser = subparsers.add_parser("generate", help="Generate a secure password")
    gen_parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    gen_parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    gen_parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    gen_parser.add_argument("--no-numbers", action="store_true", help="Exclude numbers")
    gen_parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")

    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze the strength of a password")
    analyze_parser.add_argument("password", type=str, help="The password to analyze")

    args = parser.parse_args()

    if args.command == "generate":
        try:
            password = generate_password(
                length=args.length,
                upper=not args.no_upper,
                lower=not args.no_lower,
                numbers=not args.no_numbers,
                symbols=not args.no_symbols
            )
            print(f"Generated Password: {password}")
            strength = analyze_strength(password)
            print(f"Password Strength: {strength}")
        except ValueError as e:
            print(f"Error: {e}")

    elif args.command == "analyze":
        strength = analyze_strength(args.password)
        print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
