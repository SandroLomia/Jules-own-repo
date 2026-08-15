import string
import secrets

def generate_password(length: int = 12, use_uppercase: bool = True, use_numbers: bool = True, use_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Defaults to 12.
        use_uppercase (bool): Include uppercase letters. Defaults to True.
        use_numbers (bool): Include numbers. Defaults to True.
        use_symbols (bool): Include symbols. Defaults to True.

    Returns:
        str: The generated password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    characters = list(string.ascii_lowercase)
    password_chars = []

    # Guarantee at least one character from each selected set
    password_chars.append(secrets.choice(string.ascii_lowercase))

    if use_uppercase:
        characters.extend(list(string.ascii_uppercase))
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_numbers:
        characters.extend(list(string.digits))
        password_chars.append(secrets.choice(string.digits))
    if use_symbols:
        characters.extend(list(string.punctuation))
        password_chars.append(secrets.choice(string.punctuation))

    if length < len(password_chars):
        # If length is too small to guarantee all requested types, fall back to pure random
        password_chars = [secrets.choice(characters) for _ in range(length)]
    else:
        # Fill the remaining length
        remaining_length = length - len(password_chars)
        for _ in range(remaining_length):
            password_chars.append(secrets.choice(characters))

    # Securely shuffle the list of characters
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)
