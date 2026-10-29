import secrets
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): Length of the password to generate. Must be at least 1.
        use_uppercase (bool): Whether to include uppercase letters.
        use_lowercase (bool): Whether to include lowercase letters.
        use_digits (bool): Whether to include digits.
        use_special (bool): Whether to include special characters.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length is less than 1 or if no character sets are selected.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    if not any([use_uppercase, use_lowercase, use_digits, use_special]):
        raise ValueError("At least one character set must be selected")

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = "".join(secrets.choice(characters) for i in range(length))
    return password
