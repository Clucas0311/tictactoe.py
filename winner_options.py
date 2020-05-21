def is_winner(bo, le):
    # Given a board and a player's letter, this function returns True if
    # that player has won.
    # 'bo'  = 'board' instead of board and "le" = "letter" to make it easier
    # Checks to see if board == letter at that position then assigns true
        #i.e board[7] = 'X' and le = X - result will be true
    return ((bo[7] == le and bo[8] == le and bo[9] == le)) # Across the top
    return ((bo[4] == le and bo[5] == le and bo[6] == le)) # Across the middle
    return ((bo[1] == le and bo[2] == le and bo[3] == le))  #Across the bottom
    return ((bo[7] == le and bo[4] == le and bo[1] == le)) # Down the left side
    return ((bo[8] == le and bo[5] == le and bo[2] == le)) # Down the middle
    return ((bo[9] == le and bo[6] == le and bo[5] == le)) # Down the right side
    return ((bo[1] == le and bo[5] == le and bo[9] == le)) # left diagonally
    return ((bo[7] == le and bo[5] == le and bo[3] == le)) # right diagonally

    
