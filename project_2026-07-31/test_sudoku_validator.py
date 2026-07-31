import unittest
from sudoku_validator import is_valid_sudoku

class TestSudokuValidator(unittest.TestCase):

    def setUp(self):
        self.valid_board = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]

    def test_valid_board(self):
        self.assertTrue(is_valid_sudoku(self.valid_board))

    def test_invalid_row(self):
        board = [row[:] for row in self.valid_board]
        board[0][8] = "5" # Duplicate 5 in row 0
        self.assertFalse(is_valid_sudoku(board))

    def test_invalid_column(self):
        board = [row[:] for row in self.valid_board]
        board[8][0] = "5" # Duplicate 5 in column 0
        self.assertFalse(is_valid_sudoku(board))

    def test_invalid_subgrid(self):
        board = [row[:] for row in self.valid_board]
        board[2][2] = "5" # Duplicate 5 in the top-left 3x3 subgrid
        self.assertFalse(is_valid_sudoku(board))

if __name__ == '__main__':
    unittest.main()
