import secrets
import string

def shuffle_string(text: str) -> str:
    """
    Cryptographically secure shuffle of a string.
    """
    text_list = list(text)
    secrets.SystemRandom().shuffle(text_list)
    return "".join(text_list)

def generate_password(length: int = 12, use_uppercase: bool = True, use_numbers: bool = True, use_special: bool = True) -> str:
    """
    Generates a secure password using the secrets module.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    number_chars = string.digits
    special_chars = string.punctuation

    pool = lowercase_chars
    password_chars = [secrets.choice(lowercase_chars)]

    if use_uppercase:
        pool += uppercase_chars
        password_chars.append(secrets.choice(uppercase_chars))
    if use_numbers:
        pool += number_chars
        password_chars.append(secrets.choice(number_chars))
    if use_special:
        pool += special_chars
        password_chars.append(secrets.choice(special_chars))

    if length < len(password_chars):
        raise ValueError("Password length is too short to satisfy the character set requirements.")

    while len(password_chars) < length:
        password_chars.append(secrets.choice(pool))

    password = "".join(password_chars)
    return shuffle_string(password)

if __name__ == "__main__":
    print("Secure password:", generate_password())
