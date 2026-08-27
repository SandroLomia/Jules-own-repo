import argparse
from securepass import generate_password, evaluate_strength

def main():
    parser = argparse.ArgumentParser(description="SecurePass: A secure password generator and strength evaluator.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Generate subcommand
    generate_parser = subparsers.add_parser("generate", help="Generate a secure password")
    generate_parser.add_argument("-l", "--length", type=int, default=16, help="Length of the password (default: 16)")
    generate_parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase letters")
    generate_parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase letters")
    generate_parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    generate_parser.add_argument("--no-special", action="store_true", help="Exclude special characters")

    # Evaluate subcommand
    evaluate_parser = subparsers.add_parser("evaluate", help="Evaluate the strength of a password")
    evaluate_parser.add_argument("password", type=str, help="The password to evaluate")

    args = parser.parse_args()

    if args.command == "generate":
        try:
            password = generate_password(
                length=args.length,
                use_upper=not args.no_upper,
                use_lower=not args.no_lower,
                use_digits=not args.no_digits,
                use_special=not args.no_special
            )
            print(f"Generated Password: {password}")

            # Optional: auto-evaluate
            strength = evaluate_strength(password)
            print(f"Strength Score: {strength['score']}/4 (Entropy: {strength['entropy']:.2f} bits)")
        except ValueError as e:
            print(f"Error: {e}")
    elif args.command == "evaluate":
        strength = evaluate_strength(args.password)
        print(f"Evaluating Password: {'*' * len(args.password)}") # Hide actual password in output
        print(f"Entropy: {strength['entropy']:.2f} bits")
        print(f"Score: {strength['score']}/4")
        print(f"Feedback: {strength['feedback']}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
