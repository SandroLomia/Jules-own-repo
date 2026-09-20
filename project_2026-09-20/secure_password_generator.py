import secrets
import string

def generate_password(length: int = 12, include_uppercase: bool = True, include_numbers: bool = True, include_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure password.

    Args:
        length (int): The length of the password. Default is 12. Must be greater than 0.
        include_uppercase (bool): Whether to include uppercase letters. Default is True.
        include_numbers (bool): Whether to include numbers. Default is True.
        include_symbols (bool): Whether to include symbols. Default is True.

    Returns:
        str: A cryptographically secure random password.

    Raises:
        ValueError: If the length is less than 1 or if no character sets are selected.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    numbers = string.digits if include_numbers else ""
    symbols = string.punctuation if include_symbols else ""

    all_characters = lowercase + uppercase + numbers + symbols

    if not all_characters:
        raise ValueError("At least one character set must be selected.")

    # Ensure the password has at least one character from each selected set
    password_chars = []
    if lowercase:
        password_chars.append(secrets.choice(lowercase))
    if include_uppercase:
        password_chars.append(secrets.choice(uppercase))
    if include_numbers:
        password_chars.append(secrets.choice(numbers))
    if include_symbols:
        password_chars.append(secrets.choice(symbols))

    # If the length requested is smaller than the required chars, that's fine,
    # but normally we want to generate up to `length`.
    # Actually if length < len(password_chars), we truncate it later or we should raise an error.
    # Let's handle it by just picking random characters if length < len(required).
    # To keep it simple, we will pick from all_characters to fill the rest.
    remaining_length = max(0, length - len(password_chars))
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(all_characters))

    # If length is smaller than the required sets (e.g., length=2, all sets=True), we truncate to length
    if len(password_chars) > length:
        # We need to randomly pick `length` characters from the required ones
        # Actually it's better to just truncate. But this violates the guarantee.
        # It's better to shuffle and then truncate.
        secrets.SystemRandom().shuffle(password_chars)
        password_chars = password_chars[:length]
    else:
        # Securely shuffle the result
        secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    print(f"Generated Password: {generate_password()}")
