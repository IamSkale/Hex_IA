from board import HexBoard


class Player:
    def __init__(self, player_id: int):
        self.player_id = player_id

    def play(self, board: HexBoard) -> tuple:
        """
        Solicita entrada del usuario para colocar una ficha.
        Intenta de nuevo si el movimiento no es válido.

        Returns:
            tuple: Tupla (row, col) con la posición válida
        """
        while True:
            try:
                # Solicitar entrada al usuario
                print(f"\nJugador {self.player_id}: Ingresa tu movimiento (fila,columna): ", end="")
                user_input = input().strip()

                # Parsear la entrada
                parts = user_input.split(",")
                if len(parts) != 2:
                    print("❌ Formato inválido. Usa: fila,columna (ej: 2,3)")
                    continue

                row = int(parts[0].strip())
                col = int(parts[1].strip())

                # Validar que están dentro del rango
                if not (0 <= row < board.size and 0 <= col < board.size):
                    print(f"❌ Posición fuera del tablero. Usa coordenadas entre 0 y {board.size - 1}")
                    continue

                # Validar que la casilla esté vacía
                if board.board[row][col] != 0:
                    print("❌ Esa casilla ya está ocupada. Intenta de nuevo.")
                    continue

                # Colocar la ficha
                board.place_piece(row, col, self.player_id)
                return (row, col)

            except ValueError:
                print("❌ Error: Ingresa números válidos separados por coma (ej: 2,3)")
            except Exception as e:
                print(f"❌ Error inesperado: {e}. Intenta de nuevo.")