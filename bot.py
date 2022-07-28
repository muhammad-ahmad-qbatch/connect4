from shutil import move
from tabnanny import check
from random import *
from tkinter import EXCEPTION
import numpy as np
from project import  *

def create_board():
    board = np.zeros((6,7 ), dtype=np.uint8)
    return board

def bot_func():
        print('-------Bot turn--------')
        #ones = np.count_nonzero(board==1)
        # print(ones)
        # if ones==3:
        #     self.win('bot',self.board)
        # else:
        board=create_board()
        count=0
        size= len(board)-1
        bot_row= size
        while count<=10:
            bot_col=random.randint(0, size)
            print(bot_col)
            print(bot_row)
            if board[bot_row][bot_col] !=0 and bot_row-1<0:
                bot_col=choice([i for i in range(0,size) if i not in [bot_col]])
            if board[bot_row][bot_col]==2 or board[bot_row][bot_col]==1:
                while board[bot_row][bot_col]!=0:
                    bot_row=bot_row-1
                move(board,bot_row,bot_col,2,'bot')
                count=count+1
                win(board, size)
                if(result):
                    print('BOT WON!')
                    break  
                #b.player(board,bot_row)
            else:
                bot_last_row=size
                while board[bot_last_row][bot_col]!=0:
                    bot_last_row=bot_last_row-1 
                move(board,bot_last_row,bot_col,2,'bot')
                result= win(board, size)
                if result:
                    print('BOT WON!')
                    break
                else:
                    count=count+1
                #b.player(board,bot_last_row) 
            
def move(board,row,column,piece,player):   
    try:
        board[row][column] = piece
        print(board)
    
    except Exception as e:
        print('Error', e)
        
def win(board, size):
    row_c=6
    col_c=7
    print('IN win')
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
        for r in range(row_c):
            if board[r][c] == 2 and board[r-1][c+1] == 2 and board[r-2][c+2] == 2 and board[r-3][c+3] == 2:
               return True      
    
if __name__== '__main__':
    bot_func()
            
                    
            