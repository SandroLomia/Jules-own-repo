# Daily Project - 2026-08-26: Topological Sort Algorithm

## Overview

This project implements a Topological Sort algorithm for a Directed Acyclic Graph (DAG) using Kahn's Algorithm.

Topological sorting for a DAG is a linear ordering of vertices such that for every directed edge `u -> v`, vertex `u` comes before `v` in the ordering. This is widely used for scheduling tasks, resolving dependencies, and more.

If the graph contains a cycle, a valid topological sort is not possible, and the implementation will raise a `ValueError`.

## Features
- Dynamic graph construction (`add_vertex`, `add_edge`).
- Automatic cycle detection.
- Fast `O(V + E)` time complexity, where `V` is the number of vertices and `E` is the number of edges.

## Usage

```python
from topological_sort import Graph

# Initialize a Graph
g = Graph()

# Add directed edges (u -> v)
g.add_edge(5, 2)
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

# Perform topological sort
try:
    result = g.topological_sort()
    print("Topological Sort:", result)
except ValueError as e:
    print(e)
```

## Running the Tests

To run the unit tests, use the following command from the repository root:

```bash
PYTHONPATH=project_2026-08-26 python3 -m unittest project_2026-08-26/test_topological_sort.py
```
