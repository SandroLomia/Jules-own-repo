import string
import secrets

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Defaults to 12.
        use_uppercase (bool): Whether to include uppercase letters. Defaults to True.
        use_lowercase (bool): Whether to include lowercase letters. Defaults to True.
        use_digits (bool): Whether to include digits. Defaults to True.
        use_symbols (bool): Whether to include symbols. Defaults to True.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If no character types are selected or if length is non-positive.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than zero.")

    character_pool = ""
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    # Using secrets.choice for cryptographically secure random selection
    password = ''.join(secrets.choice(character_pool) for _ in range(length))
    return password

if __name__ == "__main__":
    print(f"Default Password: {generate_password()}")
    print(f"Alphanumeric only: {generate_password(use_symbols=False)}")
    print(f"Short PIN: {generate_password(length=6, use_uppercase=False, use_lowercase=False, use_symbols=False)}")
