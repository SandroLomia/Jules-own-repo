import secrets
import string

def generate_password(length: int = 12, use_symbols: bool = True, use_numbers: bool = True, use_uppercase: bool = True) -> str:
    """
    Generates a cryptographically secure password.
    """
    if length < 1:
        raise ValueError("Password length must be at least 1")

    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    number_chars = string.digits if use_numbers else ''
    symbol_chars = string.punctuation if use_symbols else ''

    all_chars = lowercase_chars + uppercase_chars + number_chars + symbol_chars

    if not all_chars:
        raise ValueError("At least one character set must be selected")

    password_chars = []

    # Ensure at least one character from each selected set is included
    if use_uppercase:
        password_chars.append(secrets.choice(uppercase_chars))
    if use_numbers:
        password_chars.append(secrets.choice(number_chars))
    if use_symbols:
        password_chars.append(secrets.choice(symbol_chars))
    password_chars.append(secrets.choice(lowercase_chars))

    # Fill the rest of the password
    while len(password_chars) < length:
        password_chars.append(secrets.choice(all_chars))

    # Shuffle the characters using cryptographically secure method
    sys_rand = secrets.SystemRandom()
    sys_rand.shuffle(password_chars)

    # Trim to length if it exceeds (can happen if requested length is small but many options are true)
    return ''.join(password_chars[:length])

if __name__ == "__main__":
    print(generate_password())