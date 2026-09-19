import string
import secrets

def generate_password(length=12, uppercase=True, lowercase=True, numbers=True, special=True):
    """
    Generates a cryptographically secure random password based on the specified criteria.
    """
    if length <= 0:
        raise ValueError("Password length must be greater than 0")

    character_pool = ""
    guaranteed_chars = []

    if uppercase:
        character_pool += string.ascii_uppercase
        guaranteed_chars.append(secrets.choice(string.ascii_uppercase))
    if lowercase:
        character_pool += string.ascii_lowercase
        guaranteed_chars.append(secrets.choice(string.ascii_lowercase))
    if numbers:
        character_pool += string.digits
        guaranteed_chars.append(secrets.choice(string.digits))
    if special:
        character_pool += string.punctuation
        guaranteed_chars.append(secrets.choice(string.punctuation))

    if not character_pool:
        raise ValueError("At least one character type must be selected")

    if length < len(guaranteed_chars):
        raise ValueError(f"Password length must be at least {len(guaranteed_chars)} to satisfy the given criteria")

    # Generate the remaining characters
    remaining_length = length - len(guaranteed_chars)
    remaining_chars = [secrets.choice(character_pool) for _ in range(remaining_length)]

    # Combine guaranteed characters with remaining characters
    password_list = guaranteed_chars + remaining_chars

    # Shuffle the characters using secrets.SystemRandom()
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)

if __name__ == "__main__":
    print(f"Random 12-char password: {generate_password()}")
    print(f"Random 16-char alphanumeric password: {generate_password(length=16, special=False)}")
    print(f"Random 8-char pin: {generate_password(length=8, uppercase=False, lowercase=False, special=False)}")
