import secrets
import string

class PasswordGenerator:
    """
    A utility class to generate cryptographically secure random passwords.
    """

    def generate(self, length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
        """
        Generates a secure password based on the provided constraints.

        Args:
            length (int): Length of the password. Minimum length will be enforced to be at least the number of enabled character types.
            use_upper (bool): Whether to include uppercase letters.
            use_lower (bool): Whether to include lowercase letters.
            use_digits (bool): Whether to include digits.
            use_symbols (bool): Whether to include symbols.

        Returns:
            str: The generated password.

        Raises:
            ValueError: If no character types are selected or if the requested length is too small for the selected types.
        """
        if not any([use_upper, use_lower, use_digits, use_symbols]):
            raise ValueError("At least one character type must be selected.")

        char_pools = []
        mandatory_chars = []

        if use_upper:
            char_pools.append(string.ascii_uppercase)
            mandatory_chars.append(secrets.choice(string.ascii_uppercase))
        if use_lower:
            char_pools.append(string.ascii_lowercase)
            mandatory_chars.append(secrets.choice(string.ascii_lowercase))
        if use_digits:
            char_pools.append(string.digits)
            mandatory_chars.append(secrets.choice(string.digits))
        if use_symbols:
            char_pools.append(string.punctuation)
            mandatory_chars.append(secrets.choice(string.punctuation))

        if length < len(mandatory_chars):
            raise ValueError(f"Length {length} is too short to satisfy the selected constraints.")

        all_chars = "".join(char_pools)

        # Fill the rest of the password length
        remaining_length = length - len(mandatory_chars)
        password_chars = mandatory_chars + [secrets.choice(all_chars) for _ in range(remaining_length)]

        # Cryptographically secure shuffle
        secrets.SystemRandom().shuffle(password_chars)

        return "".join(password_chars)

if __name__ == "__main__":
    generator = PasswordGenerator()
    print("Example secure password:", generator.generate(16))
