from board import Board, COLS, ROWS
from ai import AI

HUMAN, COMPUTER = "X", "O"


def parse_column(raw):
    """Turn raw text into (0-based column, None), or (None, error message)."""
    raw = raw.strip()
    if not raw:
        return None, f"Please enter a column number (1-{COLS}), or q to quit."
    try:
        number = int(raw)
    except ValueError:
        return None, f"'{raw}' is not a number. Enter 1-{COLS}, or q to quit."
    if not 1 <= number <= COLS:
        return None, f"Column must be between 1 and {COLS}."
    return number - 1, None


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.turn = HUMAN

    def get_human_move(self):
        """Prompt until a playable column is entered. Returns None if the player quits."""
        while True:
            try:
                raw = input(f"Column (1-{COLS}), or q: ")
            except (EOFError, KeyboardInterrupt):
                print()
                return None
            if raw.strip().lower() in ("q", "quit"):
                return None
            col, error = parse_column(raw)
            if error:
                print(error)
            elif not self.board.can_drop(col):
                print(f"Column {col + 1} is full. Pick another.")
            else:
                return col

    def get_ai_move(self):
        """Ask the AI for a column. Returns None if it gives an unplayable one."""
        col = self.ai.choose_column(self.board)
        if col is None or not self.board.can_drop(col):
            print("The computer could not make a valid move.")
            return None
        return col

    def announce_move(self, col, row):
        """Report a placed disc. Columns count from the left, rows from the bottom, both from 1."""
        print(f"Player {self.turn} dropped in column {col + 1} (row {ROWS - row})")

    def game_over(self):
        """Check the player who just moved for a win, then for a draw."""
        if self.board.winner(self.turn):
            self.board.print()
            print(self.turn, "wins!")
            return True
        if self.board.full():
            self.board.print()
            print("Draw.")
            return True
        return False

    def run(self):
        print(f"Connect Four — you are {HUMAN}.")
        while True:
            self.board.print()
            col = self.get_human_move() if self.turn == HUMAN else self.get_ai_move()
            if col is None:
                print("Game ended.")
                return

            row = self.board.drop(col, self.turn)
            self.announce_move(col, row)
            if self.game_over():
                return
            self.turn = COMPUTER if self.turn == HUMAN else HUMAN