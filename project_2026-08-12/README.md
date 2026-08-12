# Daily Project - 2026-08-12

## Overview

Today's project is an implementation of **Conway's Game of Life** in Python. It's a classic cellular automaton devised by the British mathematician John Horton Conway in 1970.

### Why Conway's Game of Life?

I chose this project because it perfectly demonstrates how complex, emergent behaviors can arise from a very simple set of rules. It is a foundational concept in computer science, simulation, and the study of complex systems.

### How it Works

The game is a zero-player game, meaning its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

The universe of the Game of Life is a two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, *live* or *dead* (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

1.  **Underpopulation:** Any live cell with fewer than two live neighbours dies.
2.  **Survival:** Any live cell with two or three live neighbours lives on to the next generation.
3.  **Overpopulation:** Any live cell with more than three live neighbours dies.
4.  **Reproduction:** Any dead cell with exactly three live neighbours becomes a live cell.

The implementation contains a `Grid` class that encapsulates the state and the rules for generating the next state.

### How to Run Tests

You can run the unit tests to verify the core logic (like the Block still life and Blinker oscillator) with the following command:

```bash
PYTHONPATH=project_2026-08-12 python3 -m unittest project_2026-08-12/test_conway.py
```
