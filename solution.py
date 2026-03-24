import random
from player import Player
from board import HexBoard


class SmartPlayer(Player):
    def play(self, board: HexBoard) -> tuple:
        """
        Selecciona un movimiento aleatorio del tablero.
        Retorna una tupla (row, col) con la posición de la ficha.
        """
        legal_moves = board.get_legal_moves()
        
        if not legal_moves:
            raise ValueError("No hay movimientos legales disponibles")
        
        # Selecciona un movimiento aleatorio
        move = random.choice(legal_moves)
        row, col = move
        
        # Coloca la ficha en el tablero
        board.place_piece(row, col, self.player_id)
        
        return move
    
    



