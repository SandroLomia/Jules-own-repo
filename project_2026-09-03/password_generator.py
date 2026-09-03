import string
import secrets

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_punctuation=True):
    """
    Generates a cryptographically secure random password.
    """
    if length < 4:
        raise ValueError("Password length should be at least 4.")

    characters = ""
    password = []

    if use_uppercase:
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lowercase:
        characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        characters += string.digits
        password.append(secrets.choice(string.digits))
    if use_punctuation:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    if not characters:
        raise ValueError("At least one character set must be selected.")

    while len(password) < length:
        password.append(secrets.choice(characters))

    # Cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    print("Generated Secure Password:", generate_password())
