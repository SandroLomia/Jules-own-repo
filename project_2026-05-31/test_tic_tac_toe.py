import unittest
from tic_tac_toe import TicTacToe, get_best_move

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_initial_board(self):
        self.assertEqual(self.game.num_empty_squares(), 9)
        self.assertTrue(self.game.empty_squares())
        self.assertIsNone(self.game.current_winner)

    def test_make_move(self):
        self.assertTrue(self.game.make_move((0, 0), 'X'))
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertEqual(self.game.num_empty_squares(), 8)
        self.assertFalse(self.game.make_move((0, 0), 'O')) # Cannot move to an occupied square

    def test_winner_row(self):
        self.game.make_move((0, 0), 'X')
        self.game.make_move((0, 1), 'X')
        self.game.make_move((0, 2), 'X')
        self.assertEqual(self.game.current_winner, 'X')

    def test_winner_col(self):
        self.game.make_move((0, 1), 'O')
        self.game.make_move((1, 1), 'O')
        self.game.make_move((2, 1), 'O')
        self.assertEqual(self.game.current_winner, 'O')

    def test_winner_diag(self):
        self.game.make_move((0, 0), 'X')
        self.game.make_move((1, 1), 'X')
        self.game.make_move((2, 2), 'X')
        self.assertEqual(self.game.current_winner, 'X')

        self.game = TicTacToe()
        self.game.make_move((0, 2), 'O')
        self.game.make_move((1, 1), 'O')
        self.game.make_move((2, 0), 'O')
        self.assertEqual(self.game.current_winner, 'O')

    def test_ai_blocks_win(self):
        # Setup board where X is about to win
        self.game.make_move((0, 0), 'X')
        self.game.make_move((0, 1), 'X')
        # O should block at (0, 2)
        move = get_best_move(self.game, 'O')
        self.assertEqual(move, (0, 2))

    def test_ai_takes_win(self):
        # Setup board where O is about to win
        self.game.make_move((1, 0), 'O')
        self.game.make_move((1, 1), 'O')
        # O should take the win at (1, 2)
        move = get_best_move(self.game, 'O')
        self.assertEqual(move, (1, 2))

    def test_ai_first_move(self):
        # First move should be center for performance/best strategy
        move = get_best_move(self.game, 'X')
        self.assertEqual(move, (1, 1))

if __name__ == '__main__':
    unittest.main()
