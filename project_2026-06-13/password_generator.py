import secrets
import string

class PasswordGenerator:
    """
    A class to generate cryptographically secure passwords.
    """

    def __init__(self, use_lower=True, use_upper=True, use_digits=True, use_special=True):
        self.use_lower = use_lower
        self.use_upper = use_upper
        self.use_digits = use_digits
        self.use_special = use_special

    def generate(self, length=16):
        """
        Generates a secure password of the specified length.
        Guarantees at least one character from each selected type if length allows.
        """
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")

        pools = []
        if self.use_lower:
            pools.append(string.ascii_lowercase)
        if self.use_upper:
            pools.append(string.ascii_uppercase)
        if self.use_digits:
            pools.append(string.digits)
        if self.use_special:
            pools.append(string.punctuation)

        if not pools:
            raise ValueError("At least one character type must be selected.")

        password_chars = []

        # Ensure at least one character from each pool
        for pool in pools:
            password_chars.append(secrets.choice(pool))

        # Fill the remaining length with random choices from the combined pool
        combined_pool = "".join(pools)
        while len(password_chars) < length:
            password_chars.append(secrets.choice(combined_pool))

        # Shuffle the password characters to avoid predictable patterns
        secure_random = secrets.SystemRandom()
        secure_random.shuffle(password_chars)

        # Truncate if requested length is smaller than the number of pools
        return "".join(password_chars[:length])

if __name__ == "__main__":
    generator = PasswordGenerator()
    print(f"Generated Password: {generator.generate(20)}")
