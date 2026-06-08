import secrets
import string

def generate_password(length: int = 16, use_uppercase: bool = True, use_numbers: bool = True, use_special: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Minimum is 8 characters. Defaults to 16.
        use_uppercase (bool): Whether to include uppercase letters. Defaults to True.
        use_numbers (bool): Whether to include numbers. Defaults to True.
        use_special (bool): Whether to include special characters. Defaults to True.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length is less than 8 or if all character types are disabled.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters.")

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        # This case is technically caught by string.ascii_lowercase always being included,
        # but kept for completeness if we ever allow disabling lowercase.
        raise ValueError("At least one character type must be selected.")

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Generating a secure 16-character password with default settings:")
    print(generate_password())

    print("\nGenerating a secure 20-character password without special characters:")
    print(generate_password(length=20, use_special=False))
