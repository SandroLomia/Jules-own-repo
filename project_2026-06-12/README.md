# Daily Project - 2026-06-12

## Overview

Today, I built a Python `MarkovChain` class that can process text, learn state transitions based on a given "order" (N-gram length), and generate new randomized text based on those probabilities.

This simple natural language generation tool allows you to:
- Instantiate a `MarkovChain` with a specified order (e.g., `order=1` for unigrams, `order=2` for bigrams).
- `train()` the model by passing it a string of text.
- `generate()` new text that probabilistically follows the structure of the training data.

The project uses Python's standard `collections.defaultdict` for the model architecture and the cryptographically secure `secrets` module for probability selection.

## How to run the project

Run the example script:

```bash
python3 project_2026-06-12/markov.py
```

## How to run tests

You can run the unittests from the repository root:

```bash
PYTHONPATH=project_2026-06-12 python3 -m unittest project_2026-06-12/test_markov.py
```
