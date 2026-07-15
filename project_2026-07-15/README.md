# Bloom Filter

This project implements a **Bloom Filter**, a space-efficient probabilistic data structure used to test whether an element is a member of a set. False positive matches are possible, but false negatives are not (i.e., a query returns either "possibly in set" or "definitely not in set").

## Features

- Configurable bit array size.
- Configurable number of hash functions.
- Uses `hashlib` (SHA-256) with salting to generate distinct hashes.

## Usage

```python
from bloom_filter import BloomFilter

# Create a Bloom Filter with a bit array of size 1000 and 5 hash functions
bf = BloomFilter(size=1000, hash_count=5)

# Add elements
bf.add("apple")
bf.add("banana")

# Check for existence
print(bf.check("apple"))   # True
print(bf.check("cherry"))  # False (most likely)
```

## Running Tests

To run the unit tests, execute the following from the repository root:

```bash
PYTHONPATH=project_2026-07-15 python3 -m unittest project_2026-07-15/test_bloom_filter.py
```
