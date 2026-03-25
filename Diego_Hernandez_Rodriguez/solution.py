import random
import heapq
from player import Player
from board import HexBoard


def get_legal_moves(board):
    return [(r, c) for r in range(board.size) for c in range(board.size) if board.board[r][c] == 0]


def neighbors(board, row: int, col: int):
    if row % 2 == 0:
        directions = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]
    else:
        directions = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < board.size and 0 <= nc < board.size:
            yield nr, nc


def is_full(board):
    return all(cell != 0 for row in board.board for cell in row)


def board_to_string(board):
    lines = []
    for r in range(board.size):
        indent = " " * r
        row_symbols = []
        for c in range(board.size):
            value = board.board[r][c]
            row_symbols.append("." if value == 0 else str(value))
        lines.append(indent + " ".join(row_symbols))
    return "\n".join(lines)


class SmartPlayer(Player):
    def play(self, board: HexBoard) -> tuple:
        legal_moves = get_legal_moves(board)

        # Si hay un solo movimiento, jugarlo.
        if len(legal_moves) == 1:
            row, col = legal_moves[0]
            board.place_piece(row, col, self.player_id)
            return (row, col)

        opponent_id = 1 if self.player_id == 2 else 2

        # Evaluar cada movimiento por distancia mínima después de colocarlo.
        move_distances = []
        for r, c in legal_moves:
            clone = board.clone()
            clone.place_piece(r, c, self.player_id)
            dist = self.dijkstra_distance(clone, opponent_id)
            move_distances.append((dist, (r, c)))

        # Seleccionar movimiento con menor distancia.
        min_dist = min(d for d, _ in move_distances)
        best_moves = [(r, c) for d, (r, c) in move_distances if d == min_dist]

        row, col = random.choice(best_moves)
        board.place_piece(row, col, self.player_id)
        return (row, col)

    def dijkstra_distance(self, board: HexBoard, opponent_id: int) -> float:
        if self.player_id == 1:
            start_positions = [(r, 0) for r in range(board.size) if board.board[r][0] == self.player_id]
            target_col = board.size - 1
        else:
            start_positions = [(0, c) for c in range(board.size) if board.board[0][c] == self.player_id]
            target_row = board.size - 1

        if not start_positions:
            return float('inf')

        distances = { (r, c): float('inf') for r in range(board.size) for c in range(board.size) }
        for pos in start_positions:
            distances[pos] = 0

        pq = [(0, pos) for pos in start_positions]
        visited = set()

        while pq:
            dist, (r, c) = heapq.heappop(pq)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            if (self.player_id == 1 and c == target_col) or (self.player_id == 2 and r == target_row):
                return dist

            for nr, nc in neighbors(board, r, c):
                if board.board[nr][nc] == opponent_id:
                    continue  # Enemigas: infinito, no transitar.
                cost = 0 if board.board[nr][nc] == self.player_id else 1  # Propias: 0, vacías: 1
                new_dist = dist + cost
                if new_dist < distances[(nr, nc)]:
                    distances[(nr, nc)] = new_dist
                    heapq.heappush(pq, (new_dist, (nr, nc)))

        return float('inf')
    
    


