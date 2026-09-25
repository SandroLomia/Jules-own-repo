import string
import secrets

class PasswordGenerator:
    """
    A class for generating cryptographically secure random passwords.
    """

    @staticmethod
    def generate(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
        """
        Generates a secure random password with the specified length and character classes.

        Args:
            length (int): Total length of the password. Minimum length is the number of enabled character classes.
            use_uppercase (bool): Whether to include uppercase letters.
            use_lowercase (bool): Whether to include lowercase letters.
            use_digits (bool): Whether to include digits.
            use_special (bool): Whether to include special characters.

        Returns:
            str: The generated password.

        Raises:
            ValueError: If no character classes are selected, or if length is too short to satisfy requirements.
        """
        if not any([use_uppercase, use_lowercase, use_digits, use_special]):
            raise ValueError("At least one character class must be selected.")

        pool = []
        password_chars = []

        if use_uppercase:
            pool.append(string.ascii_uppercase)
            password_chars.append(secrets.choice(string.ascii_uppercase))

        if use_lowercase:
            pool.append(string.ascii_lowercase)
            password_chars.append(secrets.choice(string.ascii_lowercase))

        if use_digits:
            pool.append(string.digits)
            password_chars.append(secrets.choice(string.digits))

        if use_special:
            pool.append(string.punctuation)
            password_chars.append(secrets.choice(string.punctuation))

        if length < len(password_chars):
            raise ValueError(f"Password length ({length}) is too short to satisfy the selected character classes ({len(password_chars)}).")

        full_pool = "".join(pool)

        while len(password_chars) < length:
            password_chars.append(secrets.choice(full_pool))

        # Securely shuffle the password characters
        secrets.SystemRandom().shuffle(password_chars)

        return "".join(password_chars)
