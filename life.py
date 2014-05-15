#!/usr/bin/python3
import random

def evolve( array ):
### esegue lo step di evoluzione del gioco life su una tabella sferica
   rows = len(array)
   columns = len(array[0])
   array2 = [[0 for j in range(rows)] for i in range(columns)]

   for i in range( 0, rows-1 ):
      for j in range( 0, columns-1 ):
         totale = array[(i-1)%(rows)][(j-1)%(columns)]+array[(i-1)%(rows)][j%(columns)]+array[(i-1)%(rows)][(j+1)%(columns)]+array[i%(rows)][(j-1)%(columns)]+array[i%(rows)][j%(columns)]+array[i%(rows)][(j+1)%(columns)]+array[(i+1)%(rows)][(j-1)%(columns)]+array[(i+1)%(rows)][j%(columns)]+array[(i+1)%(rows)][(j+1)%(columns)]
         #print( totale )
         if array[i][j] == 0:
            if totale == 3:
               array2[i][j]=1
            else:
               array2[i][j]=0
         if array[i][j] == 1:
            if totale <= 2:
               array2[i][j]=0
            elif totale <= 4:
               array2[i][j]=1
            else:
               array2[i][j]=0

   return array2

def start_configuration( lenght = 6 ):
### genera la tabella iniziale quadrata e di dimensione iniziale lenght
   board = [[]]
   line = []
   random.seed()

   for a in range( lenght ):
      line = []
      for b in range( lenght ):
          tmp = random.randint( -1, 1 )
          if tmp > 0:
             line.append( 1 )
          else:
             line.append( 0 )
      board.append( line )

   board.remove([])
   return board

board = [[]]
board = start_configuration( 7 )
      
for i,v in enumerate(board):
   print(board[i])

print("\n")

while True:
   ok = input()
   board = evolve( board )
   for i,v in enumerate(board):
      print(board[i])
