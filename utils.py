# utils.py
def is_valid_move(board, row, col):
    return 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " "