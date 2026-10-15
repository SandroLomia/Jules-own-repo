import secrets
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_numbers=True, use_symbols=True):
    """
    Generates a cryptographically secure password using Python's secrets module.

    Args:
        length (int): The length of the generated password.
        use_lowercase (bool): Whether to include lowercase letters.
        use_uppercase (bool): Whether to include uppercase letters.
        use_numbers (bool): Whether to include numbers.
        use_symbols (bool): Whether to include symbols.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length is less than or equal to 0, or if no character sets are selected.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0")

    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    return ''.join(secrets.choice(characters) for i in range(length))
