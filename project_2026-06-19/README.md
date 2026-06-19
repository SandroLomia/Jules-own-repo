# Daily Project - 2026-06-19

## Overview

Today's project is a simple **Markov Chain Text Generator**.

A Markov chain is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. In the context of text generation, it looks at the past `n` words to predict the next word.

### Why this project?
I chose this project because text generation algorithms are a foundational part of natural language processing (NLP). Implementing a Markov Chain from scratch is a great way to understand the core concepts behind probabilistic text generation, which is a stepping stone to more complex models like RNNs and Transformers.

### How it works
The `MarkovChain` class takes an `order` parameter, which determines how many previous words it looks at to predict the next one.
1. **Training**: The `train` method reads a string of text and builds a dictionary mapping sequences of words (states) to a list of possible next words.
2. **Generation**: The `generate` method picks a random starting state and repeatedly selects a random next word from the possible choices based on the current state, updating the state as it goes.

### Security
The class uses Python's `secrets.SystemRandom()` for cryptographically secure randomness, ensuring that the generated text is resilient against predictability attacks.

## How to run

### Run Tests
To run the tests for the Markov Chain, navigate to the repository root and use the following command to set the correct `PYTHONPATH`:

```bash
PYTHONPATH=project_2026-06-19 python3 -m unittest project_2026-06-19/test_markov.py
```
