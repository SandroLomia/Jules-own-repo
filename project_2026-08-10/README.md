# Daily Project - 2026-08-10

## Overview

Today's project is a **Markov Chain Text Generator** implemented in Python. A Markov Chain is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. In the context of text generation, it means predicting the next word based on the previous $n$ words (an $n$-gram).

## Implementation Details

The core implementation is found in `markov_chain.py`:

*   **`MarkovChain` Class:** Represents the model. It is initialized with an `n_gram` parameter (default is 2), which determines how many previous words form the current "state".
*   **`build_model(text)`:** Processes an input string, splitting it into words. It maps each sequence of `n_gram` words to a list of possible following words using a `collections.defaultdict(list)`.
*   **`generate_text(length)`:** Starting from a random state in the model, it iteratively selects the next word based on the current state.
*   **Security Context:** For random state and word selection, it utilizes Python's `secrets.choice()` module instead of the standard `random.choice()`. This adheres to best practices by using a cryptographically secure pseudo-random number generator (CSPRNG), although overkill for basic text generation, it demonstrates a commitment to secure coding practices.

## Usage

```python
from markov_chain import MarkovChain

# 1. Initialize the model (e.g., using bigrams)
mc = MarkovChain(n_gram=2)

# 2. Provide a corpus of text
corpus = "this is a test this is only a test of the markov chain generator"
mc.build_model(corpus)

# 3. Generate new text
generated_text = mc.generate_text(length=10)
print(generated_text)
```

## Testing

Unit tests covering initialization, model state building, and text generation constraints are provided in `test_markov_chain.py`.

Run the tests using:
```bash
PYTHONPATH=project_2026-08-10 python3 -m unittest project_2026-08-10/test_markov_chain.py
```