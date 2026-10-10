import string
import secrets

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Default is 12. Must be > 0.
        use_uppercase (bool): Include uppercase letters.
        use_lowercase (bool): Include lowercase letters.
        use_digits (bool): Include digits.
        use_special (bool): Include special characters.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length is less than or equal to 0, or if no character sets are selected.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    char_pool = []
    required_chars = []

    if use_uppercase:
        char_pool.extend(list(string.ascii_uppercase))
        required_chars.append(secrets.choice(string.ascii_uppercase))

    if use_lowercase:
        char_pool.extend(list(string.ascii_lowercase))
        required_chars.append(secrets.choice(string.ascii_lowercase))

    if use_digits:
        char_pool.extend(list(string.digits))
        required_chars.append(secrets.choice(string.digits))

    if use_special:
        # Use a safe subset of special characters
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        char_pool.extend(list(special_chars))
        required_chars.append(secrets.choice(special_chars))

    if not char_pool:
        raise ValueError("At least one character set must be selected.")

    if length < len(required_chars):
        raise ValueError(f"Password length ({length}) must be at least the number of selected character sets ({len(required_chars)}).")

    # Generate the remaining characters
    remaining_length = length - len(required_chars)
    password_chars = required_chars + [secrets.choice(char_pool) for _ in range(remaining_length)]

    # Shuffle the characters to ensure randomness
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)
