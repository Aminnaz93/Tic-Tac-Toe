def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


def check_winner(board, player):
    """Checks if the given player has won."""
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal
        [2, 4, 6]   # Diagonal
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def is_full(board):
    """Checks if the board is full."""
    return all(cell != " " for cell in board)


def tic_tac_toe():
    """Main function to play the game."""
    board = [" "] * 9  # Initial empty board
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")

   
   
    while True:
        print_board(board)

        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")
            continue
        
        board[move] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()