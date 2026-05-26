import hashlib
import argparse
import os
import sys

def calculate_hash(filepath, algorithm="sha256"):
    """
    Calculates the hash of a file using the specified algorithm.
    """
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    algorithm = algorithm.lower()
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

    hasher = hashlib.new(algorithm)

    # Read the file in chunks to handle large files efficiently
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)

    return hasher.hexdigest()

def main():
    parser = argparse.ArgumentParser(description="Calculate cryptographic hashes of files.")
    parser.add_argument("filepath", help="Path to the file to hash")
    parser.add_argument(
        "-a", "--algorithm",
        default="sha256",
        choices=["md5", "sha1", "sha256", "sha512", "sha3_256", "blake2b"],
        help="Hashing algorithm to use (default: sha256)"
    )

    args = parser.parse_args()

    try:
        file_hash = calculate_hash(args.filepath, args.algorithm)
        print(f"{args.algorithm.upper()} hash of '{args.filepath}':")
        print(file_hash)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
