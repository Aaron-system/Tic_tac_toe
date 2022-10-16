# --------- Global Variables -----------

# Will hold our game board data
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet


# Tells us who the winner is


# Tells us who the current player is (X goes first)


player1 = "X"
player2 = "O"

current_player = player1

winner = 1


# ------------- Functions ---------------

# Play a game of tic tac toe


# Show the initial game board


# Loop until the game stops (winner or tie)
def play_game():
    while winner == 1:

        display_board()

        # Handle a turn
        handle_turn()
        # Check if the game is over
        check_for_winner()

        # Flip to the other player
        flip_player()

        if winner == 2:
            you_win()

        elif winner == 3:
            you_lose()

    # Since the game is over, print the winner or tie


# Display the game board to the screen
def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])


# Handle a turn for an arbitrary player
def handle_turn():

    placement = input("Please choose a number between 1-9: ")

    valid = False
    while not valid:
        while placement not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            placement = input("Sorry, that is not a valid position. Please try again: ")

        placement = int(placement) - 1

        if board[placement] == '-':
            valid = True
            board[placement] = current_player
        else:
            placement = input("Sorry, that spot has already been filled. Please try again: ")



# Check if the game is over
def check_if_game_over():
    return


# Check to see if somebody has won
def check_for_winner():
    check_rows()
    check_diagonals()
    check_columns()
    check_for_tie()

    # Set global variables

    # Check if there was a winner anywhere

    # Get the winner


# Check the rows for a win
def check_rows():
    global winner

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        winner = 2

    # Set global variables

    # Check if any of the rows have all the same value (and is not empty)

    # If any row does have a match, flag that there is a win

    # Return the winner

    # Or return None if there was no winner


# Check the columns for a win
def check_columns():
    global winner

    columns_1 = board[0] == board[3] == board[6] != "-"
    columns_2 = board[1] == board[4] == board[7] != "-"
    columns_3 = board[2] == board[5] == board[8] != "-"

    if columns_1 or columns_2 or columns_3:
        winner = 2

    # Set global variables

    # Check if any of the columns have all the same value (and is not empty)

    # If any row does have a match, flag that there is a win

    # Return the winner

    # Or return None if there was no winner


# Check the diagonals for a win
def check_diagonals():
    global winner

    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    if diagonals_1 or diagonals_2:
        winner = 2


# Check if there is a tie
def check_for_tie():
    global winner

    if "-" not in board:
        winner = 3

    # Set global variables

    # If board is full

    # Else there is no tie


# Flip the current player from X to O, or O to X
def flip_player():
    global current_player

    if current_player == player1:
        current_player = player2
    elif current_player == player2:
        current_player = player1
    else:
        return


def you_win():
    display_board()
    print("Congratulations you win!!!")


def you_lose():
    display_board()
    print("GAME OVER!!!")

    # Global variables we need

    # If the current player was X, make it O

    # Or if the current player was O, make it X


# ------------ Start Execution -------------
# Play a game of tic tac toe
play_game()
