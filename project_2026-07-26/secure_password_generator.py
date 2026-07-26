import secrets
import string

def generate_password(length=16, uppercase=True, lowercase=True, numbers=True, symbols=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): Total length of the password. Minimum length must accommodate required character types.
        uppercase (bool): Include uppercase letters.
        lowercase (bool): Include lowercase letters.
        numbers (bool): Include numeric digits.
        symbols (bool): Include punctuation symbols.

    Returns:
        str: A secure random password.

    Raises:
        ValueError: If no character types are selected or if the length is too short to fulfill requirements.
    """
    char_pools = []
    required_chars = []

    if uppercase:
        char_pools.append(string.ascii_uppercase)
        required_chars.append(secrets.choice(string.ascii_uppercase))
    if lowercase:
        char_pools.append(string.ascii_lowercase)
        required_chars.append(secrets.choice(string.ascii_lowercase))
    if numbers:
        char_pools.append(string.digits)
        required_chars.append(secrets.choice(string.digits))
    if symbols:
        char_pools.append(string.punctuation)
        required_chars.append(secrets.choice(string.punctuation))

    if not char_pools:
        raise ValueError("At least one character type (uppercase, lowercase, numbers, symbols) must be selected.")

    if length < len(required_chars):
        raise ValueError(f"Password length ({length}) is too short to include all {len(required_chars)} required character types.")

    # Combine all selected pools
    full_pool = "".join(char_pools)

    # Fill the remaining length with random choices from the full pool
    remaining_length = length - len(required_chars)
    remaining_chars = [secrets.choice(full_pool) for _ in range(remaining_length)]

    # Combine and shuffle
    password_list = required_chars + remaining_chars
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)


# Default wordlist for passphrase generation (EFF long wordlist subset example style)
DEFAULT_WORDLIST = [
    "abacus", "bacon", "cabin", "daddy", "eager", "fabric", "gadget", "habit", "icebox", "jacket",
    "kangaroo", "lab", "macaroni", "napkin", "oasis", "pacify", "quail", "rabbit", "sabotage", "tabasco",
    "udder", "vaccine", "waffle", "yacht", "zebra", "apple", "banana", "cherry", "date", "elderberry"
]

def generate_passphrase(num_words=4, wordlist=None, separator="-"):
    """
    Generates a cryptographically secure random passphrase.

    Args:
        num_words (int): Number of words in the passphrase.
        wordlist (list): List of words to choose from. Defaults to a small built-in list if None.
        separator (str): The separator between words.

    Returns:
        str: A secure random passphrase.

    Raises:
        ValueError: If num_words is less than 1 or if wordlist is empty.
    """
    if num_words < 1:
        raise ValueError("Passphrase must contain at least one word.")

    if wordlist is None:
        wordlist = DEFAULT_WORDLIST

    if not wordlist:
        raise ValueError("Wordlist cannot be empty.")

    words = [secrets.choice(wordlist) for _ in range(num_words)]
    return separator.join(words)
