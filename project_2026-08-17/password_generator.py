import string
import secrets

def generate_password(length=12):
    """
    Generates a cryptographically secure password.

    The password will contain at least one character from each of the following sets:
    - Lowercase letters
    - Uppercase letters
    - Digits
    - Punctuation

    Args:
        length (int): The length of the password to generate. Must be at least 4.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If the length is less than 4.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to include all character types.")

    alphabet = string.ascii_letters + string.digits + string.punctuation

    # Ensure at least one character from each set
    password_chars = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    # Fill the rest with random characters
    password_chars += [secrets.choice(alphabet) for _ in range(length - 4)]

    # Securely shuffle the password characters
    secrets.SystemRandom().shuffle(password_chars)

    return ''.join(password_chars)

if __name__ == '__main__':
    print("Generated Password:", generate_password())
