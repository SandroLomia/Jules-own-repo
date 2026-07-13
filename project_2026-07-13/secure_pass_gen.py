import secrets
import string
from typing import List

class PasswordGenerator:
    """
    A utility class to generate cryptographically secure passwords and passphrases
    using Python's `secrets` module.
    """

    @staticmethod
    def generate_password(length: int = 16, use_upper: bool = True, use_lower: bool = True,
                          use_digits: bool = True, use_special: bool = True) -> str:
        """
        Generates a secure password.

        Args:
            length (int): The length of the password.
            use_upper (bool): Whether to include uppercase letters.
            use_lower (bool): Whether to include lowercase letters.
            use_digits (bool): Whether to include digits.
            use_special (bool): Whether to include special characters.

        Returns:
            str: The generated password.

        Raises:
            ValueError: If no character types are selected or length is <= 0.
        """
        if length <= 0:
            raise ValueError("Password length must be greater than 0.")

        character_pool = ""
        required_chars = []

        if use_upper:
            character_pool += string.ascii_uppercase
            required_chars.append(secrets.choice(string.ascii_uppercase))
        if use_lower:
            character_pool += string.ascii_lowercase
            required_chars.append(secrets.choice(string.ascii_lowercase))
        if use_digits:
            character_pool += string.digits
            required_chars.append(secrets.choice(string.digits))
        if use_special:
            character_pool += string.punctuation
            required_chars.append(secrets.choice(string.punctuation))

        if not character_pool:
            raise ValueError("At least one character type must be selected.")

        if length < len(required_chars):
            raise ValueError("Password length is too short to satisfy all required character types.")

        # Fill the rest of the password
        remaining_length = length - len(required_chars)
        password_chars = required_chars + [secrets.choice(character_pool) for _ in range(remaining_length)]

        # Securely shuffle the password characters
        secrets.SystemRandom().shuffle(password_chars)

        return "".join(password_chars)

    @staticmethod
    def generate_passphrase(num_words: int, wordlist: List[str], separator: str = "-") -> str:
        """
        Generates a secure passphrase.

        Args:
            num_words (int): The number of words to include in the passphrase.
            wordlist (List[str]): A list of words to choose from.
            separator (str): The separator to use between words.

        Returns:
            str: The generated passphrase.

        Raises:
            ValueError: If num_words <= 0 or wordlist is empty.
        """
        if num_words <= 0:
            raise ValueError("Number of words must be greater than 0.")
        if not wordlist:
            raise ValueError("Wordlist cannot be empty.")

        words = [secrets.choice(wordlist) for _ in range(num_words)]
        return separator.join(words)
