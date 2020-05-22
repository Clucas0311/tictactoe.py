# Tic Tac Toe Project

import random  # Used to import the random module - to call randint function


def draw_board(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def input_player_letter():
    # Lets the player enter which letter they want to be
    # Returns a list with the player's letter as the first item and  the
    # computer's letter as a second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input("Do you want to be X or O?: ")
        letter = letter.upper()

        # The first element in the list is the player's letter; the second is
        # the computer's letter.
    if letter == 'X':  # if user chooses X, CPU is O; vice versa
        return ['X', 'O']  # Index[0] = Player Index[1] = CPU
    else:  # The first element is the Players the second is the CPU
        return ['O', 'X']


def who_goes_first():
    # Randomly chooses which players goes first.
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def make_move(board, letter, move):
    # board represents the state of the board
    # letter represents (x/o)
    # move represents the place on the board where the players wants to go
    board[move] = letter  # Creates a list reference of board at move index


def is_winner(bo, le):
    # Given a board and a player's letter, this function returns True if
    # that player has won.
    # 'bo'  = 'board' instead of board and "le" = "letter" to make it easier

    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # Across the top
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # Across the middle
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # Across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # Down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # Down the middle
            # Down the right side
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or  # left diagonally
            (bo[7] == le and bo[5] == le and bo[3] == le))   # right diagonally


def get_board_copy(board):
    # Make a copy of the board list and return it
    board_copy = []
    for i in board:
        board_copy.append(i)
    return board_copy


def is_space_free(board, move):
    # Returns True if the passed move is free on the board.
    # free spaces in the board lists are marked as single space strings
    # if the item at the space's index is not equal ' ' then space is taken
    return board[move] == ' '


def get_player_move(board):
    # Let the player enter thier move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split(
    ) or not is_space_free(board, int(move)):
        move = input(("What is your move? (1-9): "))
    return int(move)  # return int move because expression is short circuted


def choose_random_move_from_list(board, move_list):
    # Returns a valid move from the passed list on the passed board
    # Returns None if there is no valid moves
    possible_moves = []  # Create an empty to list so you can create a new list
    for i in move_list:  # the for loop iterates over the move list
        if is_space_free(board, i):  # cause this function to return true
            # and adds the true function to the possible moves
            possible_moves.append(i)
            # At this point possible moves has all the possible free spaces
            # stored
    if len(
            possible_moves) != 0:  # Checks to see if list is empty if list is not empty
        # There is at least one possible move to be made choose this at
        # random
        return random.choice(possible_moves)
    else:
        return None  # if there are no more moves return "None"


def get_computer_move(board, computer_letter):
    # Given a board and the computer's letter, determine where to move
    # and return that move
    if computer_letter == 'X':  # if computer chooses "X"
        player_letter = 'O'  # player choose "O" and vice versa
    else:
        player_letter = 'X'
        # Here is the algorithim for our TicTacToe AI:
        # First, check if we can win in the next move.

    for i in range(
            1,
            10):  # iterates over every possible move on the board which is numbered 1 - 9
        board_copy = get_board_copy(board)  # makes a copy of the board lists
        if is_space_free(
                board_copy,
                i):  # checks if space is free, if free makes move
            # player chooses where to place character
            make_move(board_copy, computer_letter, i)
            if is_winner(
                    board_copy,
                    computer_letter):  # if move is winning move from the list of winning move_list
                # the cpu will attempt to block it by countering with the
                # winning move selection
                return i
    # Check if the player could win on his next move, and block them
    for i in range(
            1,
            10):  # iterates over every possible move on the board which is numbered 1 - 9
        board_copy = get_board_copy(board)  # makes a copy of the board lists
        if is_space_free(
                board_copy,
                i):  # checks if space is free, if free makes move
            # player chooses where to place character
            make_move(board_copy, player_letter, i)
            if is_winner(
                    board_copy,
                    player_letter):  # if move is winning move from the list of winning move_list
                # the cpu will attempt to block it by countering with the
                # winning move selection
                return i

        # Try to take one of the corners, if they are free.
        # if CPU can't block user CPU chooses corner
    # function ensures computer picks one of these corners spaces
    move = choose_random_move_from_list(board, [1, 3, 7, 9])
    if move != None:  # if the corner space is free
        return move  # it returns the move, it not free it will return None but will will attempt to attack the center

    # Try to take the center, if it is free
    if is_space_free(board, 5):
        return 5

    # if center and corners are taken CPU will choose the sides
    return choose_random_move_from_list(board, [2, 4, 6, 8])
    # wont return None because this is the last location of choices available


def is_board_full(board):
    # Returns True if every space on the board has been taken
    # checks all the spaces in the 10 string list and see if it has an x/o in each index except 0 (ignored)
    # returns False if every space has not been taken
    for i in range(1, 10):  # for loop allows us to check indexes 1 - 9
        if is_space_free(board, i):  # looks for free space if one is found
            return False
    return True  # if no free space is found it returns T}rue - board is is_board_full


# Game loop
print("Welcome to Tic-Tac-Toe!")  # First line displayed on the program

while True:  # enters while loop - it keeps looping until the program encounters a break statement
    # Reset the board.
    # board start empty with represent that with a list of 10 single space
    # strings
    the_board = [' '] * 10
    # function returns two strings either x/o or o/x
    player_letter, computer_letter = input_player_letter()
    turn = who_goes_first()  # function that decides who goes first
    print(f"The {turn} will go first.")
    # keeps track of wheter the game is still being played or if someone won
    # or tied
    game_is_playing = True

    while game_is_playing:
        if turn == 'player':
            # Player's Turn # if turn = CPU then it will skip next steps
            # prints the TicTacToe screen if it is the users go
            draw_board(the_board)
            # allows the player to enter their move
            move = get_player_move(the_board)
            make_move(the_board, player_letter, move)  # adds X and O on board

            if is_winner(
                    the_board,
                    player_letter):  # Now since the player has made thier move the program checks to see if player won
                draw_board(the_board)
                print("Horray! You have won the game!")
                # if is winner is true the if block displays the winning board
                # and prints message
                game_is_playing = False
                # game play is also set to false to game doesn't continue on
                # the computers Turn
            else:  # if the last move doesn't win maybe the move filled up the entire board and its a tie
                if is_board_full(
                        the_board):  # returns True is there are no more moves that can be made
                    draw_board(the_board)  # displays tie board
                    print("The game is a tie!")  # tells user game is a tie
                    break
                else:  # if player hasn't won or tied the program enters another else statement
                    turn = 'computer'  # sets turn = to computer so that the program will go for the cpu's turn

        else:
            # Computer's Turn
            move = get_computer_move(the_board, computer_letter)
            make_move(the_board, computer_letter, move)

            if is_winner(the_board, computer_letter):
                draw_board(the_board)
                print("The computer has beaten you! You lose.")
                game_is_playing = False
            else:
                if is_board_full(the_board):
                    draw_board(the_board)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'
    print("Do you want to play again (yes or no)")
    if not input().lower().startswith("y"):
        break
