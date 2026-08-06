import secrets
import re

class MarkovChain:
    """
    A simple Markov Chain text generator.
    """
    def __init__(self):
        self.transitions = {}
        self.words = []

    def train(self, text):
        """
        Trains the Markov Chain with the provided text.
        """
        if not text:
            return

        # Simple tokenization: extract words and ignore punctuation
        words = re.findall(r'\w+', text.lower())
        self.words.extend(words)

        if len(words) < 2:
            return

        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]

            if current_word not in self.transitions:
                self.transitions[current_word] = []

            self.transitions[current_word].append(next_word)

    def generate(self, max_words=50):
        """
        Generates text using the trained Markov Chain.
        Uses secrets module for cryptographically secure pseudo-random choices.
        """
        if not self.transitions or not self.words:
            return ""

        secure_random = secrets.SystemRandom()

        # Pick a random starting word
        current_word = secure_random.choice(self.words)
        generated_words = [current_word]

        for _ in range(max_words - 1):
            if current_word in self.transitions and self.transitions[current_word]:
                next_word = secure_random.choice(self.transitions[current_word])
                generated_words.append(next_word)
                current_word = next_word
            else:
                # Dead end reached, stop generating
                break

        return " ".join(generated_words)
