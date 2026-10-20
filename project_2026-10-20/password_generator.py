import string
import secrets

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """
    Generates a cryptographically secure password using the secrets module.

    Args:
        length (int): Total length of the password. Minimum length is usually 4 to ensure at least
                      one character from each set if all flags are true, but enforced minimal logic will handle it.
        use_uppercase (bool): Whether to include uppercase letters.
        use_digits (bool): Whether to include digits.
        use_symbols (bool): Whether to include symbols/punctuation.

    Returns:
        str: A securely generated password.
    """

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    pool = lower
    guaranteed_chars = [secrets.choice(lower)]

    if use_uppercase:
        pool += upper
        guaranteed_chars.append(secrets.choice(upper))

    if use_digits:
        pool += digits
        guaranteed_chars.append(secrets.choice(digits))

    if use_symbols:
        pool += symbols
        guaranteed_chars.append(secrets.choice(symbols))

    if length < len(guaranteed_chars):
        raise ValueError(f"Password length must be at least {len(guaranteed_chars)} based on selected options.")

    # Fill the rest of the password length with random choices from the pool
    remaining_length = length - len(guaranteed_chars)
    password_chars = guaranteed_chars + [secrets.choice(pool) for _ in range(remaining_length)]

    # Cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)
