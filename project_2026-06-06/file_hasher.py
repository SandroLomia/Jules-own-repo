import hashlib
import os

def calculate_hash(file_path, algorithm='sha256', chunk_size=8192):
    """
    Calculates the hash of a file using the specified algorithm.

    Args:
        file_path (str): The path to the file.
        algorithm (str): The hashing algorithm to use (md5, sha1, sha256). Defaults to sha256.
        chunk_size (int): The size of chunks to read from the file. Defaults to 8192.

    Returns:
        str: The hexadecimal hash of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the specified algorithm is not supported.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    algorithm = algorithm.lower()
    if algorithm == 'md5':
        hasher = hashlib.md5()
    elif algorithm == 'sha1':
        hasher = hashlib.sha1()
    elif algorithm == 'sha256':
        hasher = hashlib.sha256()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}. Supported: md5, sha1, sha256")

    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            hasher.update(chunk)

    return hasher.hexdigest()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="Calculate file hashes.")
    parser.add_argument("file", help="The file to hash")
    parser.add_argument("-a", "--algorithm", choices=['md5', 'sha1', 'sha256'], default='sha256', help="Hashing algorithm")

    args = parser.parse_args()

    try:
        file_hash = calculate_hash(args.file, args.algorithm)
        print(f"{args.algorithm.upper()} hash of {args.file}:")
        print(file_hash)
    except Exception as e:
        print(f"Error: {e}")
