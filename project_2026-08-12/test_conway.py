import unittest
from conway import Grid

class TestConwayGameOfLife(unittest.TestCase):
    def test_block_still_life(self):
        # The block is a 2x2 square that should not change
        cells = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        grid = Grid(4, 4, cells)
        grid.next_generation()

        expected = [
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(grid.cells, expected)

    def test_blinker_oscillator(self):
        # The blinker is a line of 3 cells that oscillates horizontally and vertically
        cells = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        grid = Grid(5, 5, cells)

        # Generation 1
        grid.next_generation()
        expected_gen1 = [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(grid.cells, expected_gen1)

        # Generation 2 (should return to original state)
        grid.next_generation()
        expected_gen2 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(grid.cells, expected_gen2)

if __name__ == '__main__':
    unittest.main()
