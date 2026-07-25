# Bloom Filter Implementation

This directory contains a Python implementation of a Bloom Filter, a space-efficient probabilistic data structure.

## What it is

A Bloom filter is used to test whether an element is a member of a set. False positive matches are possible, but false negatives are not – in other words, a query returns either "possibly in set" or "definitely not in set". Elements can be added to the set, but not removed. The more elements that are added to the set, the larger the probability of false positives.

## Why use it

Bloom filters are incredibly space-efficient compared to other data structures (like Hash Tables or Sets) when dealing with massive datasets. They are ideal for applications where you need to quickly check if something might exist, such as:
- Checking if a URL is malicious before loading it
- Preventing weak passwords from being used
- Database engines avoiding disk lookups for non-existent keys

## How to use

```python
from bloom_filter import BloomFilter

# Initialize a filter expecting 10,000 items with a 1% false positive rate
bf = BloomFilter(capacity=10000, error_rate=0.01)

# Add an item
bf.add("test_item")

# Check for existence
if "test_item" in bf:
    print("Item is probably present")
else:
    print("Item is definitely not present")
```

## Running tests

```bash
PYTHONPATH=. python3 -m unittest test_bloom_filter.py
```
