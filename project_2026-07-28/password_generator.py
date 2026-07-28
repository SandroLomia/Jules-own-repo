import string
import secrets

def generate_password(
    length: int = 12,
    use_uppercase: bool = True,
    use_lowercase: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True
) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Default is 12.
        use_uppercase (bool): Whether to include uppercase letters. Default is True.
        use_lowercase (bool): Whether to include lowercase letters. Default is True.
        use_digits (bool): Whether to include digits. Default is True.
        use_symbols (bool): Whether to include symbols. Default is True.

    Returns:
        str: A randomly generated secure password.

    Raises:
        ValueError: If length is less than or equal to 0, or if no character types are selected.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = "".join(secrets.choice(characters) for _ in range(length))

    # Ensure at least one character from each selected pool is present
    password_list = list(password)

    # We will replace the first `num_required` characters to guarantee minimum requirements
    required_chars = []
    if use_uppercase:
        required_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        required_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        required_chars.append(secrets.choice(string.digits))
    if use_symbols:
        required_chars.append(secrets.choice(string.punctuation))

    if length < len(required_chars):
         raise ValueError(f"Password length ({length}) must be at least {len(required_chars)} to satisfy the selected character types.")

    for i, char in enumerate(required_chars):
        password_list[i] = char

    # Shuffle using secrets.SystemRandom
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)
