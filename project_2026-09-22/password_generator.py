import string
import secrets

def generate_password(length: int = 16, use_lowercase: bool = True, use_uppercase: bool = True, use_numbers: bool = True, use_symbols: bool = True) -> str:
    """
    Generates a cryptographically secure random password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Secure random number generator
    rng = secrets.SystemRandom()

    # Generate password characters
    password_chars = [rng.choice(characters) for _ in range(length)]

    # Shuffle for extra randomness just in case, though choice is already random
    rng.shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    print("Generated Password:", generate_password())
