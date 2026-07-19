import secrets
import string

class SecureGenerator:
    """
    A utility class for generating cryptographically secure values
    using the 'secrets' module instead of the standard 'random' module.
    """

    @staticmethod
    def generate_password(length: int = 16, use_symbols: bool = True) -> str:
        """
        Generates a cryptographically secure random password.

        Args:
            length (int): Length of the generated password.
            use_symbols (bool): Whether to include symbols in the password.

        Returns:
            str: A securely generated password string.
        """
        if length < 1:
            raise ValueError("Password length must be at least 1")

        characters = string.ascii_letters + string.digits
        if use_symbols:
            characters += string.punctuation

        return "".join(secrets.choice(characters) for _ in range(length))

    @staticmethod
    def secure_shuffle(data_list: list) -> list:
        """
        Performs a cryptographically secure shuffle of a list.
        Note: secrets.SystemRandom().shuffle() works in-place, but this method
        returns the modified list for convenience.

        Args:
            data_list (list): The list to be shuffled.

        Returns:
            list: The securely shuffled list (modifies in-place as well).
        """
        if not isinstance(data_list, list):
            raise TypeError("Input must be a list")

        secrets.SystemRandom().shuffle(data_list)
        return data_list
