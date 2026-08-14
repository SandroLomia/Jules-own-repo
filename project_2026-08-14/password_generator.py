import string
import secrets

def generate_password(length=16, use_uppercase=True, use_numbers=True, use_special=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): Total length of the password. Defaults to 16.
        use_uppercase (bool): Include uppercase letters. Defaults to True.
        use_numbers (bool): Include numbers. Defaults to True.
        use_special (bool): Include special characters. Defaults to True.

    Returns:
        str: A generated password string.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    character_pool = string.ascii_lowercase
    required_characters = []

    if use_uppercase:
        character_pool += string.ascii_uppercase
        required_characters.append(secrets.choice(string.ascii_uppercase))

    if use_numbers:
        character_pool += string.digits
        required_characters.append(secrets.choice(string.digits))

    if use_special:
        character_pool += string.punctuation
        required_characters.append(secrets.choice(string.punctuation))

    if length < len(required_characters):
        raise ValueError(f"Password length ({length}) is too short to satisfy the character type requirements ({len(required_characters)}).")

    # Generate remaining characters
    remaining_length = length - len(required_characters)
    password_chars = required_characters + [secrets.choice(character_pool) for _ in range(remaining_length)]

    # Perform a cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)
