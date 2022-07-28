from shutil import move
from tabnanny import check
from tkinter import EXCEPTION
import numpy as np
from random import *
import random
import pdb

#Conext manager
class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
         
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        
    
class board:
    def __init__(self,row,col) -> None:
        self.col = col
        self.row = row
        print(self.row)
    def create_board(self):
        self.board = np.zeros((self.row,self.col ), dtype=np.uint8)
        return self.board
    
    def read(self):
        self.count = open('result','r') 
        content = self.count.readlines()
        for line in content:
            for i in line:
                    
                # Checking for the digit in
                # the string
                if i.isdigit() == True:
                    self.count=i
                    return self.count
                 
    def move(self,board,row,column,piece,player):   
        try:
            board[row][column] = piece
            print(board)
         
        except Exception as e:
            print('Error', e)
            
    def bot_move(self,board): 
        row_c=6
        col_c=7
        print('In bot move')
        for c in range(col_c-2):
            for r in range(row_c):
                if board[r][c] == 1 and board[r][c+1] == 1 and board[r][c+2] == 1:
                    print('loop1')
                    self.move(board,r,c,2,'bot')
                
        #----------Checking vertically-----------
        for c in range(col_c):
            for r in range(row_c-2):
                if board[r][c] == 1 and board[r+1][c] == 1 and board[r+2][c] == 1 :
                    print('loop2')
                    self.move(board,r,c,2,'bot')
                
        for c in range(col_c-2):
            for r in range(row_c-2):
                if board[r][c] == 1 and board[r+1][c+1] == 1 and board[r+2][c+2] == 1:
                    print('loop3')
                    self.move(board,r,c,2,'bot')
                
        # Check for downward sloping diagonal 4 in a row for win
        for c in range(col_c-2):
            for r in range(2,row_c):
                if board[r][c] == 2 and board[r-1][c+1] == 2 and board[r-2][c+2] == 2:
                   print('loop4')
                   self.move(board,r,c,2,'bot')
                else:   
                   return -1           
               
            
    def win(self,player, board):
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
                        
                                                        
    def player(self, board, player_row):
        print('-------Player 1 turn--------')
        flag = True
        row = player_row-1
        count=int(self.read())
        print('player row : ',row)
        while flag:
            try:
                col=int(input('Player 1 enter column: '))
                if col>len(board)-1:
                    raise Exception
            except Exception:
                print('Invalid input') 
            else:
                if board[row][col] == 1 or board[row][col] == 2:
                    while board[row][col] != 0:
                        try:
                            row = row-1
                            if row<0:
                                raise Exception
                        except Exception:
                            print('Out of range. Try again')
                               
                    self.move(board,row,col,1,'player')
                    return board
                  
                        
                else:
                    last_row = player_row-1
                    while board[last_row][col] != 0:
                        last_row = last_row-1
                    self.move(board,last_row,col,1,'player')
                    return board
               
                    
            finally:         
                if flag==False:
                    break 
                
                 
    def bot_func(self,board,b_row):
        print('-------Bot turn--------')
        ones = np.count_nonzero(board==1)
        # print(ones)
        # flag=0
        # if ones>=3:
        #     flag=self.bot_move(board)
        # if flag==0 or flag==-1:
        size = len(board)-1
        bot_row = b_row-1
        bot_col=random.randint(0, size)
        print(bot_col)
        print(bot_row)
        if board[bot_row][bot_col] !=0 and bot_row-1<0:
            bot_col = choice([i for i in range(0,size) if i not in [bot_col]])
        if board[bot_row][bot_col] == 2 or board[bot_row][bot_col] == 1:
            while board[bot_row][bot_col] != 0:
                bot_row = bot_row-1
            self.move(board,bot_row,bot_col,2,'bot')
            return board
          
        else:
            bot_last_row = 5
            while board[bot_last_row][bot_col] != 0:
                bot_last_row = bot_last_row-1 
            self.move(board,bot_last_row,bot_col,2,'bot')
            return board
                            
                                      
                        
if __name__ == '__main__':
    flag = True
    object = board(row=6,col=7)
    player_count = int(object.read())
    a = object.create_board()
    print(a)
    _board = object.player(a,6)
    
    while flag:
        _board = object.bot_func(_board,6)
        _bot = object.win('bot', _board)
        if _bot:
            print('BOT wins')
            break
        _board = object.player(_board,6)
        _player = object.win('player',_board)
        if _player:
            with FileManager('result', 'w') as f:
                player_count = player_count+1
                f.write(f"Player wins: {player_count}")
            print('Player wins')
            break
                    
                        