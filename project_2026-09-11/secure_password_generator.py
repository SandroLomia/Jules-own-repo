import string
import secrets

def generate_password(length=16, use_uppercase=True, use_numbers=True, use_special_chars=True):
    """
    Generates a cryptographically secure random password.

    Args:
        length (int): The total length of the password. Default is 16.
        use_uppercase (bool): Whether to include uppercase letters. Default is True.
        use_numbers (bool): Whether to include numbers. Default is True.
        use_special_chars (bool): Whether to include special characters. Default is True.

    Returns:
        str: The generated password.

    Raises:
        ValueError: If length is less than the minimum required length based on selected options.
    """

    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    number_chars = string.digits if use_numbers else ''
    special_chars = string.punctuation if use_special_chars else ''

    # Build the total pool of characters
    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars

    if not all_chars:
         raise ValueError("At least one character set must be selected.")

    # Calculate minimum length to ensure at least one character from each selected set
    min_length = 1 + int(use_uppercase) + int(use_numbers) + int(use_special_chars)
    if length < min_length:
        raise ValueError(f"Password length must be at least {min_length} to satisfy the selected complexity requirements.")

    # Ensure at least one character from each selected pool is included
    password_chars = [secrets.choice(lowercase_chars)]

    if use_uppercase:
        password_chars.append(secrets.choice(uppercase_chars))
    if use_numbers:
        password_chars.append(secrets.choice(number_chars))
    if use_special_chars:
        password_chars.append(secrets.choice(special_chars))

    # Fill the rest of the password length with random characters from the combined pool
    remaining_length = length - len(password_chars)
    password_chars.extend(secrets.choice(all_chars) for _ in range(remaining_length))

    # Shuffle the characters using a cryptographically secure random generator
    secure_random = secrets.SystemRandom()
    secure_random.shuffle(password_chars)

    # Join the list into a string and return
    return ''.join(password_chars)
