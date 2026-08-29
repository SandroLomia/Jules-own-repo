import string
import secrets

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """
    Generates a cryptographically secure random password.
    """
    if length < 4 and (use_upper and use_lower and use_digits and use_special):
        raise ValueError("Password length must be at least 4 when using all character types to ensure at least one of each is included.")
    if not (use_upper or use_lower or use_digits or use_special):
        raise ValueError("At least one character type must be selected.")

    char_pool = []
    password_chars = []

    if use_upper:
        char_pool.extend(list(string.ascii_uppercase))
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        char_pool.extend(list(string.ascii_lowercase))
        password_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        char_pool.extend(list(string.digits))
        password_chars.append(secrets.choice(string.digits))
    if use_special:
        # Use a standard set of special characters
        special_chars = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        char_pool.extend(list(special_chars))
        password_chars.append(secrets.choice(special_chars))

    if length < len(password_chars):
        raise ValueError(f"Password length ({length}) is too short to include at least one character of each selected type ({len(password_chars)}).")

    # Fill the rest of the password length
    remaining_length = length - len(password_chars)
    for _ in range(remaining_length):
        password_chars.append(secrets.choice(char_pool))

    # Perform a cryptographically secure shuffle
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

if __name__ == "__main__":
    print(generate_password())
