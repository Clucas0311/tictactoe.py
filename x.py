def input_player_letter():
    # Lets the player enter which letter they want to be
    # Returns a list with the player's letter as the first item and  the computer's letter as a second.
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        letter = input("Do you want to be X or O?: ")
        letter = letter.upper()

print(input_player_letter())
