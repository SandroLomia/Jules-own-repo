import string
import secrets

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password to generate. Default is 12.
        include_uppercase (bool): Whether to include uppercase letters. Default is True.
        include_digits (bool): Whether to include digits. Default is True.
        include_special (bool): Whether to include special characters. Default is True.

    Returns:
        str: A randomly generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Ensure at least one character of each selected type is included if length permits
    password_chars = []

    password_chars.append(secrets.choice(string.ascii_lowercase))
    if include_uppercase:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if include_digits:
        password_chars.append(secrets.choice(string.digits))
    if include_special:
        password_chars.append(secrets.choice(string.punctuation))

    # Fill the rest of the password length
    while len(password_chars) < length:
        password_chars.append(secrets.choice(characters))

    # Shuffle the characters to prevent predictable patterns
    # secrets module doesn't have shuffle, but we can do something like this or use random.SystemRandom().shuffle
    # since we want to only use secrets or SystemRandom

    secure_rng = secrets.SystemRandom()
    secure_rng.shuffle(password_chars)

    return ''.join(password_chars)

if __name__ == "__main__":
    print(f"Generated Password (length 16): {generate_password(16)}")
