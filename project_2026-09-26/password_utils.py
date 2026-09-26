import secrets
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special=True):
    """
    Generates a cryptographically secure password based on provided criteria.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Ensure at least one character from each requested category
    password_chars = []
    if include_uppercase:
        password_chars.append(secrets.choice(string.ascii_uppercase))
    if include_numbers:
        password_chars.append(secrets.choice(string.digits))
    if include_special:
        password_chars.append(secrets.choice(string.punctuation))

    # Fill the rest with random characters
    while len(password_chars) < length:
        password_chars.append(secrets.choice(characters))

    # Shuffle the characters using secrets
    sys_rand = secrets.SystemRandom()
    sys_rand.shuffle(password_chars)

    return ''.join(password_chars)

def evaluate_strength(password):
    """
    Evaluates the strength of a given password.
    Returns a score from 0 to 4.
    """
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    # Cap score at 4 based on typical strength evaluators
    return min(score, 4)
