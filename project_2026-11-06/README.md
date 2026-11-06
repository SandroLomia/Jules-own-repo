# Maze Generator & Solver

This project implements a Python-based Maze Generator and Solver.

## Features

- **Generation:** Generates a perfect maze using randomized depth-first search (recursive backtracking). This algorithm creates long, winding paths.
- **Solving:** Solves a given maze from a start point to an end point using Breadth-First Search (BFS). This guarantees finding the shortest path.
- **Representation:** Includes a simple string representation for printing the maze to the console (`█` for walls, space for paths).

## Usage

You can use the `Maze` class to generate and solve mazes.

```python
from maze import Maze

# Create a maze with dimensions 21x21 (must be odd, will adjust automatically if even)
my_maze = Maze(21, 21)

# Generate the maze starting at (1, 1)
my_maze.generate(start_x=1, start_y=1)

# Print the generated maze
print(my_maze)

# Solve the maze from (1, 1) to (19, 19)
path = my_maze.solve((1, 1), (19, 19))

if path:
    print(f"Path found with {len(path)} steps!")
else:
    print("No path found.")
```

## Running Tests

Unit tests are provided in `test_maze.py`. You can run them using the `unittest` module:

```bash
PYTHONPATH=project_2026-11-06 python3 -m unittest project_2026-11-06/test_maze.py
```
