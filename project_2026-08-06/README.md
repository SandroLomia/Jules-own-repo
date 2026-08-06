# Daily Project - 2026-08-06: Markov Chain Text Generator

## Overview

Today's project is a Python implementation of a simple Markov Chain algorithm for generating text. It learns word transitions from a provided input text and can then generate new pseudo-random text sequences that loosely mimic the style and structure of the original input.

### Features
*   **Tokenization:** Simple regex-based tokenization ignoring punctuation and lowercasing inputs.
*   **State Mapping:** Builds a dictionary mapping a given word to all subsequent words that followed it in the training data.
*   **Secure Generation:** Uses Python's `secrets.SystemRandom` for cryptographically secure pseudo-random selections when generating the chain, ensuring robust randomness.

## Usage

```python
from markov_chain import MarkovChain

# Initialize the chain
mc = MarkovChain()

# Train with some text
text = "The quick brown fox jumps over the lazy dog. The quick red fox runs."
mc.train(text)

# Generate new text (default max 50 words)
generated_text = mc.generate(max_words=10)
print(generated_text)
```

## Running Tests

To run the test suite for this module from the repository root:

```bash
PYTHONPATH=project_2026-08-06 python3 -m unittest project_2026-08-06/test_markov_chain.py
```
