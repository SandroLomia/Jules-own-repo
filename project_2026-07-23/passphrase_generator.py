import math
import secrets

class SecurePassphraseGenerator:
    """
    A utility for generating cryptographically secure passphrases from a given word list.
    """

    DEFAULT_WORD_LIST = [
        "apple", "banana", "cherry", "dragonfruit", "elephant",
        "falcon", "giraffe", "horizon", "igloo", "jungle",
        "kangaroo", "lemon", "mountain", "nebula", "ocean",
        "panther", "quasar", "river", "sunflower", "tiger",
        "umbrella", "volcano", "waterfall", "xylophone", "yacht", "zebra"
    ]

    def __init__(self, word_list=None):
        if word_list is None:
            self.word_list = self.DEFAULT_WORD_LIST
        else:
            self.word_list = word_list

        if not self.word_list:
            raise ValueError("Word list cannot be empty.")

    def generate_passphrase(self, num_words=4, separator='-', unique=False):
        """
        Generates a secure passphrase.

        Args:
            num_words (int): The number of words in the passphrase.
            separator (str): The string used to separate words.
            unique (bool): If True, ensures words do not repeat in the passphrase.
                           Requires num_words to be <= len(word_list).

        Returns:
            str: The generated passphrase.
        """
        if num_words <= 0:
            raise ValueError("Number of words must be greater than 0.")

        if unique:
            if num_words > len(self.word_list):
                raise ValueError("Cannot pick more unique words than the word list contains.")

            # Use SystemRandom to shuffle a copy of the list securely
            shuffled_list = self.word_list.copy()
            secrets.SystemRandom().shuffle(shuffled_list)
            selected_words = shuffled_list[:num_words]
        else:
            selected_words = [secrets.choice(self.word_list) for _ in range(num_words)]

        return separator.join(selected_words)

    def evaluate_entropy(self, num_words):
        """
        Calculates the theoretical entropy of the generated passphrase.

        Args:
            num_words (int): The number of words in the passphrase.

        Returns:
            float: The entropy in bits.
        """
        if num_words <= 0:
            return 0.0

        words_count = len(self.word_list)
        if words_count <= 1:
            return 0.0

        # Entropy per word is log2(pool size)
        # Total entropy is num_words * log2(pool size)
        entropy = num_words * math.log2(words_count)
        return entropy
