import secrets
import string

def generate_password(length: int = 12, use_upper: bool = True, use_lower: bool = True, use_numbers: bool = True, use_special: bool = True) -> str:
    """
    Generates a cryptographically secure password based on given constraints.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0.")
    if not any([use_upper, use_lower, use_numbers, use_special]):
        raise ValueError("At least one character type must be selected.")

    characters = ""
    password = []

    if use_upper:
        characters += string.ascii_uppercase
        password.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        characters += string.ascii_lowercase
        password.append(secrets.choice(string.ascii_lowercase))
    if use_numbers:
        characters += string.digits
        password.append(secrets.choice(string.digits))
    if use_special:
        characters += string.punctuation
        password.append(secrets.choice(string.punctuation))

    if length < len(password):
        raise ValueError("Length is too short to satisfy the character type constraints.")

    # Fill the remaining length
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(secrets.choice(characters))

    # Securely shuffle the result
    secrets.SystemRandom().shuffle(password)

    return "".join(password)

if __name__ == "__main__":
    print(generate_password())
