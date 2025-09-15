def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_symbol = "X"

while True:
        print_board(board)
        row, col = get_player_input(current_symbol)

        if not is_valid_move(board, row, col):
            print("Invalid move. Try again.")
            continue

        update_board(board, row, col, current_symbol)

        if check_winner(board):
            print_board(board)
            print(f"Player {current_symbol} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_symbol = "O" if current_symbol == "X" else "X"

if __name__ == "__main__":
    main()