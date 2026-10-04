import secrets
import string

def generate_password(length: int = 12, use_uppercase: bool = True, use_numbers: bool = True, use_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure password with configurable requirements.

    Args:
        length (int): The length of the password to generate. Defaults to 12.
        use_uppercase (bool): Whether to include uppercase letters. Defaults to True.
        use_numbers (bool): Whether to include numbers. Defaults to True.
        use_symbols (bool): Whether to include symbols. Defaults to True.

    Returns:
        str: The generated password.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    character_pool = string.ascii_lowercase
    password_chars = []

    if use_uppercase:
        character_pool += string.ascii_uppercase
        password_chars.append(secrets.choice(string.ascii_uppercase))

    if use_numbers:
        character_pool += string.digits
        password_chars.append(secrets.choice(string.digits))

    if use_symbols:
        character_pool += string.punctuation
        password_chars.append(secrets.choice(string.punctuation))

    # Ensure we have at least one lowercase letter
    password_chars.append(secrets.choice(string.ascii_lowercase))

    if len(password_chars) > length:
        # If requirements exceed requested length, truncate randomly but ensure length matches
        secrets.SystemRandom().shuffle(password_chars)
        return ''.join(password_chars[:length])

    # Fill the rest of the password length
    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(character_pool))

    secrets.SystemRandom().shuffle(password_chars)
    return ''.join(password_chars)

if __name__ == "__main__":
    print(f"Default 12-char password: {generate_password()}")
    print(f"20-char password with no symbols: {generate_password(length=20, use_symbols=False)}")
    print(f"16-char password with only letters: {generate_password(length=16, use_numbers=False, use_symbols=False)}")
