import string
import secrets

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    """
    Generate a secure random password.

    Args:
        length (int): Length of the password. Default is 12.
        include_uppercase (bool): Include uppercase letters. Default is True.
        include_numbers (bool): Include numbers. Default is True.
        include_symbols (bool): Include symbols. Default is True.

    Returns:
        str: The generated password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Always include lowercase letters
    characters = string.ascii_lowercase
    required_chars = [secrets.choice(string.ascii_lowercase)]

    if include_uppercase:
        characters += string.ascii_uppercase
        required_chars.append(secrets.choice(string.ascii_uppercase))

    if include_numbers:
        characters += string.digits
        required_chars.append(secrets.choice(string.digits))

    if include_symbols:
        # Use a reasonable subset of printable symbols
        symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        characters += symbols
        required_chars.append(secrets.choice(symbols))

    # If the requested length is smaller than the number of required characters,
    # we can't satisfy all constraints
    if length < len(required_chars):
        raise ValueError(f"Password length ({length}) is too short to include all requested character types ({len(required_chars)}).")

    # Fill the rest of the password length
    remaining_length = length - len(required_chars)
    password_chars = required_chars + [secrets.choice(characters) for _ in range(remaining_length)]

    # Cryptographically secure shuffle using SystemRandom
    sys_rand = secrets.SystemRandom()
    sys_rand.shuffle(password_chars)

    return "".join(password_chars)
