import numpy as np
from random import *
import random
from winner import win

#Conext manager
class FileManager():
    """
    This class implements the FileManager interface and takes filename and mode as parameters. It takes care of closing
    the file automatically if it is opened.
    """ 
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
      
         
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
     
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        
        
class GameBoard:
    
    def __init__(self, row, col) -> None:
        self.col = col
        self.row = row
        print(self.row)
        
        
    def create_board(self):
        self.board = np.zeros((self.row, self.col ), dtype = np.uint8)
        return self.board
    
    
    def read(self):
        """This function reads win count from the file and returns it as an integer.

        Returns:
            integer: reads the whole file and extracts win count from it.
        """
        self.count = open('result', 'r') 
        content = self.count.readlines()
        for line in content:
            for i in line:
                    
                # Checking for the digit in
                # the string
                if i.isdigit() == True:
                    self.count = i
                    return self.count
    
                 
    def move(self, board, row, column, piece): 
        """This function places the piece into the board.

        Args:
            board (2D array): 
            row (integer): 
            column (integer): 
            piece (integer): 
            player (string): 
        """
        try:
            board[row][column] = piece
            print(board)
         
        except Exception as e:
            print('Error', e)
                        
                                                                       
    def player(self, board, player_row):
        """This function allows the player to move the piece into the board.
        
         Args:
            board (2D array): 
            player_row (integer): row of the board where the piece will be placed.
        """        
        print('-------Player 1 turn--------')
        flag = True
        row = player_row - 1
        
        print('player row : ', row)
        while flag:
            try:
                col = int(input('Player 1 enter column: '))
                if col > len(board) - 1:
                    raise Exception
            except Exception:
                print('Invalid input') 
            else:
                if board[row][col] == 1 or board[row][col] == 2:
                    while board[row][col] != 0:
                        try:
                            row = row - 1
                            if row < 0:
                                raise Exception
                        except Exception:
                            print('Out of range. Try again')
                               
                    self.move(board, row, col, 1)
                    return board 
                
                                          
                else:
                    last_row = player_row - 1
                    while board[last_row][col] != 0:
                        last_row = last_row - 1
                    self.move(board, last_row, col, 1)
                    return board   
                
                            
            finally:         
                if flag == False:
                    break 
                
                 
    def bot_func(self, board, b_row):
        """This function is called after the player has done its move. It'll automatically pick a colum using random
        numpy function within the board range.
         Args:
            board (2D array): 
            b_row (integer): row of the board where the piece will be placed."""
    
        print('-------Bot turn--------')
        ones = np.count_nonzero(board == 1)
        # print(ones)
        # flag=0
        # if ones>=3:
        #     flag=self.bot_move(board)
        # if flag==0 or flag==-1:
        size = len(board) - 1
        bot_row = b_row - 1
        bot_col = random.randint(0, size)
        print(bot_col)
        print(bot_row)
        if board[bot_row][bot_col] != 0 and bot_row - 1 < 0:
            bot_col = choice([i for i in range(0, size) if i not in [bot_col]])
        if board[bot_row][bot_col] == 2 or board[bot_row][bot_col] == 1:
            while board[bot_row][bot_col] != 0:
                bot_row = bot_row - 1
            self.move(board, bot_row, bot_col, 2)
            return board
          
        else:
            bot_last_row = 5
            while board[bot_last_row][bot_col] != 0:
                bot_last_row = bot_last_row - 1 
            self.move(board, bot_last_row, bot_col, 2)
            return board   
        
 
                                                        
if __name__ == '__main__':
    flag = True
    game_board = GameBoard(row=6, col=7)
    player_count = int(game_board.read())
    fix_board = game_board.create_board()
    print(fix_board)
    _board = game_board.player(fix_board, 6)
    
    while flag:
        _board = game_board.bot_func(_board, 6)
        _bot = win('bot', _board)
        if _bot:
            print('BOT wins')
            break
        _board = game_board.player(_board, 6)
        _player = win('player', _board)
        if _player:
            with FileManager('result', 'w') as f:
                player_count = player_count+1
                f.write(f"Player wins: {player_count}")
            print('Player wins')
            break
        
                                