import math
import argparse

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_winner = None

    def print_board(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        moves = []
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == ' ':
                    moves.append((r, c))
        return moves

    def empty_squares(self):
        return any(' ' in row for row in self.board)

    def num_empty_squares(self):
        return sum(row.count(' ') for row in self.board)

    def make_move(self, square, letter):
        # square is a tuple (row, col)
        r, c = square
        if self.board[r][c] == ' ':
            self.board[r][c] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # check row
        row_ind = square[0]
        if all(s == letter for s in self.board[row_ind]):
            return True

        # check col
        col_ind = square[1]
        if all(self.board[r][col_ind] == letter for r in range(3)):
            return True

        # check diagonals
        if square[0] == square[1]:
            if all(self.board[i][i] == letter for i in range(3)):
                return True

        if square[0] + square[1] == 2:
            if all(self.board[i][2-i] == letter for i in range(3)):
                return True

        return False

def get_best_move(state, player):
    def minimax(state, current_player, maximizing_player, alpha=-math.inf, beta=math.inf):
        other_player = 'O' if current_player == 'X' else 'X'

        # Base cases
        if state.current_winner == other_player:
            score = (state.num_empty_squares() + 1)
            return {'position': None, 'score': score if other_player == maximizing_player else -score}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if current_player == maximizing_player:
            best = {'position': None, 'score': -math.inf}
        else:
            best = {'position': None, 'score': math.inf}

        for possible_move in state.available_moves():
            state.make_move(possible_move, current_player)
            sim_score = minimax(state, other_player, maximizing_player, alpha, beta)

            # Undo move
            state.board[possible_move[0]][possible_move[1]] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move

            if current_player == maximizing_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
                alpha = max(alpha, sim_score['score'])
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
                beta = min(beta, sim_score['score'])

            if beta <= alpha:
                break

        return best

    if state.num_empty_squares() == 9:
        return (1, 1) # Center is always best first move for performance

    result = minimax(state, player, player)
    return result['position']

def human_player(game, letter):
    valid_square = False
    val = None
    while not valid_square:
        square_str = input(f'{letter}\'s turn. Input move (0-8): ')
        try:
            val = int(square_str)
            if val < 0 or val > 8:
                raise ValueError

            row = val // 3
            col = val % 3
            if (row, col) not in game.available_moves():
                raise ValueError

            valid_square = True
            val = (row, col)
        except ValueError:
            print('Invalid square. Try again.')
    return val

def ai_player(game, letter):
    print(f'AI is thinking ({letter})...')
    return get_best_move(game, letter)

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player(game, letter)
        else:
            square = x_player(game, letter)

        if game.make_move(square, letter):
            if print_game:
                print(f'{letter} makes a move to square {square[0]*3 + square[1]}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print('It\'s a tie!')

def main():
    parser = argparse.ArgumentParser(description="Play Tic-Tac-Toe against an AI.")
    parser.add_argument("--human", choices=['X', 'O', 'none'], default='X', help="Choose which letter the human plays as (X, O, or none for AI vs AI). Default is X.")

    args = parser.parse_args()

    game = TicTacToe()

    if args.human == 'X':
        play(game, human_player, ai_player)
    elif args.human == 'O':
        play(game, ai_player, human_player)
    else:
        play(game, ai_player, ai_player)

if __name__ == '__main__':
    main()
