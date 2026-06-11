import secrets
import string

def generate_password(length=16, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Default is 16.
        use_uppercase (bool): Whether to include uppercase letters.
        use_digits (bool): Whether to include digits.
        use_special (bool): Whether to include special characters.

    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 to ensure security and complexity.")

    # Start with lowercase letters which are always included
    alphabet = string.ascii_lowercase

    # Track required characters to ensure at least one of each requested type is present
    required_chars = [secrets.choice(string.ascii_lowercase)]

    if use_uppercase:
        alphabet += string.ascii_uppercase
        required_chars.append(secrets.choice(string.ascii_uppercase))

    if use_digits:
        alphabet += string.digits
        required_chars.append(secrets.choice(string.digits))

    if use_special:
        # Avoid visually confusing characters if possible, but for general purposes use standard punctuation
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        alphabet += special_chars
        required_chars.append(secrets.choice(special_chars))

    # Generate the rest of the password
    remaining_length = length - len(required_chars)
    password_chars = required_chars + [secrets.choice(alphabet) for _ in range(remaining_length)]

    # Shuffle the characters to ensure randomness
    # secrets does not have a shuffle method, so we emulate it securely
    secure_rng = secrets.SystemRandom()
    secure_rng.shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    print(f"Generated Password (default): {generate_password()}")
    print(f"Generated Password (length 20): {generate_password(length=20)}")
    print(f"Generated Password (no special): {generate_password(use_special=False)}")
