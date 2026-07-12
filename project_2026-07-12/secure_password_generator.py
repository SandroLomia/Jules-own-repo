import secrets
import string
import math

def generate_password(length=16, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """
    Generates a cryptographically secure random password.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    if not any([use_uppercase, use_lowercase, use_digits, use_symbols]):
        raise ValueError("At least one character set must be selected.")

    char_pool = ""
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    return "".join(secrets.choice(char_pool) for _ in range(length))

def calculate_entropy(password):
    """
    Calculates the entropy of a given password based on its length and character set.
    Note: This is a simplified entropy calculation that assumes all characters in
    the inferred character pool are equally likely. It infers the pool based on the
    characters present in the password.
    """
    if not password:
        return 0.0

    pool_size = 0
    if any(c in string.ascii_uppercase for c in password):
        pool_size += len(string.ascii_uppercase)
    if any(c in string.ascii_lowercase for c in password):
        pool_size += len(string.ascii_lowercase)
    if any(c in string.digits for c in password):
        pool_size += len(string.digits)
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        # Fallback if somehow there's an unseen character type
        pool_size = len(set(password))

    # E = L * log2(R) where L is length, R is pool size
    return len(password) * math.log2(pool_size)
