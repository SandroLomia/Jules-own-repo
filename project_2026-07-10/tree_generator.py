import os

def build_tree_nodes(dir_path, prefix='', depth=-1, current_depth=0, exclude=None):
    """
    Recursively builds the tree structure lines.
    """
    if exclude is None:
        exclude = []

    if depth != -1 and current_depth >= depth:
        return []

    try:
        entries = sorted(os.listdir(dir_path))
    except PermissionError:
        return [f"{prefix}└── [Permission Denied]"]

    entries = [e for e in entries if e not in exclude]

    lines = []
    for index, entry in enumerate(entries):
        path = os.path.join(dir_path, entry)
        is_last = index == (len(entries) - 1)

        connector = '└── ' if is_last else '├── '
        lines.append(f"{prefix}{connector}{entry}")

        if os.path.isdir(path):
            extension = '    ' if is_last else '│   '
            lines.extend(build_tree_nodes(path, prefix + extension, depth, current_depth + 1, exclude))

    return lines

def generate_tree(dir_path, depth=-1, exclude=None):
    """
    Initializes the traversal and returns the formatted tree string.
    """
    if not os.path.isdir(dir_path):
        raise ValueError(f"'{dir_path}' is not a valid directory")

    lines = [os.path.basename(os.path.abspath(dir_path))]
    lines.extend(build_tree_nodes(dir_path, depth=depth, exclude=exclude))

    return '\n'.join(lines)
