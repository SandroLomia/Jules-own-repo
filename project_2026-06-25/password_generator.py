import string
import secrets

class SecurePasswordGenerator:
    """
    A cryptographically secure password generator using the secrets module.
    """
    def __init__(self, include_uppercase=True, include_lowercase=True, include_digits=True, include_symbols=True, custom_symbols=None):
        self.pool = ""
        self.guaranteed_chars = []

        if include_lowercase:
            self.pool += string.ascii_lowercase
            self.guaranteed_chars.append(string.ascii_lowercase)
        if include_uppercase:
            self.pool += string.ascii_uppercase
            self.guaranteed_chars.append(string.ascii_uppercase)
        if include_digits:
            self.pool += string.digits
            self.guaranteed_chars.append(string.digits)
        if include_symbols:
            symbols = custom_symbols if custom_symbols else string.punctuation
            self.pool += symbols
            self.guaranteed_chars.append(symbols)

        if not self.pool:
            raise ValueError("At least one character type must be selected.")

    def generate(self, length=16):
        """
        Generates a password of the specified length.
        Ensures at least one character from each selected category is included.
        """
        if length < len(self.guaranteed_chars):
            raise ValueError(f"Password length must be at least {len(self.guaranteed_chars)} to include all selected character types.")

        password = []

        # Guarantee at least one of each selected type
        for char_set in self.guaranteed_chars:
            password.append(secrets.choice(char_set))

        # Fill the rest randomly from the entire pool
        remaining_length = length - len(self.guaranteed_chars)
        for _ in range(remaining_length):
            password.append(secrets.choice(self.pool))

        # Shuffle the result to prevent predictable patterns (like uppercase always first)
        secrets.SystemRandom().shuffle(password)

        return "".join(password)
