import secrets

class MarkovChain:
    """
    A simple Markov Chain implementation for generating text based on statistical probabilities.
    Uses cryptographically secure randomness via the `secrets` module.
    """

    def __init__(self, order: int = 1):
        """
        Initializes the Markov Chain.

        Args:
            order (int): The number of words that comprise a state (the lookback length).
        """
        if order < 1:
            raise ValueError("Order must be at least 1.")
        self.order = order
        self.state_dict = {}

    def train(self, text: str):
        """
        Trains the Markov Chain on the provided text.

        Args:
            text (str): The input text corpus to train on.
        """
        if not text:
            return

        words = text.split()
        if len(words) <= self.order:
            return

        for i in range(len(words) - self.order):
            state = tuple(words[i:i + self.order])
            next_word = words[i + self.order]

            if state not in self.state_dict:
                self.state_dict[state] = []
            self.state_dict[state].append(next_word)

    def generate(self, max_words: int = 50) -> str:
        """
        Generates text using the trained Markov Chain.

        Args:
            max_words (int): The maximum number of words to generate.

        Returns:
            str: The generated text sequence.
        """
        if not self.state_dict:
            return ""

        # Choose a random starting state
        current_state = secrets.choice(list(self.state_dict.keys()))
        generated_words = list(current_state)

        for _ in range(max_words - self.order):
            if current_state not in self.state_dict:
                break

            possible_next_words = self.state_dict[current_state]
            next_word = secrets.choice(possible_next_words)

            generated_words.append(next_word)
            current_state = tuple(generated_words[-self.order:])

        return " ".join(generated_words)
