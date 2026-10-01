# Daily Project - 2026-10-01: Markov Chain Text Generator

## Overview

Today's project is a Python implementation of a **Markov Chain Text Generator**.

A Markov Chain is a stochastic model that models a sequence of events where the probability of each event depends only on the state attained in the previous event. In the context of text generation, it means generating a sequence of words where each word is chosen based on the preceding word(s).

This implementation:
- Uses the cryptographically secure `secrets` module to pick random next words, avoiding the standard `random` module for better security practices.
- Supports variable "order" (lookback length), meaning the state can be composed of $n$ previous words rather than just one.
- Includes comprehensive unit tests.

## Files

- `markov_chain.py`: The core logic containing the `MarkovChain` class.
- `test_markov_chain.py`: The `unittest` test suite verifying the behavior of the class.

## How to Run the Tests

From the root directory of the repository, execute:

```bash
PYTHONPATH=project_2026-10-01 python3 -m unittest project_2026-10-01/test_markov_chain.py
```
