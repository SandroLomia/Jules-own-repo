import string
import secrets

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Default is 12.
        use_upper (bool): Whether to include uppercase letters.
        use_lower (bool): Whether to include lowercase letters.
        use_digits (bool): Whether to include digits.
        use_special (bool): Whether to include special characters.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length is <= 0 or if no character sets are selected.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0")

    characters = []
    required_chars = []

    if use_upper:
        characters.extend(string.ascii_uppercase)
        required_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        characters.extend(string.ascii_lowercase)
        required_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        characters.extend(string.digits)
        required_chars.append(secrets.choice(string.digits))
    if use_special:
        characters.extend(string.punctuation)
        required_chars.append(secrets.choice(string.punctuation))

    if not characters:
        raise ValueError("At least one character set must be selected.")

    if length < len(required_chars):
        raise ValueError("Password length is too short to satisfy the selected character sets.")

    # Fill the rest of the password length with random characters from the pool
    remaining_length = length - len(required_chars)
    password_chars = required_chars + [secrets.choice(characters) for _ in range(remaining_length)]

    # Securely shuffle the password characters
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    print(f"Generated Password (Default): {generate_password()}")
    print(f"Generated Password (16 chars, no special): {generate_password(length=16, use_special=False)}")
