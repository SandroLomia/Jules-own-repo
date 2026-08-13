import secrets
import string

def generate_password(length: int = 12, use_upper: bool = True, use_lower: bool = True, use_digits: bool = True, use_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password to generate.
        use_upper (bool): Whether to include uppercase letters.
        use_lower (bool): Whether to include lowercase letters.
        use_digits (bool): Whether to include digits.
        use_symbols (bool): Whether to include symbols.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If no character types are selected or length is <= 0.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    char_pool = ""
    required_chars = []

    if use_upper:
        char_pool += string.ascii_uppercase
        required_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        char_pool += string.ascii_lowercase
        required_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        char_pool += string.digits
        required_chars.append(secrets.choice(string.digits))
    if use_symbols:
        char_pool += string.punctuation
        required_chars.append(secrets.choice(string.punctuation))

    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    if length < len(required_chars):
        raise ValueError(f"Password length must be at least {len(required_chars)} to satisfy the selected constraints.")

    # Fill the rest of the password length with random choices from the pool
    remaining_length = length - len(required_chars)
    password_chars = required_chars + [secrets.choice(char_pool) for _ in range(remaining_length)]

    # Securely shuffle the password characters
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    print("Example 12-char password:", generate_password())
    print("Example 16-char alphanumeric password:", generate_password(length=16, use_symbols=False))
