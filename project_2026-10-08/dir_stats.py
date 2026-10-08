import os

def get_directory_stats(path: str) -> dict:
    """
    Recursively calculates the total size of files grouped by their extensions.

    Args:
        path (str): The root directory path to start scanning from.

    Returns:
        dict: A dictionary where keys are file extensions (e.g., '.py', '.txt')
              and values are the total size of files with that extension in bytes.
              Files without an extension are grouped under the key ''.
    """
    stats = {}

    if not os.path.exists(path):
        return stats

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            # Skip symlinks to avoid circular references or counting out-of-tree files
            if os.path.islink(file_path):
                continue

            try:
                size = os.path.getsize(file_path)
            except OSError:
                # File might have been deleted, or we lack permissions
                continue

            _, ext = os.path.splitext(file)
            ext = ext.lower()  # Normalize extensions to lowercase

            if ext not in stats:
                stats[ext] = 0
            stats[ext] += size

    return stats

if __name__ == "__main__":
    import sys

    scan_path = sys.argv[1] if len(sys.argv) > 1 else "."

    print(f"Directory Statistics for: {scan_path}")
    print("-" * 40)

    stats = get_directory_stats(scan_path)

    if not stats:
        print("No files found or directory does not exist.")
    else:
        # Sort by total size in descending order
        sorted_stats = sorted(stats.items(), key=lambda x: x[1], reverse=True)

        for ext, size in sorted_stats:
            display_ext = ext if ext else "<no extension>"
            # Format size to be more readable
            if size >= 1024**3:
                readable_size = f"{size / (1024**3):.2f} GB"
            elif size >= 1024**2:
                readable_size = f"{size / (1024**2):.2f} MB"
            elif size >= 1024:
                readable_size = f"{size / 1024:.2f} KB"
            else:
                readable_size = f"{size} bytes"

            print(f"{display_ext:15}: {readable_size:>10}")
