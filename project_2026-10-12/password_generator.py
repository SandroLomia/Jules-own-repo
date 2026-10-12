import string
import secrets

def generate_password(length: int, use_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The length of the password.
        use_symbols (bool): Whether to include symbols in the password. Defaults to True.

    Returns:
        str: The generated password.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if use_symbols else ""

    alphabet = letters + digits + symbols

    if not alphabet:
        raise ValueError("Alphabet for password generation cannot be empty.")

    # Ensure at least one character from each selected pool is used if length allows
    password = []

    if length >= 3:
        password.append(secrets.choice(string.ascii_lowercase))
        password.append(secrets.choice(string.ascii_uppercase))
        password.append(secrets.choice(string.digits))
        if use_symbols and length >= 4:
            password.append(secrets.choice(symbols))

    # Fill the rest of the password
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(secrets.choice(alphabet))

    # If the length was too small to include at least one of each,
    # just fill it with random choices from the alphabet.
    # The list is already created and filled if length < 3
    if length < 3 or (use_symbols and length < 4):
         password = [secrets.choice(alphabet) for _ in range(length)]

    # Shuffle the password to make it unpredictable
    sys_rand = secrets.SystemRandom()
    sys_rand.shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    print(f"Generated 16-char password (with symbols): {generate_password(16)}")
    print(f"Generated 12-char password (without symbols): {generate_password(12, use_symbols=False)}")
