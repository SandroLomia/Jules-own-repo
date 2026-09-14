# Daily Project - 2026-09-14

## Overview

Today I implemented a **Dependency Resolver** utility in Python.

In complex software systems, package managers, task schedulers, or build pipelines, ensuring that tasks are executed in the correct order based on their prerequisites is a common challenge.

This project solves that problem by implementing a graph-based approach using **Topological Sort (Kahn's algorithm)**. It evaluates a set of items and their dependencies, producing a valid sequence of execution. If there is a cycle (e.g., A depends on B, and B depends on A), the algorithm will detect the circular dependency and raise an error.

## Features

- Resolves complex dependency graphs.
- Safely detects and reports circular dependencies.
- Handles isolated independent nodes.

## Usage

```python
from dependency_resolver import DependencyResolver

resolver = DependencyResolver()

# Add dependencies: format is (item, depends_on_this_item)
resolver.add_dependency('Task B', 'Task A')  # Task B needs Task A to be done first
resolver.add_dependency('Task C', 'Task A')
resolver.add_dependency('Task D', 'Task B')
resolver.add_dependency('Task D', 'Task C')

# Resolve the order
order = resolver.resolve()
print(order)
# Output: ['Task A', 'Task B', 'Task C', 'Task D']
# (Note: B and C can be swapped since they have the same dependencies)
```

## Running Tests

To run the unit test suite, make sure your Python path is set correctly:

```bash
PYTHONPATH=project_2026-09-14 python3 -m unittest project_2026-09-14/test_dependency_resolver.py
```
