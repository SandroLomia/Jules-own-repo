import secrets
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    """
    Generates a secure password using the specified character sets.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    return ''.join(secrets.choice(characters) for _ in range(length))

def evaluate_strength(password):
    """
    Evaluates the strength of a given password.
    Returns 'Weak', 'Medium', or 'Strong'.
    """
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])

    if length >= 12 and score >= 3:
        return 'Strong'
    elif length >= 8 and score >= 2:
        return 'Medium'
    else:
        return 'Weak'
