import secrets

def generate_passphrase(wordlist, num_words=4, separator="-"):
    """
    Generates a memorable passphrase using words from the provided wordlist.

    Args:
        wordlist (list): A list of words to choose from.
        num_words (int): The number of words to include in the passphrase. Defaults to 4.
        separator (str): The separator to use between words. Defaults to "-".

    Returns:
        str: The generated passphrase.
    """
    if not wordlist:
        raise ValueError("Wordlist cannot be empty")
    if num_words <= 0:
        raise ValueError("Number of words must be greater than 0")

    words = [secrets.choice(wordlist) for _ in range(num_words)]
    return separator.join(words)
