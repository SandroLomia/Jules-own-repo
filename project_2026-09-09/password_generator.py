import string
import secrets

class PasswordGenerator:
    """
    A utility class to generate cryptographically secure passwords.
    """

    @staticmethod
    def generate_password(length: int = 12, use_upper: bool = True, use_lower: bool = True,
                          use_digits: bool = True, use_special: bool = True) -> str:
        """
        Generates a secure password based on the specified criteria.

        Args:
            length (int): The desired length of the password. Minimum is 1.
            use_upper (bool): Whether to include uppercase letters.
            use_lower (bool): Whether to include lowercase letters.
            use_digits (bool): Whether to include digits.
            use_special (bool): Whether to include special characters.

        Returns:
            str: A secure, randomly generated password.

        Raises:
            ValueError: If the length is less than 1, or if no character types are selected.
        """
        if length < 1:
            raise ValueError("Password length must be at least 1.")

        char_pools = []
        if use_upper:
            char_pools.append(string.ascii_uppercase)
        if use_lower:
            char_pools.append(string.ascii_lowercase)
        if use_digits:
            char_pools.append(string.digits)
        if use_special:
            char_pools.append(string.punctuation)

        if not char_pools:
            raise ValueError("At least one character type must be selected.")

        all_chars = "".join(char_pools)

        password_chars = []
        # Ensure at least one character from each selected pool is included
        for pool in char_pools:
            password_chars.append(secrets.choice(pool))

        # Fill the rest of the password length with random choices from all selected pools
        remaining_length = length - len(password_chars)
        for _ in range(remaining_length):
            password_chars.append(secrets.choice(all_chars))

        # If the requested length was less than the number of selected pools,
        # we need to truncate. We shuffle first to ensure randomness of which types remain.
        secrets.SystemRandom().shuffle(password_chars)
        password_chars = password_chars[:length]

        # Shuffle again to randomize the position of the guaranteed characters
        secrets.SystemRandom().shuffle(password_chars)

        return "".join(password_chars)
