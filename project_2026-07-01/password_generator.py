import string
import secrets

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_numbers=True, use_symbols=True):
    """
    Generates a cryptographically secure random password.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    if not any([use_uppercase, use_lowercase, use_numbers, use_symbols]):
        raise ValueError("At least one character type must be selected.")

    characters = ""
    password_list = []

    if use_uppercase:
        characters += string.ascii_uppercase
        password_list.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        characters += string.ascii_lowercase
        password_list.append(secrets.choice(string.ascii_lowercase))
    if use_numbers:
        characters += string.digits
        password_list.append(secrets.choice(string.digits))
    if use_symbols:
        characters += string.punctuation
        password_list.append(secrets.choice(string.punctuation))

    if length < len(password_list):
        raise ValueError("Password length must be at least the number of selected character types to ensure inclusion of all selected types.")

    # Fill the rest of the password length
    for _ in range(length - len(password_list)):
        password_list.append(secrets.choice(characters))

    # Shuffle the characters to randomize the positions
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)
