import secrets
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): Length of the password. Default is 12.
        use_uppercase (bool): Include uppercase letters. Default is True.
        use_numbers (bool): Include numbers. Default is True.
        use_symbols (bool): Include symbols. Default is True.

    Returns:
        str: The generated password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ""
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""

    all_characters = lowercase + uppercase + numbers + symbols

    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    # Ensure at least one character of each selected type is included
    password = []
    password.append(secrets.choice(lowercase))
    if use_uppercase:
        password.append(secrets.choice(uppercase))
    if use_numbers:
        password.append(secrets.choice(numbers))
    if use_symbols:
        password.append(secrets.choice(symbols))

    # Fill the rest of the password
    if length < len(password):
        raise ValueError(f"Length must be at least {len(password)} to accommodate the selected character types.")

    for _ in range(length - len(password)):
        password.append(secrets.choice(all_characters))

    # Shuffle the password to ensure randomness using cryptographically secure method
    secrets.SystemRandom().shuffle(password)

    return "".join(password)
