import argparse
import sys
import os
from tree_generator import generate_tree

def main():
    parser = argparse.ArgumentParser(description="Directory Tree Generator CLI")
    parser.add_argument("--path", type=str, default=".", help="The path to the directory to generate the tree for. Defaults to current directory.")
    parser.add_argument("--depth", type=int, default=-1, help="The maximum depth to traverse. Defaults to unlimited.")
    parser.add_argument("--exclude", type=str, nargs='*', help="Directories or files to exclude.")
    parser.add_argument("--output", type=str, help="Output file to write the tree to. If not provided, prints to console.")

    args = parser.parse_args()

    try:
        tree_output = generate_tree(args.path, depth=args.depth, exclude=args.exclude)

        if args.output:
            with open(args.output, 'w') as f:
                f.write(tree_output)
                f.write('\n')
            print(f"Tree structure written to {args.output}")
        else:
            print(tree_output)

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
