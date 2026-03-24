from board import HexBoard
from solution import SmartPlayer
from player import Player
import aux

def print_board(board: HexBoard):
    """
    Imprime el tablero en consola como un tablero hexagonal even-r.
    """
    print(f"\n{'='*70}")
    print(f"Estado del tablero HEX (Even-R Layout)")
    print(f"{'='*70}")
    
    # Leyenda de colores
    print("Jugador 1 (Izquierda ↔ Derecha): 🔴")
    print("Jugador 2 (Arriba ↕ Abajo): 🔵")
    print("Vacío: ⚪\n")
    
    # Imprimir encabezado de columnas
    print("     ", end="")
    for col in range(board.size):
        print(f"{col:3}", end="")
    print()
    
    # Imprimir filas con indentación para layout hexagonal even-r
    for row in range(board.size):
        # En even-r invertido: filas pares tienen indentación, impares pegadas al borde
        if row % 2 == 0:
            indent = "  "  # 2 espacios para filas pares
        else:
            indent = ""
        
        print(f"{row:2} {indent}", end="")
        
        for col in range(board.size):
            cell = board.board[row][col]
            if cell == 0:
                print(" ⚪ ", end="")
            elif cell == 1:
                print(" 🔴 ", end="")
            else:  # cell == 2
                print(" 🔵 ", end="")
        print()
    
    print(f"{'='*70}\n")


def get_player_type(player_num: int) -> str:
    """
    Solicita al usuario el tipo de jugador (IA o Usuario).
    
    Args:
        player_num: Número del jugador (1 o 2)
    
    Returns:
        str: 'ia' o 'usuario'
    """
    while True:
        print(f"\n¿Qué tipo de jugador es Jugador {player_num}?")
        print("1. IA (SmartPlayer)")
        print("2. Usuario (Humano)")
        choice = input("Selecciona (1 o 2): ").strip()
        
        if choice == "1":
            return "ia"
        elif choice == "2":
            return "usuario"
        else:
            print("❌ Opción inválida. Intenta de nuevo.")


def play_game(board_size: int = 4):
    """
    Inicializa un tablero de HEX y empieza un juego.
    El usuario puede elegir si cada jugador es una IA o un usuario.
    
    Args:
        board_size: Tamaño del tablero (NxN). Por defecto 4.
    """
    # Solicitar tipos de jugadores
    print("\n" + "="*60)
    print("⚙️  CONFIGURACIÓN DE JUGADORES")
    print("="*60)
    
    player1_type = get_player_type(1)
    player2_type = get_player_type(2)
    
    # Crear jugadores según selección
    if player1_type == "ia":
        player1 = SmartPlayer(1)
        print("\n✅ Jugador 1: IA (SmartPlayer)")
    else:
        player1 = Player(1)
        print("\n✅ Jugador 1: Usuario (Humano)")
    
    if player2_type == "ia":
        player2 = SmartPlayer(2)
        print("✅ Jugador 2: IA (SmartPlayer)")
    else:
        player2 = Player(2)
        print("✅ Jugador 2: Usuario (Humano)")
    
    # Inicializar tablero
    board = HexBoard(board_size)
    
    print("\n" + "="*60)
    print(f"🎮 INICIANDO JUEGO HEX {board_size}x{board_size}")
    print("="*60)
    print("Jugador 1 (🔴): Conecta izquierda ↔ derecha")
    print("Jugador 2 (🔵): Conecta arriba ↕ abajo")
    print("="*60 + "\n")
    
    turn = 0
    game_over = False
    
    while not game_over:
        # Verificar si el tablero está lleno
        if aux.is_full(board):
            print("\n🤝 ¡El tablero está lleno! Empate.")
            game_over = True
            break
        
        # Turno del Jugador 1
        print(f"\n📍 Turno {turn + 1}: Jugador 1 (🔴)")
        print_board(board)
        
        try:
            player1.play(board)
            if board.check_connection(1):
                print("\n🎉 ¡Jugador 1 (🔴) HA GANADO! Conectó izquierda ↔ derecha")
                print_board(board)
                game_over = True
                break
        except ValueError as e:
            print(f"Error: {e}")
            game_over = True
            break
        
        # Verificar si el tablero está lleno después de Jugador 1
        if aux.is_full(board):
            print("\n🤝 ¡El tablero está lleno! Empate.")
            game_over = True
            break
        
        # Turno del Jugador 2
        print(f"\n📍 Turno {turn + 1}: Jugador 2 (🔵)")
        print_board(board)
        
        try:
            player2.play(board)
            if board.check_connection(2):
                print("\n🎉 ¡Jugador 2 (🔵) HA GANADO! Conectó arriba ↕ abajo")
                print_board(board)
                game_over = True
                break
        except ValueError as e:
            print(f"Error: {e}")
            game_over = True
            break
        
        turn += 1


# Bloque principal: Inicializar y jugar
if __name__ == "__main__":
    play_game(board_size=10)