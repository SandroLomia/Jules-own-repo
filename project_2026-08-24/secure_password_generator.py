import secrets
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): Length of the password. Minimum 4 recommended if all char types used.
        use_uppercase (bool): Include uppercase letters.
        use_lowercase (bool): Include lowercase letters.
        use_digits (bool): Include digits.
        use_special (bool): Include special characters.

    Returns:
        str: A randomly generated secure password.
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

    if use_digits:
        character_pool += string.digits
        required_characters.append(secrets.choice(string.digits))

    if use_special:
        # Avoid visually confusing characters where possible, but include standard symbols
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        character_pool += special_chars
        required_characters.append(secrets.choice(special_chars))

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    if length < len(required_characters):
         raise ValueError(f"Password length ({length}) is too short for the {len(required_characters)} required character types.")

    # Fill the rest of the password length with random characters from the pool
    remaining_length = length - len(required_characters)
    password_chars = required_characters + [secrets.choice(character_pool) for _ in range(remaining_length)]

    # Cryptographically secure shuffle
    secrets_generator = secrets.SystemRandom()
    secrets_generator.shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    print(f"Generated 16-char password: {generate_password(length=16)}")
    print(f"Generated 12-char alphanumeric password: {generate_password(length=12, use_special=False)}")
    print(f"Generated 8-char numeric PIN: {generate_password(length=8, use_uppercase=False, use_lowercase=False, use_special=False)}")
