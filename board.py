#board.py
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def update_board(board, row, col, symbol):
    board[row][col] = symbol