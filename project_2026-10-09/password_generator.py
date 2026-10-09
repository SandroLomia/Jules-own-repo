import secrets
import string

def generate_password(length: int = 12, use_uppercase: bool = True, use_numbers: bool = True, use_symbols: bool = True) -> str:
    """
    Generate a cryptographically secure random password.

    Args:
        length (int): Length of the password. Minimum is usually 4 to satisfy all character pools.
        use_uppercase (bool): Include uppercase letters.
        use_numbers (bool): Include numbers.
        use_symbols (bool): Include punctuation symbols.

    Returns:
        str: The generated password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    lowercase_pool = string.ascii_lowercase
    uppercase_pool = string.ascii_uppercase
    numbers_pool = string.digits
    symbols_pool = string.punctuation

    char_pool = lowercase_pool
    required_chars = [secrets.choice(lowercase_pool)]

    if use_uppercase:
        char_pool += uppercase_pool
        required_chars.append(secrets.choice(uppercase_pool))

    if use_numbers:
        char_pool += numbers_pool
        required_chars.append(secrets.choice(numbers_pool))

    if use_symbols:
        char_pool += symbols_pool
        required_chars.append(secrets.choice(symbols_pool))

    if length < len(required_chars):
        raise ValueError(f"Password length ({length}) is too short for the required number of character types ({len(required_chars)}).")

    # Generate the rest of the password
    remaining_length = length - len(required_chars)
    password_chars = required_chars + [secrets.choice(char_pool) for _ in range(remaining_length)]

    # Securely shuffle the password characters
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    print("Generated Password:", generate_password())
    print("Generated Pin:", generate_password(length=6, use_uppercase=False, use_symbols=False))
