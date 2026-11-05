import string
import secrets

def generate_password(length: int = 12, use_uppercase: bool = True, use_lowercase: bool = True, use_digits: bool = True, use_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length: Total length of the password.
        use_uppercase: Whether to include uppercase letters.
        use_lowercase: Whether to include lowercase letters.
        use_digits: Whether to include digits.
        use_symbols: Whether to include symbols (punctuation).

    Returns:
        The generated password string.

    Raises:
        ValueError: If no character types are selected or if length is too short to satisfy requirements.
    """
    if not any([use_uppercase, use_lowercase, use_digits, use_symbols]):
        raise ValueError("At least one character type must be selected.")

    chars = []
    pool = ""

    if use_uppercase:
        chars.append(secrets.choice(string.ascii_uppercase))
        pool += string.ascii_uppercase
    if use_lowercase:
        chars.append(secrets.choice(string.ascii_lowercase))
        pool += string.ascii_lowercase
    if use_digits:
        chars.append(secrets.choice(string.digits))
        pool += string.digits
    if use_symbols:
        chars.append(secrets.choice(string.punctuation))
        pool += string.punctuation

    if length < len(chars):
        raise ValueError(f"Password length ({length}) is too short to contain all requested character types ({len(chars)}).")

    while len(chars) < length:
        chars.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)
