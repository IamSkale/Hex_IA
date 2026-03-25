"""
Funciones auxiliares para el juego HEX
"""

from collections import deque


def get_legal_moves(board):
    """Retorna lista de movimientos legales (casillas vacías)."""
    return [(r, c) for r in range(board.size) for c in range(board.size) if board.board[r][c] == 0]


def neighbors(board, row: int, col: int):
    """Genera los vecinos de una celda en even-r layout."""
    if row % 2 == 0:
        directions = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
    else:
        directions = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < board.size and 0 <= nc < board.size:
            yield nr, nc


def is_full(board):
    """Verifica si el tablero está completo."""
    return all(cell != 0 for row in board.board for cell in row)


def board_to_string(board):
    """Retorna representación en string del tablero."""
    lines = []
    for r in range(board.size):
        indent = " " * r
        row_symbols = []
        for c in range(board.size):
            value = board.board[r][c]
            row_symbols.append("." if value == 0 else str(value))
        lines.append(indent + " ".join(row_symbols))
    return "\n".join(lines)

def _neighbors_internal(self, row: int, col: int):
        """Genera los vecinos internos para check_connection."""
        if row % 2 == 0:
            directions = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
        else:
            directions = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.size and 0 <= nc < self.size:
                yield nr, nc
