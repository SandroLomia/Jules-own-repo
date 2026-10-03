import os
import hashlib
from collections import defaultdict
from typing import List

def get_file_hash(filepath: str, chunk_size: int = 8192) -> str:
    """Calculate the SHA-256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except OSError:
        return ""

def find_duplicates(directory: str) -> List[List[str]]:
    """
    Find duplicate files in a directory tree.
    Returns a list of lists, where each sub-list contains paths to identical files.
    """
    # Step 1: Group files by size
    size_to_files = defaultdict(list)
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            try:
                # Get actual file size (resolving symlinks if needed, though typically we just check size)
                # Ignore symlinks for duplicate finding
                if os.path.islink(filepath):
                    continue
                size = os.path.getsize(filepath)
                size_to_files[size].append(filepath)
            except OSError:
                pass

    # Step 2: For files with the same size, calculate hash and group by hash
    duplicates = []
    for size, filepaths in size_to_files.items():
        if len(filepaths) > 1:
            hash_to_files = defaultdict(list)
            for filepath in filepaths:
                file_hash = get_file_hash(filepath)
                if file_hash: # Only group if hashing was successful
                    hash_to_files[file_hash].append(filepath)

            # Step 3: Any hash with > 1 file is a duplicate
            for hash_val, dup_paths in hash_to_files.items():
                if len(dup_paths) > 1:
                    duplicates.append(dup_paths)

    return duplicates

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        target_dir = sys.argv[1]
        dups = find_duplicates(target_dir)
        if dups:
            print(f"Found {len(dups)} groups of duplicate files:")
            for i, group in enumerate(dups, 1):
                print(f"Group {i}:")
                for path in group:
                    print(f"  {path}")
        else:
            print("No duplicate files found.")
    else:
        print("Usage: python duplicate_finder.py <directory>")
