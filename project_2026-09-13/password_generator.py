import string
import secrets

def generate_password(length: int = 16, use_uppercase: bool = True, use_numbers: bool = True, use_special: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Minimum is 4 if all types are used to ensure at least one of each.
        use_uppercase (bool): Include uppercase letters.
        use_numbers (bool): Include numbers.
        use_special (bool): Include special characters.

    Returns:
        str: The generated password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ""
    number_chars = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special else ""

    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars

    if not all_chars:
        raise ValueError("At least one character type must be selected.")

    # Ensure at least one character from each selected pool is included
    password = []

    # We must have at least one lowercase character since it's always included in our base set
    password.append(secrets.choice(lowercase_chars))

    if use_uppercase:
        password.append(secrets.choice(uppercase_chars))
    if use_numbers:
        password.append(secrets.choice(number_chars))
    if use_special:
        password.append(secrets.choice(special_chars))

    if length < len(password):
        raise ValueError(f"Password length must be at least {len(password)} to include all selected character types.")

    # Fill the rest of the password length with random choices from all selected characters
    while len(password) < length:
        password.append(secrets.choice(all_chars))

    # Perform a cryptographically secure shuffle
    sys_rand = secrets.SystemRandom()
    sys_rand.shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    print(f"Generated Password (Default): {generate_password()}")
    print(f"Generated Password (No Special, No Numbers, 12 chars): {generate_password(length=12, use_numbers=False, use_special=False)}")
