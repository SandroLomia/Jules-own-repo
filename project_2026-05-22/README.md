# Daily Project - 2026-05-22

## Overview

This project implements a simple **Markov Chain Text Generator**. It trains on provided text using an n-gram model and generates random text that mimics the style and structure of the input.

## How it works

The `MarkovChain` class takes an `order` (the size of the n-gram). During training, it records all sequences of `order` words and maps them to the following word. During generation, it picks a starting sequence and randomly selects the next word based on the frequencies observed during training, continuously shifting the window of words to generate new text.

## Usage

```python
from markov_chain import MarkovChain

# Initialize a Markov chain with order 2
mc = MarkovChain(order=2)

# Train on some text
text = "I love learning about artificial intelligence. Artificial intelligence is a fascinating field."
mc.train(text)

# Generate new text
generated_text = mc.generate(max_words=10)
print(generated_text)
```

## Running Tests

To run the unit tests, execute the following from the repository root:

```bash
PYTHONPATH=project_2026-05-22 python3 -m unittest project_2026-05-22/test_markov_chain.py
```
