import secrets
import string

# A basic eff wordlist for passphrase generation (subset for demonstration, or we can use a built-in dictionary if available, but hardcoding a small subset or downloading one is better. For simplicity, we'll use a small wordlist embedded, or we can just fetch one). Let's use a small embedded wordlist for this mini-project.
WORDLIST = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam", "zucchini",
    "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india",
    "juliet", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo",
    "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu",
    "ocean", "mountain", "river", "forest", "desert", "island", "canyon", "valley",
    "planet", "star", "galaxy", "comet", "meteor", "nebula", "asteroid", "orbit",
    "science", "math", "history", "art", "music", "poetry", "drama", "fiction",
    "computer", "network", "software", "hardware", "internet", "database", "security",
    "cipher", "crypto", "encryption", "decryption", "hash", "salt", "token", "key"
]

def generate_password(length=16, use_uppercase=True, use_digits=True, use_symbols=True):
    """
    Generates a secure random password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Ensure at least one character from each selected pool if length is sufficient
    password = []
    if use_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    password.append(secrets.choice(string.ascii_lowercase))

    # Fill the rest
    while len(password) < length:
        password.append(secrets.choice(characters))

    # Shuffle the result
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def generate_passphrase(num_words=4, separator="-"):
    """
    Generates a secure passphrase using a wordlist.
    """
    if num_words < 2:
        raise ValueError("Passphrase must contain at least 2 words.")

    words = [secrets.choice(WORDLIST) for _ in range(num_words)]
    return separator.join(words)
