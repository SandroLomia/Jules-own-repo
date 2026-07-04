import secrets
import string
import math

def generate_password(length=16, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    if not any([include_uppercase, include_lowercase, include_digits, include_symbols]):
        raise ValueError("At least one character set must be selected.")
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    pool = ""
    required_chars = []

    if include_uppercase:
        pool += string.ascii_uppercase
        required_chars.append(secrets.choice(string.ascii_uppercase))
    if include_lowercase:
        pool += string.ascii_lowercase
        required_chars.append(secrets.choice(string.ascii_lowercase))
    if include_digits:
        pool += string.digits
        required_chars.append(secrets.choice(string.digits))
    if include_symbols:
        pool += string.punctuation
        required_chars.append(secrets.choice(string.punctuation))

    if length < len(required_chars):
        raise ValueError(f"Length must be at least {len(required_chars)} to include all selected character types.")

    password_chars = required_chars + [secrets.choice(pool) for _ in range(length - len(required_chars))]

    # Secure shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def calculate_entropy(password):
    if not password:
        return 0.0

    pool_size = 0
    if any(c in string.ascii_lowercase for c in password):
        pool_size += 26
    if any(c in string.ascii_uppercase for c in password):
        pool_size += 26
    if any(c in string.digits for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return 0.0

    entropy = len(password) * math.log2(pool_size)
    return entropy
