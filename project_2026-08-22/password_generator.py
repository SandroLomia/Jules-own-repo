import secrets
import string

def generate_password(length: int, use_upper: bool = True, use_lower: bool = True, use_numbers: bool = True, use_specials: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length: The length of the password.
        use_upper: Include uppercase letters.
        use_lower: Include lowercase letters.
        use_numbers: Include digits.
        use_specials: Include special characters.

    Returns:
        A randomly generated password string.

    Raises:
        ValueError: If length is less than 1, or if all character sets are disabled.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be enabled")

    return "".join(secrets.choice(characters) for _ in range(length))
