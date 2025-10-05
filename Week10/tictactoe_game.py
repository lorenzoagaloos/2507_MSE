""" Tic-Tac-Toe Game """
import sys


class Board:
    """ Tic Tac Toe Board """
    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]

    def display(self):
        """ Display the board """
        for row in self.grid:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col, mark):
        """ Make a move on the board """
        if 0 <= row < 3 and 0 <= col < 3 and self.grid[row][col] == ' ':
            self.grid[row][col] = mark
            return True
        return False

    def check_winner(self, mark):
        """ Check for a winner """

        for i in range(3):
            if all(self.grid[i][j] == mark for j in range(3)) or \
               all(self.grid[j][i] == mark for j in range(3)):
                return True
        # Check diagonals
        if all(self.grid[i][i] == mark for i in range(3)) or \
           all(self.grid[i][2-i] == mark for i in range(3)):
            return True
        return False

    def is_full(self):
        """ Check if the board is full """
        return all(cell != ' ' for row in self.grid for cell in row)


class Player:
    """ Player class """
    def __init__(self, name, mark):
        """ Initialize player """
        self.name = name
        self.mark = mark
        self.wins = 0

    def get_move(self):
        """ Get move from player """
        try:
            sys.stdout.write(f"{self.name} ({self.mark}), enter row,col: ")
            sys.stdout.flush()
            move = sys.stdin.readline().strip()
            if not move:
                raise EOFError
            row, col = map(int, move.split(','))
            return row, col
        except (ValueError, IndexError):
            print("Invalid input. Use format: row,col")
            return None, None
        except EOFError:
            print("\nGame interrupted.")
            sys.exit(0)

    def record_win(self):
        """ Record a win for this player """
        self.wins += 1

    def get_stats(self):
        """ Get player statistics """
        return f"{self.name} has won {self.wins} game(s)"

class TicTacToeGame:
    """ Main Tic Tac Toe Game """
    def __init__(self):
        """ Initialize game """
        self.board = Board()
        self.players = [Player("Player 1", 'X'), Player("Player 2", 'O')]
        self.current = 0

    def play(self):
        """ Play the game """
        self.board.display()
        while True:
            player = self.players[self.current]
            row, col = player.get_move()

            if row is not None and self.board.make_move(row, col, player.mark):
                self.board.display()
                if self.board.check_winner(player.mark):
                    print(f"{player.name} wins!")
                    break
                if self.board.is_full():
                    print("It's a draw!")
                    break
                self.current = 1 - self.current
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":

    TicTacToeGame().play()
