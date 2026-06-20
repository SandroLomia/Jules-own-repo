import secrets
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True):
    """
    Generates a cryptographically secure random password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    character_pool = ""
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_digits:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    # Ensure at least one character from each selected pool is included
    password = []
    if include_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if include_lowercase:
        password.append(secrets.choice(string.ascii_lowercase))
    if include_digits:
        password.append(secrets.choice(string.digits))
    if include_symbols:
        password.append(secrets.choice(string.punctuation))

    # Fill the rest of the password length
    while len(password) < length:
        password.append(secrets.choice(character_pool))

    # Cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password)

    return "".join(password[:length])

if __name__ == "__main__":
    print(f"Generated Password: {generate_password(16)}")
