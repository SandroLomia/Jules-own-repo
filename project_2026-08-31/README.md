# Daily Project - 2026-08-31

## Overview

Today's project is an implementation of the **Levenshtein Distance** algorithm in Python.

The Levenshtein distance is a string metric for measuring the difference between two sequences. Informally, the Levenshtein distance between two words is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other.

This implementation uses dynamic programming to efficiently calculate the distance.

## Usage

You can use the `calculate_levenshtein_distance` function from `levenshtein.py`:

```python
from levenshtein import calculate_levenshtein_distance

distance = calculate_levenshtein_distance("kitten", "sitting")
print(f"The Levenshtein distance is: {distance}")  # Output: 3
```

## Running Tests

To run the unit tests, use the following command from the repository root:

```bash
PYTHONPATH=project_2026-08-31 python3 -m unittest project_2026-08-31/test_levenshtein.py
```
