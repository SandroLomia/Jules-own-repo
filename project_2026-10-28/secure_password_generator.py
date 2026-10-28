import secrets
import string

def generate_password(length: int = 16,
                      use_uppercase: bool = True,
                      use_lowercase: bool = True,
                      use_numbers: bool = True,
                      use_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): Length of the password. Default is 16.
        use_uppercase (bool): Include uppercase letters. Default is True.
        use_lowercase (bool): Include lowercase letters. Default is True.
        use_numbers (bool): Include numbers. Default is True.
        use_symbols (bool): Include symbols. Default is True.

    Returns:
        str: The generated password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    character_pool = ""
    required_characters = []

    if use_uppercase:
        character_pool += string.ascii_uppercase
        required_characters.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        character_pool += string.ascii_lowercase
        required_characters.append(secrets.choice(string.ascii_lowercase))
    if use_numbers:
        character_pool += string.digits
        required_characters.append(secrets.choice(string.digits))
    if use_symbols:
        character_pool += string.punctuation
        required_characters.append(secrets.choice(string.punctuation))

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    if length < len(required_characters):
        raise ValueError("Password length is too short to satisfy the required character types.")

    # Fill the rest of the password length with random characters from the pool
    remaining_length = length - len(required_characters)
    password_chars = required_characters + [secrets.choice(character_pool) for _ in range(remaining_length)]

    # Cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    print(f"Random 16-char password: {generate_password()}")
