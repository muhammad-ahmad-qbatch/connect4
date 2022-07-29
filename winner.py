def win(player, board):
    row_c=6
    col_c=7
    if player=='player':
        for c in range(col_c-3):
            for r in range(row_c):
                if board[r][c] == 1 and board[r][c+1] == 1 and board[r][c+2] == 1 and board[r][c+3] == 1:
                    return True
        #----------Checking vertically-----------
        for c in range(col_c):
            for r in range(row_c-3):
                if board[r][c] == 1 and board[r+1][c] == 1 and board[r+2][c] == 1 and board[r+3][c] == 1:
                    return True
        for c in range(col_c-3):
            for r in range(row_c-3):
                if board[r][c] == 1 and board[r+1][c+1] == 1 and board[r+2][c+2] == 1 and board[r+3][c+3] == 1:
                    return True
        # Check for downward sloping diagonal 4 in a row for win
        for c in range(col_c-3):
            for r in range(3, row_c):
                if board[r][c] == 1 and board[r-1][c+1] == 1 and board[r-2][c+2] == 1 and board[r-3][c+3] == 1:
                    return True
            
    #----------------BOT---------------- 
    if player=='bot':  
        for c in range(col_c-3):
            for r in range(row_c):
                if board[r][c] == 2 and board[r][c+1] == 2 and board[r][c+2] == 2 and board[r][c+3] == 2:
                    return True
                
    #----------Checking vertically-----------
    for c in range(col_c):
        for r in range(row_c-3):
            if board[r][c] == 2 and board[r+1][c] == 2 and board[r+2][c] == 2 and board[r+3][c] == 2:
                return True
            
    for c in range(col_c-3):
        for r in range(row_c-3):
            if board[r][c] == 2 and board[r+1][c+1] == 2 and board[r+2][c+2] == 2 and board[r+3][c+3] == 2:
                return True
            
    # Check for downward sloping diagonal 4 in a row for win
    for c in range(col_c-3):
        for r in range(3,row_c):
            if board[r][c] == 2 and board[r-1][c+1] == 2 and board[r-2][c+2] == 2 and board[r-3][c+3] == 2:
                return True 