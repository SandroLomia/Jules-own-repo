import secrets
import string

class SecureGenerator:
    """
    A cryptographically secure generator for passwords and passphrases.
    """

    def __init__(self):
        self.rng = secrets.SystemRandom()

    def generate_password(self, length=16, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
        """
        Generates a secure password of a given length, utilizing the specified character sets.
        """
        if length < 4:
            raise ValueError("Password length must be at least 4 characters for sufficient security.")

        char_sets = []
        password = []

        if use_uppercase:
            char_sets.append(string.ascii_uppercase)
            password.append(self.rng.choice(string.ascii_uppercase))
        if use_lowercase:
            char_sets.append(string.ascii_lowercase)
            password.append(self.rng.choice(string.ascii_lowercase))
        if use_digits:
            char_sets.append(string.digits)
            password.append(self.rng.choice(string.digits))
        if use_special:
            char_sets.append(string.punctuation)
            password.append(self.rng.choice(string.punctuation))

        if not char_sets:
            raise ValueError("At least one character set must be selected.")

        all_chars = "".join(char_sets)

        # Fill the rest of the password length
        for _ in range(length - len(password)):
            password.append(self.rng.choice(all_chars))

        # Perform a cryptographically secure shuffle
        self.rng.shuffle(password)

        return "".join(password)

    def generate_passphrase(self, num_words=6, wordlist_file=None):
        """
        Generates a secure passphrase using a wordlist.
        If wordlist_file is not provided, a default hardcoded list of words will be used.
        """
        if num_words < 3:
            raise ValueError("Passphrase must contain at least 3 words.")

        if wordlist_file:
            with open(wordlist_file, 'r') as f:
                words = [line.strip() for line in f if line.strip()]
        else:
            # A fallback list if no file is provided
            words = [
                "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
                "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
                "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam", "zucchini",
                "alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", "hotel", "india",
                "juliett", "kilo", "lima", "mike", "november", "oscar", "papa", "quebec", "romeo",
                "sierra", "tango", "uniform", "victor", "whiskey", "xray", "yankee", "zulu"
            ]

        if not words:
             raise ValueError("Wordlist cannot be empty.")

        passphrase_words = [self.rng.choice(words) for _ in range(num_words)]
        return "-".join(passphrase_words)
