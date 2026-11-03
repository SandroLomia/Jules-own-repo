import secrets
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): Length of the generated password. Must be > 0.
        use_lowercase (bool): Include lowercase letters.
        use_uppercase (bool): Include uppercase letters.
        use_digits (bool): Include digits.
        use_special (bool): Include special characters.

    Returns:
        str: A cryptographically secure generated password.

    Raises:
        ValueError: If length <= 0 or if no character sets are selected.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    chars = ""
    if use_lowercase:
        chars += string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        raise ValueError("At least one character set must be selected.")

    # Generate the password
    password = "".join(secrets.choice(chars) for _ in range(length))
    return password

if __name__ == '__main__':
    print("Example 12-char password:", generate_password())
    print("Example 16-char alphanumeric password:", generate_password(length=16, use_special=False))
