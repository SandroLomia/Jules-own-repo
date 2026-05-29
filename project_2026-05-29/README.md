# Daily Project - 2026-05-29

## Overview

Today's project is a robust Fuzzy Search utility implemented in Python.
It uses the Levenshtein distance algorithm to find approximate string matches from a list of items based on a user-defined threshold.

## Features
- **Levenshtein Distance Calculation**: A highly efficient implementation to calculate the minimum number of edits to convert one string to another.
- **Fuzzy Searching**: Allows querying a list of strings and returning matches that differ by at most a specified threshold distance.
- **Case-insensitive matching**: Standardizes cases before comparison to ensure more natural matches.
- **Sorted Results**: Results are returned ordered by the closest match first (lowest distance).

## How to use

```python
from fuzzy_search import fuzzy_search

items = ["apple", "banana", "orange", "grape", "pineapple"]
results = fuzzy_search("aple", items, threshold=1)
print(results)
# Output: ['apple']
```

## Running tests

To run the unit tests, use the following command from the root of the repository:
```bash
PYTHONPATH=project_2026-05-29 python3 -m unittest project_2026-05-29/test_fuzzy_search.py
```