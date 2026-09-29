import secrets
import string

def generate_secure_password(length: int = 16, include_lowercase: bool = True, include_uppercase: bool = True, include_numbers: bool = True, include_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length: The desired length of the password. Minimum length is 4.
        include_lowercase: Whether to include lowercase letters.
        include_uppercase: Whether to include uppercase letters.
        include_numbers: Whether to include numbers.
        include_symbols: Whether to include symbols.

    Returns:
        A securely generated random password string.

    Raises:
        ValueError: If length is less than 4 or if no character types are selected.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    if not (include_lowercase or include_uppercase or include_numbers or include_symbols):
        raise ValueError("At least one character type must be selected.")

    password_chars = []
    available_chars = ""

    if include_lowercase:
        password_chars.append(secrets.choice(string.ascii_lowercase))
        available_chars += string.ascii_lowercase

    if include_uppercase:
        password_chars.append(secrets.choice(string.ascii_uppercase))
        available_chars += string.ascii_uppercase

    if include_numbers:
        password_chars.append(secrets.choice(string.digits))
        available_chars += string.digits

    if include_symbols:
        password_chars.append(secrets.choice(string.punctuation))
        available_chars += string.punctuation

    while len(password_chars) < length:
        password_chars.append(secrets.choice(available_chars))

    # Perform a cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)
