import secrets
import string

def generate_password(length=16, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Default is 16.
        use_uppercase (bool): Include uppercase letters. Default is True.
        use_lowercase (bool): Include lowercase letters. Default is True.
        use_digits (bool): Include digits. Default is True.
        use_special (bool): Include special characters. Default is True.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length is less than 1 or if no character types are selected.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    char_sets = []
    if use_uppercase:
        char_sets.append(string.ascii_uppercase)
    if use_lowercase:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_special:
        char_sets.append(string.punctuation)

    if not char_sets:
        raise ValueError("At least one character type must be selected.")

    all_chars = ''.join(char_sets)

    # Ensure at least one character from each selected set is included
    password = []
    for char_set in char_sets:
        password.append(secrets.choice(char_set))

    # Fill the rest of the password length
    while len(password) < length:
        password.append(secrets.choice(all_chars))

    # If the required length was less than the number of selected char sets,
    # we need to truncate it. (Though usually length >= 4)
    if len(password) > length:
        password = password[:length]

    # Shuffle the characters using secrets.SystemRandom()
    secrets.SystemRandom().shuffle(password)

    return ''.join(password)
