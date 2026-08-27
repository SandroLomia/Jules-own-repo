import secrets
import string
import math

def generate_password(length: int = 16, use_upper: bool = True, use_lower: bool = True, use_digits: bool = True, use_special: bool = True) -> str:
    if length < 1:
        raise ValueError("Password length must be at least 1.")

    char_sets = []
    required_chars = []

    if use_upper:
        char_sets.append(string.ascii_uppercase)
        required_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        char_sets.append(string.ascii_lowercase)
        required_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        char_sets.append(string.digits)
        required_chars.append(secrets.choice(string.digits))
    if use_special:
        char_sets.append(string.punctuation)
        required_chars.append(secrets.choice(string.punctuation))

    if not char_sets:
        raise ValueError("At least one character set must be selected.")

    all_chars = "".join(char_sets)

    if length < len(required_chars):
        raise ValueError("Password length is too short to satisfy all character set constraints.")

    # Generate remaining characters
    remaining_length = length - len(required_chars)
    password_chars = required_chars + [secrets.choice(all_chars) for _ in range(remaining_length)]

    # Cryptographically secure shuffle
    sys_rand = secrets.SystemRandom()
    sys_rand.shuffle(password_chars)

    return "".join(password_chars)

def evaluate_strength(password: str) -> dict:
    char_set_size = 0
    if any(c in string.ascii_lowercase for c in password):
        char_set_size += 26
    if any(c in string.ascii_uppercase for c in password):
        char_set_size += 26
    if any(c in string.digits for c in password):
        char_set_size += 10
    if any(c in string.punctuation for c in password):
        char_set_size += len(string.punctuation)

    if char_set_size == 0 or len(password) == 0:
        entropy = 0
    else:
        entropy = len(password) * math.log2(char_set_size)

    if entropy < 30:
        score = 0
        feedback = "Very Weak. Too short and lacks variety."
    elif entropy < 50:
        score = 1
        feedback = "Weak. Consider making it longer and adding special characters."
    elif entropy < 70:
        score = 2
        feedback = "Moderate. Good, but could be stronger."
    elif entropy < 100:
        score = 3
        feedback = "Strong. Good password."
    else:
        score = 4
        feedback = "Very Strong. Excellent password."

    return {
        "entropy": entropy,
        "score": score,
        "feedback": feedback
    }
