def levenshtein_distance(s1: str, s2: str) -> int:
    """
    Calculates the Levenshtein distance between two strings.
    The Levenshtein distance is the minimum number of single-character edits
    (insertions, deletions, or substitutions) required to change one word into the other.
    """
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)

    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def fuzzy_search(query: str, items: list[str], threshold: int = 2) -> list[str]:
    """
    Performs a fuzzy search on a list of items using the Levenshtein distance.
    Returns a list of items that match the query within the given threshold.
    """
    results = []
    for item in items:
        # Allow case-insensitive matching by converting both to lower case for comparison
        dist = levenshtein_distance(query.lower(), item.lower())
        if dist <= threshold:
            results.append((item, dist))

    # Sort results by distance
    results.sort(key=lambda x: x[1])
    return [item for item, _ in results]
