import unittest
from maze import Maze

class TestMaze(unittest.TestCase):
    def test_dimensions(self):
        """Test if the maze dimensions are always odd."""
        maze1 = Maze(10, 10)
        self.assertEqual(maze1.width, 11)
        self.assertEqual(maze1.height, 11)

        maze2 = Maze(11, 11)
        self.assertEqual(maze2.width, 11)
        self.assertEqual(maze2.height, 11)

    def test_initial_grid(self):
        """Test if the initial grid is completely filled with walls (1)."""
        maze = Maze(5, 5)
        for row in maze.grid:
            for cell in row:
                self.assertEqual(cell, 1)

    def test_generation_paths(self):
        """Test if generation creates paths (0s) and keeps boundaries mostly as walls."""
        maze = Maze(11, 11)
        maze.generate()

        # Check that starting point is a path
        self.assertEqual(maze.grid[1][1], 0)

        # Check that there are multiple paths (0s)
        path_count = sum(row.count(0) for row in maze.grid)
        self.assertGreater(path_count, 10) # Should have many path cells

    def test_solvable(self):
        """Test if a generated maze is solvable from start to another point."""
        maze = Maze(11, 11)
        maze.generate(start_x=1, start_y=1)

        # Find a valid end point (must be a path cell, i.e., 0)
        end_x, end_y = -1, -1
        for y in range(maze.height - 2, 0, -1):
            for x in range(maze.width - 2, 0, -1):
                if maze.grid[y][x] == 0:
                    end_x, end_y = x, y
                    break
            if end_x != -1:
                break

        self.assertNotEqual((end_x, end_y), (-1, -1))

        path = maze.solve((1, 1), (end_x, end_y))

        # There should be a path
        self.assertIsNotNone(path)
        self.assertIsInstance(path, list)
        self.assertEqual(path[0], (1, 1))
        self.assertEqual(path[-1], (end_x, end_y))

        # Verify the path is valid (only moves through 0s, and adjacent steps)
        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i+1]
            self.assertEqual(maze.grid[y1][x1], 0)
            self.assertEqual(maze.grid[y2][x2], 0)

            # Check adjacency (Manhattan distance == 1)
            dist = abs(x1 - x2) + abs(y1 - y2)
            self.assertEqual(dist, 1)

    def test_unsolvable(self):
        """Test if solver correctly returns None for unsolvable paths (e.g. into a wall)."""
        maze = Maze(5, 5)
        # Manually create a simple maze
        # 1 1 1 1 1
        # 1 0 1 0 1
        # 1 1 1 1 1
        # 1 0 1 0 1
        # 1 1 1 1 1
        maze.grid[1][1] = 0
        maze.grid[1][3] = 0
        maze.grid[3][1] = 0
        maze.grid[3][3] = 0

        # Try to solve from path to wall
        path1 = maze.solve((1, 1), (0, 0))
        self.assertIsNone(path1)

        # Try to solve from disconnected paths
        path2 = maze.solve((1, 1), (3, 3))
        self.assertIsNone(path2)

if __name__ == '__main__':
    unittest.main()
