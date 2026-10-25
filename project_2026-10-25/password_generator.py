import secrets
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_numbers=True, use_symbols=True):
    """
    Generates a secure, random password using the secrets module.

    Args:
        length (int): Length of the generated password.
        use_upper (bool): Include uppercase letters.
        use_lower (bool): Include lowercase letters.
        use_numbers (bool): Include digits.
        use_symbols (bool): Include special characters.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length <= 0 or no character types are selected.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_numbers:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    # Ensure at least one character from each selected pool is used if length is sufficient
    password_chars = []
    if use_upper and length >= len(password_chars) + 1:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower and length >= len(password_chars) + 1:
        password_chars.append(secrets.choice(string.ascii_lowercase))
    if use_numbers and length >= len(password_chars) + 1:
        password_chars.append(secrets.choice(string.digits))
    if use_symbols and length >= len(password_chars) + 1:
        password_chars.append(secrets.choice(string.punctuation))

    # Fill the rest with random characters from the combined pool
    remaining_length = length - len(password_chars)
    password_chars.extend(secrets.choice(char_pool) for _ in range(remaining_length))

    # Shuffle the characters to avoid predictable patterns
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)
