import random
from collections import defaultdict
from typing import List, Dict, Optional

class MarkovChain:
    """
    A simple n-gram Markov Chain text generator.
    """
    def __init__(self, order: int = 2):
        """
        Initializes the Markov Chain with a given order (n-gram size).
        """
        if order < 1:
            raise ValueError("Order must be at least 1.")
        self.order = order
        self.chain: Dict[tuple, List[str]] = defaultdict(list)
        self.starts: List[tuple] = []

    def train(self, text: str) -> None:
        """
        Trains the Markov model on the provided text.
        """
        words = text.split()
        if len(words) <= self.order:
            return

        # Record possible starting states (we consider the first `order` words a starting state)
        # We can also consider starts of sentences. For simplicity, just use the beginning of the text.
        # A more robust version would split by sentences.
        self.starts.append(tuple(words[:self.order]))

        for i in range(len(words) - self.order):
            state = tuple(words[i : i + self.order])
            next_word = words[i + self.order]
            self.chain[state].append(next_word)

    def generate(self, max_words: int = 50, start_state: Optional[tuple] = None) -> str:
        """
        Generates text using the trained Markov model.
        """
        if not self.chain and not self.starts:
            return ""

        # Choose a starting state
        if start_state and start_state in self.chain:
            current_state = start_state
        elif self.starts:
            current_state = random.choice(self.starts)
        elif self.chain:
             current_state = random.choice(list(self.chain.keys()))
        else:
             return ""

        generated_words = list(current_state)

        for _ in range(max_words - self.order):
            if current_state not in self.chain or not self.chain[current_state]:
                break # Reached a dead end

            next_word = random.choice(self.chain[current_state])
            generated_words.append(next_word)

            # Shift state
            current_state = tuple(generated_words[-self.order:])

        return " ".join(generated_words)
