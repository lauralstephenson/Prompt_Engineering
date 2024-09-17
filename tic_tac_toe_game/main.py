import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to convert a move to row and column
def convert_move(move):
    move -= 1
    return move // 3, move % 3

# Function to check if someone has won
def check_win(board, mark):
    # Check rows, columns, and diagonals
    return ((board[0][0] == board[0][1] == board[0][2] == mark) or
            (board[1][0] == board[1][1] == board[1][2] == mark) or
            (board[2][0] == board[2][1] == board[2][2] == mark) or
            (board[0][0] == board[1][0] == board[2][0] == mark) or
            (board[0][1] == board[1][1] == board[2][1] == mark) or
            (board[0][2] == board[1][2] == board[2][2] == mark) or
            (board[0][0] == board[1][1] == board[2][2] == mark) or
            (board[0][2] == board[1][1] == board[2][0] == mark))

# Function to check for a draw
def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function to get available moves
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                moves.append((i, j))
    return moves

# Function to get the player's move
def get_player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Enter a number between 1 and 9.")
                continue
            row, col = convert_move(move)
            if board[row][col] != " ":
                print("Invalid move. The cell is already occupied.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

# Function for the AI to make a move
def get_ai_move(board):
    available_moves = get_available_moves(board)
    return random.choice(available_moves)

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_mark = "X"
    ai_mark = "O"

    print("Welcome to Tic-Tac-Toe!")
    print("Enter numbers 1-9 to make your move:\n1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\n")
    
    print_board(board)

    while True:
        # Player's move
        row, col = get_player_move(board)
        board[row][col] = player_mark
        print_board(board)

        if check_win(board, player_mark):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        # AI's move
        print("AI is making a move...")
        row, col = get_ai_move(board)
        board[row][col] = ai_mark
        print_board(board)

        if check_win(board, ai_mark):
            print("AI wins! Better luck next time.")
            break
        if check_draw(board):
            print("It's a draw!")
            break

    if input("Play again? (y/n): ").lower() == 'y':
        play_game()

# Start the game
if __name__ == "__main__":
    play_game()

