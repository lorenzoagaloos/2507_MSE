"""Tic Tac Toe game with two human players."""
import sys
import threading
import time


class Board:
    """Represents the Tic Tac Toe board."""

    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        """Display the board."""
        print("\n")
        for i, row in enumerate(self.grid):
            print(" | ".join(row))
            if i < 2:
                print("-" * 5)

    def empty_squares(self):
        """Return list of empty squares."""
        return [(r, c) for r in range(3) for c in range(3) if self.grid[r][c] == " "]

    def make_move(self, row, col, symbol):
        """Place a symbol if valid."""
        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True
        return False

    def won_game(self, symbol):
        """Check if symbol has won."""
        lines = self.grid + [list(col) for col in zip(*self.grid)]
        lines.append([self.grid[i][i] for i in range(3)])
        lines.append([self.grid[i][2 - i] for i in range(3)])
        return any(all(cell == symbol for cell in line) for line in lines)

    def game_over(self):
        """Return True if someone wins or draw."""
        return self.won_game("X") or self.won_game("O") or len(self.empty_squares()) == 0


class Player:
    """Represents a player."""

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0

    def record_win(self):
        """Record a win for this player."""
        self.wins += 1

    def get_stats(self):
        """Get player statistics."""
        return f"{self.name} has won {self.wins} game(s)"


class Game:
    """Main Tic Tac Toe game."""

    def __init__(self):
        self.board = Board()
        self.player1 = None
        self.player2 = None
        self.current_player = None
        self.setup_players()

    def setup_players(self):
        """Setup players with symbol selection."""
        sys.stdout.write("Player 1, choose your symbol (X or O): ")
        sys.stdout.flush()
        choice = sys.stdin.readline().strip().upper()

        while choice not in ['X', 'O']:
            sys.stdout.write("Invalid choice. Please enter X or O: ")
            sys.stdout.flush()
            choice = sys.stdin.readline().strip().upper()

        symbol1 = choice
        symbol2 = 'O' if symbol1 == 'X' else 'X'

        self.player1 = Player("Player 1", symbol1)
        self.player2 = Player("Player 2", symbol2)
        self.current_player = self.player1

        print(f"Player 1 is {symbol1}, Player 2 is {symbol2}")

    def other_player(self):
        """Switch turns."""
        self.current_player = (
            self.player2 if self.current_player == self.player1 else self.player1
        )

    def make_human_move(self, timeout=10):
        """Handle a player's move with timer."""
        result = {'row': None, 'col': None, 'timed_out': False}

        def timer_thread():
            start_time = time.time()
            while time.time() - start_time < timeout:
                remaining = int(timeout - (time.time() - start_time))
                if remaining <= 5 and remaining > 0:
                    sys.stdout.write(f"\r{remaining} seconds left...   ")
                    sys.stdout.flush()
                time.sleep(0.5)
                if result['row'] is not None:
                    return
            result['timed_out'] = True
            sys.stdout.write("\r\nTime's up!                    \n")
            sys.stdout.flush()

        timer = threading.Thread(target=timer_thread, daemon=True)
        timer.start()

        while True:
            try:
                sys.stdout.write(f"{self.current_player.name}, enter row (0–2): ")
                sys.stdout.flush()
                row_input = sys.stdin.readline().strip()
                if result['timed_out']:
                    return False
                row = int(row_input)

                sys.stdout.write(f"{self.current_player.name}, enter col (0–2): ")
                sys.stdout.flush()
                col_input = sys.stdin.readline().strip()
                if result['timed_out']:
                    return False
                col = int(col_input)

                if (row, col) in self.board.empty_squares():
                    self.board.make_move(row, col, self.current_player.symbol)
                    result['row'] = row
                    result['col'] = col
                    sys.stdout.write("\r" + " " * 60 + "\r")
                    sys.stdout.flush()
                    return True
                print(" Invalid move — square already taken or out of range.")
            except ValueError:
                if not result['timed_out']:
                    print(" Please enter valid numbers between 0 and 2.")
            except EOFError:
                print("\nGame interrupted.")
                sys.exit(0)

    def play_one_turn(self):
        """Play a single turn."""
        success = self.make_human_move(timeout=10)
        if not success:
            print(f"{self.current_player.name}'s turn skipped due to timeout.")

    def play_game(self):
        """Main game loop."""
        print("=== Tic Tac Toe (Human1 vs Human2) ===")
        self.board.display()
        while not self.board.game_over():
            print(f"\n{self.current_player.name}'s turn ({self.current_player.symbol})")
            self.play_one_turn()
            self.board.display()
            if self.board.won_game(self.current_player.symbol):
                print(f" {self.current_player.name} wins!")
                self.current_player.record_win()
                return
            self.other_player()
        print(" It's a draw!")

    def print_result(self):
        """Print final result."""
        print("Game finished. Thanks for playing!")


if __name__ == "__main__":
    game = Game()
    game.play_game()
    game.print_result()
