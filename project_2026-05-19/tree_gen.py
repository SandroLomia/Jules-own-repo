import os
import argparse

def generate_tree(dir_path, prefix="", max_depth=None, current_depth=0, ignore_dirs=None):
    if ignore_dirs is None:
        ignore_dirs = []

    # If max depth is exceeded, stop traversing
    if max_depth is not None and current_depth > max_depth:
        return ""

    try:
        entries = os.listdir(dir_path)
    except PermissionError:
        return prefix + "├── [Permission Denied]\n"

    # Filter entries
    filtered_entries = [
        e for e in entries if e not in ignore_dirs and not e.startswith('.') # ignore hidden by default to keep it clean
    ]
    # Sort directories first, then files
    def get_sort_key(entry):
        return (not os.path.isdir(os.path.join(dir_path, entry)), entry.lower())

    filtered_entries.sort(key=get_sort_key)

    tree_str = ""
    for i, entry in enumerate(filtered_entries):
        is_last = (i == len(filtered_entries) - 1)
        connector = "└── " if is_last else "├── "
        full_path = os.path.join(dir_path, entry)

        tree_str += prefix + connector + entry + "\n"

        if os.path.isdir(full_path):
            next_prefix = prefix + ("    " if is_last else "│   ")
            tree_str += generate_tree(
                full_path,
                prefix=next_prefix,
                max_depth=max_depth,
                current_depth=current_depth + 1,
                ignore_dirs=ignore_dirs
            )

    return tree_str

def main():
    parser = argparse.ArgumentParser(description="Generate a visual directory tree structure.")
    parser.add_argument("path", nargs="?", default=".", help="The directory path to start from (default: current directory)")
    parser.add_argument("-d", "--depth", type=int, help="Maximum depth to traverse (e.g., 0 for just the current directory)")
    parser.add_argument("-i", "--ignore", nargs="+", default=["__pycache__", "node_modules", "venv", ".git"], help="Directories to ignore (default: __pycache__, node_modules, venv, .git)")

    args = parser.parse_args()

    start_path = os.path.abspath(args.path)

    if not os.path.exists(start_path) or not os.path.isdir(start_path):
        print(f"Error: Path '{start_path}' is not a valid directory.")
        return

    print(os.path.basename(start_path) or start_path)
    print(generate_tree(start_path, max_depth=args.depth, ignore_dirs=args.ignore), end="")

if __name__ == "__main__":
    main()
