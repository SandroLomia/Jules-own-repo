import argparse
import sys
from secret_santa import generate_pairs

def main():
    parser = argparse.ArgumentParser(description="Generate secure Secret Santa pairs.")
    parser.add_argument('names', metavar='N', type=str, nargs='+',
                        help='A list of at least two unique names.')

    args = parser.parse_args()

    try:
        pairs = generate_pairs(args.names)
        print("Secret Santa Assignments:")
        print("-" * 25)
        for giver, receiver in pairs.items():
            print(f"{giver:10} ->  {receiver}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
