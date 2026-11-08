import string
import secrets


def generate_password(length: int = 16, use_uppercase: bool = True, use_digits: bool = True, use_special: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Must be at least 4.
        use_uppercase (bool): Whether to include uppercase letters.
        use_digits (bool): Whether to include digits.
        use_special (bool): Whether to include special characters.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length is less than 4.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ""
    digit_chars = string.digits if use_digits else ""
    special_chars = string.punctuation if use_special else ""

    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    if not all_chars:
        # Should not be possible with lowercase always enabled, but good practice
        raise ValueError("At least one character set must be selected.")

    # Ensure at least one character from each selected set is included
    password_chars = []
    password_chars.append(secrets.choice(lowercase_chars))
    if use_uppercase:
        password_chars.append(secrets.choice(uppercase_chars))
    if use_digits:
        password_chars.append(secrets.choice(digit_chars))
    if use_special:
        password_chars.append(secrets.choice(special_chars))

    # Fill the rest of the password length
    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(all_chars))

    # Shuffle the characters to ensure randomness
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)
