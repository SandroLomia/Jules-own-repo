import secrets
from collections import defaultdict

class MarkovChain:
    """A Markov Chain text generator."""

    def __init__(self, order=1):
        """
        Initializes the Markov Chain model.

        Args:
            order (int): The number of preceding words used to determine the next word.
                         Higher order means more coherent but less random text.
        """
        self.order = order
        self.model = defaultdict(list)
        self.secure_random = secrets.SystemRandom()

    def train(self, text):
        """
        Trains the Markov Chain model on the given text.

        Args:
            text (str): The text corpus to train on.
        """
        if not text:
            return

        words = text.split()
        if len(words) <= self.order:
            return

        for i in range(len(words) - self.order):
            state = tuple(words[i : i + self.order])
            next_word = words[i + self.order]
            self.model[state].append(next_word)

    def generate(self, max_length=50, seed_state=None):
        """
        Generates text using the trained Markov Chain model.

        Args:
            max_length (int): The maximum number of words to generate.
            seed_state (tuple): The starting state (tuple of words).
                                If None, a random state is chosen.

        Returns:
            str: The generated text.
        """
        if not self.model:
            return ""

        if seed_state and seed_state in self.model:
            current_state = seed_state
        else:
            current_state = self.secure_random.choice(list(self.model.keys()))

        generated_words = list(current_state)

        while len(generated_words) < max_length:
            possible_next_words = self.model.get(current_state)
            if not possible_next_words:
                break

            next_word = self.secure_random.choice(possible_next_words)
            generated_words.append(next_word)
            current_state = tuple(generated_words[-self.order:])

        return " ".join(generated_words)
