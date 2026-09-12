import secrets
import string

def generate_password(length: int, use_uppercase: bool = True, use_lowercase: bool = True, use_digits: bool = True, use_special: bool = True) -> str:
    """
    Generates a secure password of a given length using cryptographically secure random numbers.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    if not (use_uppercase or use_lowercase or use_digits or use_special):
        raise ValueError("At least one character type must be selected.")

    char_pool = ""
    password = []

    if use_uppercase:
        char_pool += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        char_pool += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        char_pool += string.digits
        password.append(secrets.choice(string.digits))
    if use_special:
        char_pool += string.punctuation
        password.append(secrets.choice(string.punctuation))

    # If the requested length is smaller than the number of active character types,
    # we cannot guarantee all requested types are included. We will raise an error.
    if length < len(password):
        raise ValueError("Password length is too small to include all selected character types.")

    # Fill the rest of the password length
    while len(password) < length:
        password.append(secrets.choice(char_pool))

    # Cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password)
