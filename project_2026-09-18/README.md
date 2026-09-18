# Daily Project - 2026-09-18

## Overview

Today's project is a **Text Similarity Utility**.

This Python module provides a simple implementation of Cosine Similarity using basic term frequencies (TF) to calculate how similar two pieces of text are. It takes two strings as input, tokenizes them, counts word frequencies, and computes the cosine of the angle between the two resulting text vectors.

The result is a floating-point score between `0.0` (no words in common) and `1.0` (identical word frequencies).

### Features
* Simple tokenization (case-insensitive, strips punctuation).
* Fast computation of term frequencies using `collections.Counter`.
* Vector magnitude calculation and dot product computation to find cosine similarity.
* Fully contained in standard library (uses `math`, `collections`, `re`).

## Usage

```python
from text_similarity import TextSimilarity

text1 = "The quick brown fox jumps over the lazy dog"
text2 = "A fast brown fox jumps over a lazy dog"

similarity_score = TextSimilarity.compute_cosine_similarity(text1, text2)

print(f"Similarity Score: {similarity_score:.4f}")
# Similarity Score: 0.5455
```

## Running Tests

To run the unit tests, use the following command from the project directory:

```bash
python3 -m unittest test_text_similarity.py
```
