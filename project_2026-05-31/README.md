# Daily Project - 2026-05-31

## Overview

Today's project is a command-line based **Unbeatable Tic-Tac-Toe Game** implemented in Python.

It features a robust game engine and a highly intelligent AI opponent powered by the **Minimax algorithm with Alpha-Beta Pruning**.

### Features

- Play Tic-Tac-Toe in your terminal.
- Choose to play as 'X' or 'O' against the AI.
- Let the AI play against itself to watch a perfect game.
- The AI uses the Minimax algorithm ensuring it will never lose (at worst, it forces a tie).

### How to Run

Navigate to the project directory or run from the root:

```bash
# Play as X (default, you go first)
python3 project_2026-05-31/tic_tac_toe.py

# Play as O (AI goes first)
python3 project_2026-05-31/tic_tac_toe.py --human O

# Watch AI vs AI
python3 project_2026-05-31/tic_tac_toe.py --human none
```

### Running Tests

To verify the game logic and AI correctness, run the unit tests:

```bash
PYTHONPATH=project_2026-05-31 python3 -m unittest project_2026-05-31/test_tic_tac_toe.py
```
