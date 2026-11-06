import secrets
from collections import deque

class Maze:
    def __init__(self, width: int, height: int):
        # We need odd dimensions to ensure walls and paths map correctly
        self.width = width if width % 2 != 0 else width + 1
        self.height = height if height % 2 != 0 else height + 1

        # 1 represents wall, 0 represents path
        # Initialize maze with all walls
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]
        self.prng = secrets.SystemRandom()

    def generate(self, start_x: int = 1, start_y: int = 1):
        """Generates the maze using randomized depth-first search (recursive backtracking)."""
        # Starting point should be a path
        self.grid[start_y][start_x] = 0

        # Stack stores (x, y)
        stack = [(start_x, start_y)]

        while stack:
            current_x, current_y = stack[-1]

            # Find all unvisited neighbors
            neighbors = []
            # Directions: Right, Down, Left, Up (movement by 2 to jump over walls)
            directions = [(2, 0), (0, 2), (-2, 0), (0, -2)]

            for dx, dy in directions:
                nx, ny = current_x + dx, current_y + dy

                # Check if neighbor is within bounds and is a wall (unvisited)
                if 0 < nx < self.width - 1 and 0 < ny < self.height - 1 and self.grid[ny][nx] == 1:
                    neighbors.append((nx, ny, dx, dy))

            if neighbors:
                # Choose a random neighbor
                nx, ny, dx, dy = self.prng.choice(neighbors)

                # Knock down the wall between current and neighbor
                wall_x = current_x + dx // 2
                wall_y = current_y + dy // 2
                self.grid[wall_y][wall_x] = 0

                # Mark neighbor as path
                self.grid[ny][nx] = 0

                # Push neighbor to stack
                stack.append((nx, ny))
            else:
                # Backtrack if no unvisited neighbors
                stack.pop()

    def solve(self, start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]] | None:
        """Solves the maze using Breadth-First Search (BFS). Returns a list of coordinates for the path."""
        if self.grid[start[1]][start[0]] == 1 or self.grid[end[1]][end[0]] == 1:
            return None # Start or end is a wall

        queue = deque([(start, [start])])
        visited = {start}

        # Directions: Right, Down, Left, Up (movement by 1)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while queue:
            (curr_x, curr_y), path = queue.popleft()

            if (curr_x, curr_y) == end:
                return path

            for dx, dy in directions:
                nx, ny = curr_x + dx, curr_y + dy

                # Check bounds, if it's a path, and if it's unvisited
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.grid[ny][nx] == 0 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append(((nx, ny), path + [(nx, ny)]))

        return None # No path found

    def __str__(self):
        """Returns a string representation of the maze."""
        output = ""
        for row in self.grid:
            for cell in row:
                output += "█" if cell == 1 else " "
            output += "\n"
        return output
