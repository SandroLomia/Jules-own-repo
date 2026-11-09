import string
import secrets

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special=True):
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ""
    number_chars = string.digits if use_numbers else ""
    special_chars = string.punctuation if use_special else ""

    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars

    if not all_chars:
        raise ValueError("At least one character set must be selected.")

    password = []

    # Ensure at least one character from each selected set is included
    password.append(secrets.choice(lowercase_chars))
    if use_uppercase:
        password.append(secrets.choice(uppercase_chars))
    if use_numbers:
        password.append(secrets.choice(number_chars))
    if use_special:
        password.append(secrets.choice(special_chars))

    # Fill the rest of the password
    for _ in range(length - len(password)):
        password.append(secrets.choice(all_chars))

    # Cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password)
