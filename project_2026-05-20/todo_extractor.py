import os
import re
import json
import argparse
from typing import List, Dict, Tuple

def extract_todos_from_file(filepath: str) -> Tuple[List[str], List[str]]:
    """Extracts pending and completed TODOs from a given markdown file."""
    pending = []
    completed = []

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                # Match `- [ ]` or `* [ ]`
                if re.match(r'^[-*]\s+\[ \]\s+(.+)', line):
                    pending.append(re.match(r'^[-*]\s+\[ \]\s+(.+)', line).group(1).strip())
                # Match `- [x]` or `* [X]`
                elif re.match(r'^[-*]\s+\[[xX]\]\s+(.+)', line):
                    completed.append(re.match(r'^[-*]\s+\[[xX]\]\s+(.+)', line).group(1).strip())
    except Exception as e:
        print(f"Error reading {filepath}: {e}")

    return pending, completed

def scan_directory(directory: str) -> Dict[str, Dict[str, List[str]]]:
    """Scans directory for .md files and extracts TODOs."""
    results = {}

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                pending, completed = extract_todos_from_file(filepath)

                if pending or completed:
                    results[filepath] = {
                        "pending": pending,
                        "completed": completed
                    }

    return results

def format_output(results: Dict[str, Dict[str, List[str]]], as_json: bool = False):
    """Formats and prints the extracted TODOs."""
    if as_json:
        print(json.dumps(results, indent=2))
        return

    if not results:
        print("No TODOs found.")
        return

    for filepath, todos in results.items():
        print(f"\n📁 File: {filepath}")
        print("-" * (len(filepath) + 9))

        if todos["pending"]:
            print("  ⏳ Pending:")
            for task in todos["pending"]:
                print(f"    - [ ] {task}")

        if todos["completed"]:
            print("  ✅ Completed:")
            for task in todos["completed"]:
                print(f"    - [x] {task}")

def main():
    parser = argparse.ArgumentParser(description="Extract TODOs from markdown files.")
    parser.add_argument("directory", nargs="?", default=".", help="Directory to scan (default: current directory)")
    parser.add_argument("--json", action="store_true", help="Output in JSON format")

    args = parser.parse_args()

    start_path = os.path.abspath(args.directory)

    if not os.path.exists(start_path) or not os.path.isdir(start_path):
        print(f"Error: Path '{start_path}' is not a valid directory.")
        return

    results = scan_directory(start_path)
    format_output(results, args.json)

if __name__ == "__main__":
    main()
