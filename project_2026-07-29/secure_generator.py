import string
import secrets


def generate_password(
    length: int = 16,
    use_uppercase: bool = True,
    use_numbers: bool = True,
    use_symbols: bool = True,
) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length: The length of the password. Minimum is 4.
        use_uppercase: Whether to include uppercase letters.
        use_numbers: Whether to include digits.
        use_symbols: Whether to include symbols.

    Returns:
        A securely generated random string.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    # Build the character pool and ensure at least one character from each requested pool
    pool = lowercase
    password_chars = [secrets.choice(lowercase)]

    if use_uppercase:
        pool += uppercase
        password_chars.append(secrets.choice(uppercase))

    if use_numbers:
        pool += numbers
        password_chars.append(secrets.choice(numbers))

    if use_symbols:
        pool += symbols
        password_chars.append(secrets.choice(symbols))

    # Fill the rest of the password length
    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(pool))

    # Use SystemRandom().shuffle() for cryptographically secure shuffling
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)


def generate_token(length: int = 32) -> str:
    """
    Generates a cryptographically secure random URL-safe token.

    Args:
        length: The length of the token (in bytes, resulting string will be longer).
                If you want a specific string length, use token_urlsafe.

    Returns:
        A securely generated URL-safe token.
    """
    if length < 1:
        raise ValueError("Token length must be at least 1.")

    return secrets.token_urlsafe(length)
