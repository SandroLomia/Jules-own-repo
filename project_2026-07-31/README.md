# Daily Project - 2026-07-31

## Overview

This project implements a Sudoku Validator in Python. The goal of this tool is to efficiently determine if a given 9x9 Sudoku board configuration is valid according to classic Sudoku rules.

## Features

- Validates a 9x9 grid to ensure that each row contains the digits 1-9 without repetition.
- Validates that each column contains the digits 1-9 without repetition.
- Validates that each of the nine 3x3 subgrids contains the digits 1-9 without repetition.
- Handles empty cells (represented by `"."`).
- Implemented with optimal time complexity by iterating through the board in a single pass.

## Running Tests

To execute the unit tests and verify the logic:

```bash
PYTHONPATH=project_2026-07-31 python3 -m unittest project_2026-07-31/test_sudoku_validator.py
```
