# Project 2026-06-24: Markov Chain Text Generator

## Overview
This project implements a simple Markov Chain text generator in Python. It builds n-gram state transitions from source text and generates pseudo-random text based on those probabilities. It uses the `secrets` module for cryptographically secure pseudo-randomness during generation.

## Features
- Dynamic n-gram size configuration.
- Simple heuristic for identifying sentence starters.
- Cryptographically secure pseudo-random number generator for state transitions.

## How to Run
To run the example usage directly from the script:

```bash
python3 markov_chain.py
```

To run the unit tests:

```bash
PYTHONPATH=. python3 -m unittest test_markov_chain.py
```
