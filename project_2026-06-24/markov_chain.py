import collections
import secrets

class MarkovChain:
    """
    A simple Markov Chain text generator.
    Builds n-gram state transitions from source text and generates pseudo-random text.
    """

    def __init__(self, n_gram=2):
        self.n_gram = n_gram
        self.transitions = collections.defaultdict(list)
        self.starts = []
        self._rng = secrets.SystemRandom()

    def train(self, text):
        """
        Train the Markov Chain on a given string.
        """
        words = text.split()
        if len(words) <= self.n_gram:
            return

        for i in range(len(words) - self.n_gram):
            state = tuple(words[i:i + self.n_gram])
            next_word = words[i + self.n_gram]
            self.transitions[state].append(next_word)

            # Simple heuristic for a starting point: capitalized words
            if words[i][0].isupper():
                self.starts.append(state)

        # If no capitalized words were found to start, just use all states as possible starts
        if not self.starts:
            self.starts = list(self.transitions.keys())

    def generate(self, max_length=50):
        """
        Generate text up to a maximum length.
        """
        if not self.transitions or not self.starts:
            return ""

        current_state = self._rng.choice(self.starts)
        output = list(current_state)

        for _ in range(max_length - self.n_gram):
            possible_next_words = self.transitions.get(current_state)
            if not possible_next_words:
                break

            next_word = self._rng.choice(possible_next_words)
            output.append(next_word)
            current_state = tuple(output[-self.n_gram:])

        return " ".join(output)

if __name__ == "__main__":
    sample_text = (
        "The quick brown fox jumps over the lazy dog. "
        "The quick brown fox is very fast. "
        "The lazy dog sleeps all day long."
    )
    chain = MarkovChain(n_gram=2)
    chain.train(sample_text)
    print("Generated text:")
    print(chain.generate(20))
