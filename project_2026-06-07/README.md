# Markov Chain Text Generator

## Overview

This project implements a simple Markov Chain text generator. It models word state transitions from an input text corpus and uses statistical probability to generate new, pseudo-random text that mimics the structure of the original input.

## How it works

The `MarkovChain` class takes an optional `state_size` parameter (default 2).

1. **Training:** `add_text("some text corpus")` parses text into words and maps each sequence of `state_size` words to the list of possible subsequent words.
2. **Generating:** `generate_text(length)` picks a starting state (or uses a provided one) and repeatedly selects the next word randomly from the possible transitions for the current state, ensuring cryptographic security via the `secrets` module.

## Usage

```python
from markov import MarkovChain

# Initialize
generator = MarkovChain(state_size=2)

# Train
generator.add_text("I love writing code. Writing code is incredibly fun and rewarding.")

# Generate
new_text = generator.generate_text(length=10)
print(new_text)
```

## Running Tests

Tests can be run using the standard Python `unittest` framework:

```bash
PYTHONPATH=project_2026-06-07 python3 -m unittest project_2026-06-07/test_markov.py
```