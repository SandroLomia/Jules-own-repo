import secrets
from collections import defaultdict

class MarkovChain:
    def __init__(self, order=1):
        self.order = order
        self.model = defaultdict(list)

    def train(self, text):
        """Train the Markov Chain model on the given text."""
        words = text.split()
        if len(words) <= self.order:
            return

        for i in range(len(words) - self.order):
            state = tuple(words[i:i+self.order])
            next_word = words[i+self.order]
            self.model[state].append(next_word)

    def generate(self, length=20, start_state=None):
        """Generate text using the trained model."""
        if not self.model:
            return ""

        if start_state is None or start_state not in self.model:
            start_state = secrets.choice(list(self.model.keys()))

        current_state = start_state
        output = list(current_state)

        for _ in range(length - self.order):
            if current_state not in self.model:
                break

            next_word = secrets.choice(self.model[current_state])
            output.append(next_word)
            current_state = tuple(output[-self.order:])

        return " ".join(output)

if __name__ == "__main__":
    sample_text = "I am a helpful assistant. I am a software engineer. I am here to write code."
    mc = MarkovChain(order=1)
    mc.train(sample_text)
    print("Generated text:", mc.generate(length=10))
