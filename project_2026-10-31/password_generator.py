import string
import secrets

def generate_password(length: int, use_uppercase: bool = True, use_numbers: bool = True, use_symbols: bool = True) -> str:
    """
    Generates a secure random password.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0")

    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ""
    number_chars = string.digits if use_numbers else ""
    symbol_chars = string.punctuation if use_symbols else ""

    all_chars = lowercase_chars + uppercase_chars + number_chars + symbol_chars
    if not all_chars:
        raise ValueError("At least one character set must be selected")

    password = []

    # Ensure at least one character from each selected set is included if possible
    pool_used = []
    pool_used.append(lowercase_chars)
    if use_uppercase:
        pool_used.append(uppercase_chars)
    if use_numbers:
        pool_used.append(number_chars)
    if use_symbols:
        pool_used.append(symbol_chars)

    if length < len(pool_used):
        # Pick randomly if the length is too small to guarantee one of each
        for _ in range(length):
            password.append(secrets.choice(all_chars))
    else:
        for char_set in pool_used:
            password.append(secrets.choice(char_set))

        # Fill the rest of the password
        remaining_length = length - len(password)
        for _ in range(remaining_length):
            password.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)
