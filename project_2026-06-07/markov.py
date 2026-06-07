import secrets
from collections import defaultdict

class MarkovChain:
    """A simple Markov Chain text generator."""

    def __init__(self, state_size=2):
        self.state_size = state_size
        self.model = defaultdict(list)

    def add_text(self, text):
        """Train the model with a given string of text."""
        words = text.split()
        if len(words) <= self.state_size:
            return

        for i in range(len(words) - self.state_size):
            state = tuple(words[i:i + self.state_size])
            next_word = words[i + self.state_size]
            self.model[state].append(next_word)

    def generate_text(self, length=50, start_state=None):
        """Generate text using the Markov chain model."""
        if not self.model:
            return ""

        # Choose a random starting state if none is provided
        if start_state is None:
            start_state = secrets.choice(list(self.model.keys()))

        if start_state not in self.model:
            return ""

        current_state = start_state
        result = list(current_state)

        for _ in range(length - self.state_size):
            next_word_choices = self.model.get(current_state)
            if not next_word_choices:
                break

            # Use secrets.choice instead of random.choice
            next_word = secrets.choice(next_word_choices)
            result.append(next_word)
            current_state = tuple(result[-self.state_size:])

        return " ".join(result)
