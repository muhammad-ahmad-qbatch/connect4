
import numpy as np


class board:
    def __init__(self,size) -> None:
        self.size=size
    def create_board(self):
        self.board = np.zeros((self.size,self.size ), dtype=np.uint8)
        return self.board     
    # def show(self,board):
    #     #cells = [" ", "●", "○"]
    #     for i in range(self.size+1):
    #         print(' ',i, end =' ')  
    #     print("")        
    #     for row in reversed(board):
    #         print("+---" * self.size  + "+---+")
    #         print("|   " * self.size  + "|   |")
        print("+---" * self.size  + "+---+")
    def move(self,board,row,column,piece):
      try: 
        board[row][column] = piece
      except Exception as e:
          print('Error', e)
      else:      
        print(board)
        
    def player1(self,board): 
     print('-------Player 1 turn--------')    
     flag=True
     while(flag):
      try:   
       row=int(input('Player 1 enter row: '))  
       col=int(input('Player 1 enter column: '))
      except Exception:
        print('Invalid input')  
      else:    
        if board[row][col]==0:   
          self.move(a,row,col,1)
          result=self.win('player1',board)
          if result==True:
             print(result)
             flag=False
             break
          else:
            self.player2(board)
        else:
          print("Position occupied") 
          continue 
    
    def player2(self,board):
      print('-------Player 2 turn--------')  
      flag=True
      while(flag):
        try:   
         row=int(input('Player 2 enter row: '))  
         col=int(input('Player 2 enter column: '))
        except Exception:
          print('Invalid input')  
        else:    
          if board[row][col]==0:   
            self.move(a,row,col,2)
            result=self.win('player2',board)
            if result==True:
             print(result)
             flag=False
             break
            else:
             self.player1(board)
          else:
            print("Position occupied") 
            continue 
     
        
    def win(self,player,board):
     if(player=='player1'):
       for c in range(self.size):
         for r in range(self.size):
             if board[r][c] == 1 and board[r][c+1] == 1 and board[r][c+2] == 1 and board[r][c+3] == 1:
                return True 
    #----------Checking vertically-----------
       for c in range(self.size):
         for r in range(self.size):
            if board[r][c] == 1 and board[r+1][c] == 1 and board[r+2][c] == 1 and board[r+3][c] == 1:
                return True
            
       for c in range(self.size-3):
         for r in range(self.size-3):
            if board[r][c] == 1 and board[r+1][c+1] == 1 and board[r+2][c+2] == 1 and board[r+3][c+3] == 1:
                return True
    
    # Check for downward sloping diagonal 4 in a row for win
       for c in range(self.size):
          for r in range(3, self.size):
            if board[r][c] == 1 and board[r-1][c+1] == 1 and board[r-2][c+2] == 1 and board[r-3][c+3] == 1:
                return True 
            
            
                
    #--------------------Player 2----------------
    
     if(player=='player2'):
       for c in range(self.size):
         for r in range(self.size):
             if board[r][c] == 2 and board[r][c+1] == 2 and board[r][c+2] == 2 and board[r][c+3] == 2:
                return True 
    #----------Checking vertically-----------
       for c in range(self.size):
         for r in range(self.size):
            if board[r][c] == 2 and board[r+1][c] == 2 and board[r+2][c] == 2 and board[r+3][c] == 2:
                return True
            
       for c in range(self.size-3):
         for r in range(self.size-3):
            if board[r][c] == 2 and board[r+1][c+1] == 2 and board[r+2][c+2] == 2 and board[r+3][c+3] == 2:
                return True
    
    # Check for downward sloping diagonal 4 in a row for win
       for c in range(self.size):
          for r in range(3, self.size):
            if board[r][c] == 2 and board[r-1][c+1] == 2 and board[r-2][c+2] == 2 and board[r-3][c+3] == 2:
                return True             
        
        
            
 



if __name__== '__main__':
    x=int(input("Please enter the board size\n"))
    b=board(x)
    count=0
    a=b.create_board()
    b.player1(a)

    
       
  
        