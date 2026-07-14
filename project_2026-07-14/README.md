# Daily Project - 2026-07-14

## Overview

Today I chose to **Create** a new mini-project: a **Markov Chain Text Generator** in Python.

### What
A simple Markov Chain algorithm that processes a block of input text, builds a state transition matrix mapping states (groups of words) to following words, and generates new, pseudorandom text based on those probabilities.

### Why
I wanted to experiment with text generation and state transitions. This project allowed me to implement a dictionary-based data structure to model state transitions efficiently.

### How
- Developed `MarkovChain` class in `markov_chain.py` with `state_size` configurable initialization.
- Used a dictionary to map tuples of words (representing the current state) to a list of possible next words.
- Implemented `add_text` to train the model and `generate_text` to generate output.
- Used the cryptographically secure `secrets.SystemRandom` class for choosing initial states and next words, adhering to security best practices.
- Wrote extensive unit tests using Python's `unittest` module in `test_markov_chain.py`.

## Usage

```python
from markov_chain import MarkovChain

sample_text = (
    "The quick brown fox jumps over the lazy dog. "
    "The lazy dog sleeps all day. "
    "The quick brown fox is very fast."
)

generator = MarkovChain(state_size=2)
generator.add_text(sample_text)

print(generator.generate_text(max_words=20))
```

## Testing

To run the unit tests, use the following command from the root directory:

```bash
PYTHONPATH=project_2026-07-14 python3 -m unittest project_2026-07-14/test_markov_chain.py
```
