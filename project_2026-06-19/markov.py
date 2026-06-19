import secrets
from collections import defaultdict

class MarkovChain:
    """
    A simple Markov Chain text generator.
    """

    def __init__(self, order=1):
        self.order = order
        self.transitions = defaultdict(list)
        self.starts = []
        self._random = secrets.SystemRandom()

    def train(self, text):
        """
        Trains the Markov chain on a string of text.
        """
        words = text.split()
        if len(words) < self.order:
            return

        # Record possible starting states (we consider the first n words)
        start_state = tuple(words[:self.order])
        self.starts.append(start_state)

        for i in range(len(words) - self.order):
            state = tuple(words[i : i + self.order])
            next_word = words[i + self.order]
            self.transitions[state].append(next_word)

    def generate(self, length=20):
        """
        Generates text of the specified length.
        """
        if not self.starts:
            return ""

        current_state = self._random.choice(self.starts)
        output = list(current_state)

        for _ in range(length - self.order):
            possible_next_words = self.transitions.get(current_state)
            if not possible_next_words:
                break

            next_word = self._random.choice(possible_next_words)
            output.append(next_word)
            current_state = tuple(output[-self.order:])

        return " ".join(output)
