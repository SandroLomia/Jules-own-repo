# Daily Project - 2026-10-24

## Overview

Today's project is a **Markov Chain Text Generator**.

A Markov Chain is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. In the context of text generation, it uses a corpus of text to learn the probabilities of which word follows a sequence of preceding words, and uses this information to generate new text that mimics the style of the original corpus.

### Features
* **Variable Order:** The generator supports different "orders". An order of 1 means the next word is chosen based solely on the previous word. An order of 2 looks at the previous two words, generally resulting in more coherent (but less random) text.
* **Secure Randomness:** Utilizes Python's `secrets` module instead of `random` for cryptographically secure random selections during text generation.
* **Comprehensive Testing:** Fully tested using Python's `unittest` framework to ensure proper state-building and probabilistic generation logic.

## Usage

```python
from markov_chain import MarkovChain

# Initialize the model (default order is 1)
model = MarkovChain(order=2)

# Train the model with some text
corpus = "the quick brown fox jumps over the lazy dog the quick brown cat"
model.train(corpus)

# Generate new text (up to max_length words)
generated_text = model.generate(max_length=10)
print(generated_text)
```

## Running Tests

From the repository root, run:
```bash
PYTHONPATH=project_2026-10-24 python3 -m unittest project_2026-10-24/test_markov_chain.py
```