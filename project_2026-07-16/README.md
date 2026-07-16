# Daily Project - 2026-07-16

## Overview

Today's project is a robust implementation of a **Token Bucket Rate Limiter** in Python. Rate limiters are critical for controlling the rate of traffic sent to or received by a network interface or API, preventing overload and ensuring fair usage.

The Token Bucket algorithm works by adding "tokens" to a "bucket" at a constant rate. Each request or action consumes a token. If the bucket is empty, the action is denied (or rate-limited). This allows for sudden bursts of traffic up to the bucket's capacity, while maintaining an average rate equal to the fill rate.

## Features

- **`TokenBucket` Class:** Thread-safe implementation of the token bucket algorithm.
- **Parameters:**
  - `capacity`: The maximum number of tokens the bucket can hold (maximum burst size).
  - `fill_rate`: The number of tokens added to the bucket per second.
- **Methods:**
  - `consume(tokens=1)`: Attempts to consume the specified number of tokens. Returns `True` if successful, `False` if there are not enough tokens.

## Running Tests

The project includes a comprehensive test suite covering scenarios like initial capacity, consuming too many tokens, token refilling over time, and maximum capacity limits.

To run the tests from the repository root:

```bash
PYTHONPATH=project_2026-07-16 python3 -m unittest project_2026-07-16/test_rate_limiter.py
```
