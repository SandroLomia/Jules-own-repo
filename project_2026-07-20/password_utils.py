import secrets
import string

def generate_password(length: int, upper: bool, lower: bool, numbers: bool, symbols: bool) -> str:
    """
    Generate a secure password based on specified criteria.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    if not any([upper, lower, numbers, symbols]):
        raise ValueError("At least one character set must be selected.")

    char_sets = []
    if upper:
        char_sets.append(string.ascii_uppercase)
    if lower:
        char_sets.append(string.ascii_lowercase)
    if numbers:
        char_sets.append(string.digits)
    if symbols:
        char_sets.append(string.punctuation)

    all_chars = "".join(char_sets)

    # Ensure at least one character from each selected set is included
    password = [secrets.choice(char_set) for char_set in char_sets]

    # Fill the rest of the password length
    password += [secrets.choice(all_chars) for _ in range(length - len(password))]

    # Shuffle the password to ensure randomness
    secrets.SystemRandom().shuffle(password)

    return "".join(password)

def analyze_strength(password: str) -> str:
    """
    Analyze the strength of a given password.
    Returns 'Weak', 'Medium', or 'Strong'.
    """
    length_score = len(password) >= 12
    upper_score = any(c.isupper() for c in password)
    lower_score = any(c.islower() for c in password)
    number_score = any(c.isdigit() for c in password)
    symbol_score = any(c in string.punctuation for c in password)

    score = sum([length_score, upper_score, lower_score, number_score, symbol_score])

    if score >= 4:
        return 'Strong'
    elif score >= 2:
        return 'Medium'
    else:
        return 'Weak'
