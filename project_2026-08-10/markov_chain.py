import secrets
import collections

class MarkovChain:
    """
    A simple Markov Chain text generator.
    """
    def __init__(self, n_gram=2):
        self.n_gram = n_gram
        self.state_dict = collections.defaultdict(list)

    def build_model(self, text):
        """
        Builds the Markov chain model from the provided text.
        """
        if not text:
            return

        words = text.split()
        if len(words) < self.n_gram:
            return

        for i in range(len(words) - self.n_gram):
            state = tuple(words[i:i + self.n_gram])
            next_word = words[i + self.n_gram]
            self.state_dict[state].append(next_word)

    def generate_text(self, length=50):
        """
        Generates text using the built Markov chain model.
        Uses secrets.choice for cryptographically secure random selection.
        """
        if not self.state_dict:
            return ""

        # Choose a random starting state securely
        current_state = secrets.choice(list(self.state_dict.keys()))
        output = list(current_state)

        for _ in range(length - self.n_gram):
            possible_next_words = self.state_dict.get(current_state)
            if not possible_next_words:
                break

            # Securely choose the next word
            next_word = secrets.choice(possible_next_words)
            output.append(next_word)
            current_state = tuple(output[-self.n_gram:])

        return " ".join(output)
