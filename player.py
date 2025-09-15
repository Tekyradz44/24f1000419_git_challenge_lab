#player.py
def get_player_input(symbol):
    while True:
        try:
            row = int(input(f"Player {symbol}, enter your row (1, 2, or 3): "))-1
            col = int(input(f"Player {symbol}, enter your column (1, 2, or 3): "))-1
            
            if row in [0, 1, 2] and col in [0, 1, 2]:
                return row, col
            else:
                print("Row and column must be 1, 2, or 3. Try again.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")