import secrets
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generate a cryptographically secure random password.

    Args:
        length (int): The length of the generated password (must be at least the number of active character sets).
        use_lowercase (bool): Include lowercase letters.
        use_uppercase (bool): Include uppercase letters.
        use_digits (bool): Include digits.
        use_special (bool): Include special characters.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If no character sets are selected or if the length is too short to include one of each selected set.
    """

    character_sets = []
    if use_lowercase:
        character_sets.append(string.ascii_lowercase)
    if use_uppercase:
        character_sets.append(string.ascii_uppercase)
    if use_digits:
        character_sets.append(string.digits)
    if use_special:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character set must be selected.")

    if length < len(character_sets):
        raise ValueError(f"Password length must be at least {len(character_sets)} to include one of each selected character set.")

    # Ensure at least one character from each selected set is included
    password_chars = []
    for charset in character_sets:
        password_chars.append(secrets.choice(charset))

    # Fill the rest of the password length with random characters from all selected sets combined
    all_chars = ''.join(character_sets)
    for _ in range(length - len(character_sets)):
        password_chars.append(secrets.choice(all_chars))

    # Shuffle the resulting characters securely
    # secrets.SystemRandom().shuffle is required for cryptographic security instead of random.shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)
