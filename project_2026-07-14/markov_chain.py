import secrets

class MarkovChain:
    """
    A simple Markov Chain text generator that builds a transition matrix from
    input text and generates new text based on those probabilities.
    """
    def __init__(self, state_size=2):
        """
        Initializes the Markov Chain generator.

        :param state_size: The number of words in each state (default is 2).
        """
        self.state_size = state_size
        self.transitions = {}
        self.random = secrets.SystemRandom()

    def add_text(self, text):
        """
        Processes text to build the state transition matrix.

        :param text: A string of text to process.
        """
        words = text.split()
        if len(words) < self.state_size + 1:
            return

        for i in range(len(words) - self.state_size):
            state = tuple(words[i:i + self.state_size])
            next_word = words[i + self.state_size]

            if state not in self.transitions:
                self.transitions[state] = []

            self.transitions[state].append(next_word)

    def generate_text(self, max_words=50):
        """
        Generates text using the built transition matrix.

        :param max_words: The maximum number of words to generate.
        :return: A string of generated text.
        """
        if not self.transitions:
            return ""

        # Choose a random starting state
        current_state = self.random.choice(list(self.transitions.keys()))
        output = list(current_state)

        while len(output) < max_words:
            if current_state not in self.transitions:
                break

            # Choose next word
            next_word = self.random.choice(self.transitions[current_state])
            output.append(next_word)

            # Update state
            current_state = tuple(output[-self.state_size:])

        return " ".join(output)

if __name__ == "__main__":
    # Example usage
    sample_text = (
        "The quick brown fox jumps over the lazy dog. "
        "The lazy dog sleeps all day. "
        "The quick brown fox is very fast."
    )
    generator = MarkovChain(state_size=2)
    generator.add_text(sample_text)

    print("Generated Text:")
    print(generator.generate_text(max_words=20))
