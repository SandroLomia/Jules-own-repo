import string
import secrets

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_special=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): Length of the password. Default is 12.
        include_uppercase (bool): Whether to include uppercase letters.
        include_lowercase (bool): Whether to include lowercase letters.
        include_digits (bool): Whether to include digits.
        include_special (bool): Whether to include special characters.

    Returns:
        str: A securely generated random password.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4 for good security.")

    character_pool = ""
    required_characters = []

    if include_uppercase:
        character_pool += string.ascii_uppercase
        required_characters.append(secrets.choice(string.ascii_uppercase))

    if include_lowercase:
        character_pool += string.ascii_lowercase
        required_characters.append(secrets.choice(string.ascii_lowercase))

    if include_digits:
        character_pool += string.digits
        required_characters.append(secrets.choice(string.digits))

    if include_special:
        character_pool += string.punctuation
        required_characters.append(secrets.choice(string.punctuation))

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    # Fill the rest of the password length
    remaining_length = length - len(required_characters)
    password_list = required_characters + [secrets.choice(character_pool) for _ in range(remaining_length)]

    # Shuffle using the cryptographically secure SystemRandom
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)

if __name__ == "__main__":
    print(f"Generated Password (length=16): {generate_password(16)}")
