import secrets
from typing import Dict, List

def generate_pairs(names: List[str]) -> Dict[str, str]:
    """
    Generate Secret Santa pairs from a list of names.
    Returns a dictionary mapping the giver to the receiver.
    Guarantees no one is assigned to themselves.
    Raises ValueError if there are fewer than 2 names or if there are duplicates.
    """
    if len(names) < 2:
        raise ValueError("At least 2 names are required for Secret Santa.")

    if len(set(names)) != len(names):
        raise ValueError("All names must be unique.")

    shuffled_names = list(names)
    # Use cryptographically secure shuffle as per best practices
    secrets.SystemRandom().shuffle(shuffled_names)

    pairs = {}
    for i in range(len(shuffled_names)):
        giver = shuffled_names[i]
        receiver = shuffled_names[(i + 1) % len(shuffled_names)]
        pairs[giver] = receiver

    return pairs
