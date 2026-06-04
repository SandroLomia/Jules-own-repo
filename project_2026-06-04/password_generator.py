import secrets
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_symbols=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password. Minimum is 4.
        use_uppercase (bool): Include uppercase letters.
        use_numbers (bool): Include digits.
        use_symbols (bool): Include punctuation symbols.

    Returns:
        str: The generated secure password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected.")

    # Ensure at least one character from each selected set is included if the length allows
    password = []
    if use_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_numbers:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    # Fill the rest of the password length
    remaining_length = length - len(password)
    password.extend(secrets.choice(characters) for _ in range(remaining_length))

    # Shuffle the list to randomize the position of the guaranteed characters
    # Since secrets doesn't have a shuffle method that works in-place like random.shuffle,
    # we can implement a Fisher-Yates shuffle using secrets.randbelow
    for i in range(len(password) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        password[i], password[j] = password[j], password[i]

    return ''.join(password)
