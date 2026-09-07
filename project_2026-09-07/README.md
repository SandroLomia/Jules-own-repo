# Daily Project - 2026-09-07: Basic Blockchain Simulator

## Overview
This project is a simple simulation of a blockchain implemented in Python. It includes the foundational concepts of blocks, cryptographic hashing, proof-of-work (mining), and chain validation.

## Why it was built
To explore cryptographic hashing and foundational blockchain concepts like proof-of-work and chain validation as a fun daily algorithmic exercise.

## Features
- **Block Representation:** A `Block` class that encapsulates data (transactions), a timestamp, its own hash, and the hash of the previous block.
- **Blockchain Management:** A `Blockchain` class that handles the creation of the genesis block, adding new blocks, and validating the integrity of the chain.
- **Proof of Work:** A basic mining algorithm requiring a specific number of leading zeros in the hash (difficulty) to validly add a block.
- **Chain Validation:** Verification logic to ensure that no block's data has been tampered with and that the chain correctly links back to the genesis block.

## How to use
You can import the classes and simulate a blockchain network:
```python
from blockchain import Block, Blockchain

# Initialize a blockchain with difficulty level 2
my_coin = Blockchain(difficulty=2)

# Create and add a new block
print("Mining block 1...")
my_coin.add_block(Block(1, [{"amount": 10}]))

# Create and add another block
print("Mining block 2...")
my_coin.add_block(Block(2, [{"amount": 20}]))

# Check if the chain is valid
print(f"Is chain valid? {my_coin.is_chain_valid()}")
```

## Running Unit Tests
To run the included unit tests, execute the following command from the root of the repository:
```bash
PYTHONPATH=project_2026-09-07 python3 -m unittest project_2026-09-07/test_blockchain.py
```
