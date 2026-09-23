# Daily Project - 2026-09-23

## Overview

Today's project is an implementation of a **Token Bucket Rate Limiter** in Python.

A rate limiter is used to control the rate of traffic sent or received by a network interface controller. It is essential for protecting APIs from overuse, preventing denial-of-service attacks, and ensuring fair usage among clients.

The token bucket algorithm works as follows:
- A "bucket" is assigned to each client, capable of holding a maximum number of tokens (`capacity`).
- Tokens are added to the bucket at a constant `refill_rate` (e.g., tokens per second), up to the maximum capacity.
- When a request comes in, the rate limiter checks if there's at least 1 token in the bucket.
- If a token is available, it is consumed, and the request is allowed.
- If the bucket is empty, the request is rejected (rate limited).

## Features

- **Efficient Refill:** Tokens are refilled lazily at the time of a request based on the time elapsed since the last refill, avoiding the need for a background process to constantly update token counts.
- **Client Isolation:** Each `client_id` (e.g., IP address, user ID) gets its own independent token bucket.
- **Configurable:** Both the bucket capacity and the refill rate are customizable when instantiating the limiter.

## How to Run Tests

The implementation comes with a comprehensive suite of unit tests. You can run them using the built-in `unittest` module.

From the root directory of the repository, run:

```bash
PYTHONPATH=project_2026-09-23 python3 -m unittest project_2026-09-23/test_rate_limiter.py
```
