import string
import secrets

def generate_password(length: int = 12, use_special: bool = True) -> str:
    """
    Generate a cryptographically secure random password.

    Args:
        length (int): The length of the password. Defaults to 12.
        use_special (bool): Whether to include special characters. Defaults to True.

    Returns:
        str: The generated password.
    """
    alphabet = string.ascii_letters + string.digits
    if use_special:
        alphabet += string.punctuation

    return ''.join(secrets.choice(alphabet) for i in range(length))

if __name__ == "__main__":
    print(f"Generated password (length 16, with special chars): {generate_password(16, True)}")
    print(f"Generated password (length 12, without special chars): {generate_password(12, False)}")
