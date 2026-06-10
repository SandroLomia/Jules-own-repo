import string
import secrets

def generate_password(length: int = 12, use_upper: bool = True, use_numbers: bool = True, use_special: bool = True) -> str:
    """
    Generates a cryptographically secure random password.

    Args:
        length: The length of the password. Minimum length is 4 if all character sets are used.
        use_upper: Whether to include uppercase letters.
        use_numbers: Whether to include numbers.
        use_special: Whether to include special characters.

    Returns:
        A randomly generated secure password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    # Build the character pool
    pool = string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_numbers:
        pool += string.digits
    if use_special:
        pool += string.punctuation

    if not pool:
        raise ValueError("At least one character set must be selected")

    # Generate the password
    # To ensure at least one character from each selected pool is included,
    # we first pick one character from each requested pool.

    password_chars = []

    if use_upper:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_numbers:
        password_chars.append(secrets.choice(string.digits))
    if use_special:
        password_chars.append(secrets.choice(string.punctuation))

    # Also add a lowercase letter since it's the base pool
    password_chars.append(secrets.choice(string.ascii_lowercase))

    # Fill the rest of the password length
    remaining_length = length - len(password_chars)
    if remaining_length > 0:
        for _ in range(remaining_length):
            password_chars.append(secrets.choice(pool))
    elif remaining_length < 0:
        # If the requested length is smaller than the number of constraints, we just pick from the pool
        # This breaks the strict guarantee of having at least one of each, but respects the length
        # Or we could raise an error. Let's just pick randomly from the pool if length is too small.
        password_chars = [secrets.choice(pool) for _ in range(length)]
        return ''.join(password_chars)

    # Shuffle the characters using secrets to ensure randomness
    # secrets doesn't have shuffle, so we do it manually or using SystemRandom
    rng = secrets.SystemRandom()
    rng.shuffle(password_chars)

    return ''.join(password_chars)

if __name__ == '__main__':
    print(f"Generated password: {generate_password(16)}")
