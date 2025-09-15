from board import print_board, update_board
from player import get_player_input
from game import check_winner, is_draw
from utils import is_valid_move

def main():
    game_board = [[" " for _ in range(3)] for _ in range(3)]
    current_symbol = "X"

    while True:
        print_board(game_board)
        row, col = get_player_input(current_symbol)

        if not is_valid_move(board, row, col):
            print("Invalid move. Try again.")
            continue

        update_board(game_board, row, col, current_symbol)

        if check_winner(game_board):
            print_board(game_board)
            print(f"Player {current_symbol} wins!")
            break
        elif is_draw(game_board):
            print_board(game_board)
            print("It's a draw!")
            break

        current_symbol = "O" if current_symbol == "X" else "X"

if __name__ == "__main__":
    main()