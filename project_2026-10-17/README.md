# Markov Chain Text Generator

## Overview

This project implements a simple, robust Markov Chain text generator in Python. It builds a state-based frequency dictionary from input text and generates statistically similar text.

## Features

- **State Size Customization:** The `MarkovChain` can be initialized with a custom `state_size` (default is 1), determining how many preceding words define the current state.
- **Secure Randomness:** Uses Python's `secrets` module for cryptographically secure random selections during generation.
- **Safe HTML Rendering:** Includes a `render_to_html` method that escapes potentially harmful user input using `html.escape()` to prevent Cross-Site Scripting (XSS) when rendering the generated text within a web context.
- **Secure Shuffling:** The `generate_shuffled` method uses `secrets.SystemRandom().shuffle()` for a cryptographically secure randomization of the generated text's word order.

## Usage

```python
from markov_chain import MarkovChain

# Initialize
mc = MarkovChain(state_size=2)

# Train the model
text = "the quick brown fox jumps over the lazy dog and the quick brown cat jumps over the lazy mouse"
mc.train(text)

# Generate text
generated = mc.generate(length=10)
print(f"Generated text: {generated}")

# Render to HTML safely
html_output = mc.render_to_html(user_title="My AI Story", length=5)
print(html_output)

# Generate and shuffle securely
shuffled = mc.generate_shuffled(length=5)
print(f"Shuffled text: {shuffled}")
```

## Running Tests

To run the test suite, use the following command from the project root:

```bash
PYTHONPATH=. python3 -m unittest test_markov_chain.py
```
