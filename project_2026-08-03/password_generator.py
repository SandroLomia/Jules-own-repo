import string
import secrets

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The desired length of the password.
        use_upper (bool): Include uppercase letters.
        use_lower (bool): Include lowercase letters.
        use_digits (bool): Include digits.
        use_symbols (bool): Include symbols (punctuation).

    Returns:
        str: A generated password meeting the specified criteria.

    Raises:
        ValueError: If length is <= 0 or no character sets are selected.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    char_sets = []
    if use_upper:
        char_sets.append(string.ascii_uppercase)
    if use_lower:
        char_sets.append(string.ascii_lowercase)
    if use_digits:
        char_sets.append(string.digits)
    if use_symbols:
        char_sets.append(string.punctuation)

    if not char_sets:
        raise ValueError("At least one character set must be selected.")

    # Combine all allowed characters
    all_chars = "".join(char_sets)

    # Ensure at least one character from each selected set is used to guarantee variety
    password_chars = []
    for char_set in char_sets:
        password_chars.append(secrets.choice(char_set))

    # Fill the rest of the password length
    remaining_length = length - len(password_chars)
    if remaining_length < 0:
        raise ValueError(f"Password length ({length}) must be at least the number of selected character sets ({len(char_sets)}).")

    for _ in range(remaining_length):
        password_chars.append(secrets.choice(all_chars))

    # Cryptographically secure shuffle of the chosen characters
    sys_random = secrets.SystemRandom()
    sys_random.shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    # Example usage
    print("Default password (12 chars, all sets):", generate_password())
    print("16 chars, letters only:", generate_password(length=16, use_digits=False, use_symbols=False))
    print("20 chars, alphanumeric:", generate_password(length=20, use_symbols=False))
