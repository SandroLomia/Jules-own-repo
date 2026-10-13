import secrets
import string

def generate_password(length: int = 12, use_uppercase: bool = True, use_numbers: bool = True, use_special: bool = True) -> str:
    """
    Generates a cryptographically secure password.

    Args:
        length (int): Length of the password. Default is 12.
        use_uppercase (bool): Whether to include uppercase letters. Default is True.
        use_numbers (bool): Whether to include numbers. Default is True.
        use_special (bool): Whether to include special characters. Default is True.

    Returns:
        str: A randomly generated password.
    """

    if length <= 0:
        raise ValueError("Password length must be greater than zero.")

    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ""
    number_chars = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special else ""

    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars

    if not all_chars:
        raise ValueError("At least one character type must be selected.")

    password = []

    # Ensure at least one character of each selected type is included
    if lowercase_chars:
        password.append(secrets.choice(lowercase_chars))
    if uppercase_chars:
        password.append(secrets.choice(uppercase_chars))
    if number_chars:
        password.append(secrets.choice(number_chars))
    if special_chars:
        password.append(secrets.choice(special_chars))

    # Fill the rest of the password length
    while len(password) < length:
        password.append(secrets.choice(all_chars))

    # Shuffle the characters using a cryptographically secure random number generator
    secrets.SystemRandom().shuffle(password)

    # Trim to exact length (in case the minimum guaranteed characters exceeded the requested length)
    password = password[:length]

    # Shuffle again just in case the trimming removed something from the end deterministically
    secrets.SystemRandom().shuffle(password)

    return "".join(password)
