import secrets
import string

def generate_password(length: int = 16, include_uppercase: bool = True, include_numbers: bool = True, include_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure password.

    Args:
        length (int): The length of the password. Minimum length is 8.
        include_uppercase (bool): Whether to include uppercase letters.
        include_numbers (bool): Whether to include numbers.
        include_symbols (bool): Whether to include symbols.

    Returns:
        str: A randomly generated, secure password.
    """
    if length < 8:
        raise ValueError("Password length must be at least 8 characters for security reasons.")

    # Base character set: always include lowercase letters
    characters = list(string.ascii_lowercase)

    # Optional character sets
    if include_uppercase:
        characters.extend(list(string.ascii_uppercase))
    if include_numbers:
        characters.extend(list(string.digits))
    if include_symbols:
        characters.extend(list(string.punctuation))

    # Create an initial secure pool from which to choose
    # and guarantee at least one character of each requested type
    password = []

    # Add one character of each requested type to ensure the password meets the complexity requirements
    password.append(secrets.choice(string.ascii_lowercase))
    if include_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if include_numbers:
        password.append(secrets.choice(string.digits))
    if include_symbols:
        password.append(secrets.choice(string.punctuation))

    # Fill the rest of the password length
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(secrets.choice(characters))

    # Cryptographically secure shuffle of the password characters
    # Since secrets doesn't have shuffle directly, we use secrets.SystemRandom()
    secure_random = secrets.SystemRandom()
    secure_random.shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    print(f"Generated 16-character password: {generate_password(16)}")
    print(f"Generated 24-character password: {generate_password(24)}")
