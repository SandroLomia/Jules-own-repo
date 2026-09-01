# Daily Project - 2026-09-01

## Overview

Today's project is an implementation of a **Bloom Filter** in Python.

A Bloom filter is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set. False positive matches are possible, but false negatives are not – in other words, a query returns either "possibly in set" or "definitely not in set". Elements can be added to the set, but not removed.

### Features
- Automatic calculation of optimal bit array size and number of hash functions based on target capacity and acceptable error rate.
- Cryptographic hash simulation to represent `k` independent hash functions using `hashlib.sha256`.

### How to Run Tests

From the repository root, you can run the unit tests with the following command:

```bash
PYTHONPATH=project_2026-09-01 python3 -m unittest project_2026-09-01/test_bloom_filter.py
```
