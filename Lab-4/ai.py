import copy

from board import COLS


class AI:
    def choose_column(self, board, me="O", opponent="X"):
        legal = self._legal_columns(board)
        if not legal:
            return None

        # 1. Take an immediate win.
        for col in legal:
            if self._wins_by_playing(board, col, me):
                return col

        # 2. Otherwise block the opponent's immediate win.
        for col in legal:
            if self._wins_by_playing(board, col, opponent):
                return col

        # 3. Otherwise play the legal column closest to the centre.
        centre = (COLS - 1) / 2
        return min(legal, key=lambda c: abs(c - centre))

    @staticmethod
    def _legal_columns(board):
        return [c for c in range(COLS) if board.grid[0][c] == "."]

    @staticmethod
    def _wins_by_playing(board, col, token):
        """Would dropping `token` in `col` win? Tries it on a copy, never the real board."""
        trial = copy.deepcopy(board)
        trial.drop(col, token)
        return trial.winner(token)