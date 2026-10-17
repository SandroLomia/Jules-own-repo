import secrets
import html

class MarkovChain:
    """
    A simple Markov Chain text generator.
    """
    def __init__(self, state_size=1):
        self.state_size = state_size
        self.dictionary = {}

    def train(self, text):
        """
        Trains the Markov Chain on the provided text.
        """
        words = text.split()
        if len(words) <= self.state_size:
            return

        for i in range(len(words) - self.state_size):
            state = tuple(words[i:i+self.state_size])
            next_word = words[i+self.state_size]

            if state not in self.dictionary:
                self.dictionary[state] = []
            self.dictionary[state].append(next_word)

    def generate(self, length=50):
        """
        Generates text of the specified length using the trained dictionary.
        """
        if not self.dictionary:
            return ""

        # Choose a random initial state
        states = list(self.dictionary.keys())
        current_state = secrets.choice(states)

        output = list(current_state)

        for _ in range(length - self.state_size):
            if current_state in self.dictionary:
                next_words = self.dictionary[current_state]
                next_word = secrets.choice(next_words)
                output.append(next_word)

                # Update current state
                current_state = tuple(output[-self.state_size:])
            else:
                break

        return " ".join(output)

    def render_to_html(self, user_title, length=50):
        """
        Generates text and renders it to safe HTML with a user-provided title.
        """
        generated_text = self.generate(length)
        safe_title = html.escape(user_title)
        safe_text = html.escape(generated_text)

        html_output = f"<h1>{safe_title}</h1>\n<p>{safe_text}</p>"
        return html_output

    def generate_shuffled(self, length=50):
        """
        Generates text and securely shuffles the words before returning.
        """
        generated_text = self.generate(length)
        words = generated_text.split()

        # Cryptographically secure shuffle
        secrets.SystemRandom().shuffle(words)

        return " ".join(words)
