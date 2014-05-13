#!/usr/bin/python3
### game of life
### Author: Edoardo Bompiani
### Date: 15/04/2014
### Version: 0.6

import random

def evolve( array ):
### esegue lo step di evoluzione del gioco life su una tabella sferica
   rows = len(array)
   columns = len(array[0])
   array2 = array
   
# i=0, j=0 
   totale = array[rows-1][columns-1]+array[rows-1][0]+array[rows-1][1]+array[0][columns-1]+array[0][0]+array[0][1]+array[1][columns-1]+array[1][0]+array[1][1]
   if    array[0][0] == 0:
      if totale == 3:
         array2[0][0]=1
      else:
         array2[0][0]=0
   if array[0][0] == 1:
      if totale <= 2:
         array2[0][0]=0
      elif totale <= 4:
         array2[0][0]=1
      else:
         array2[0][0]=0
# i=rows-1, j=0 
   totale = array[rows-2][columns-1]+array[rows-2][0]+array[rows-2][1]+array[rows-1][columns-1]+array[rows-1][0]+array[rows-1][1]+array[0][columns-1]+array[0][0]+array[0][1]
   if    array[rows-1][0] == 0:
      if totale == 3:
         array2[rows-1][0]=1
      else:
         array2[rows-1][0]=0
   if array[rows-1][0] == 1:
      if totale <= 2:
         array2[rows-1][0]=0
      elif totale <= 4:
         array2[rows-1][0]=1
      else:
         array2[rows-1][0]=0

# i=0, j=columns-1
   totale = array[rows-1][columns-2]+array[rows-1][columns-1]+array[rows-1][0]+array[0][columns-2]+array[0][columns-1]+array[0][0]+array[1][columns-2]+array[1][columns-1]+array[1][0]
   if    array[0][columns-1] == 0:
      if totale == 3:
         array2[0][columns-1]=1
      else:
         array2[0][columns-1]=0
   if array[0][columns-1] == 1:
      if totale <= 2:
         array2[0][columns-1]=0
      elif totale <= 4:
         array2[0][columns-1]=1
      else:
         array2[0][columns-1]=0

# i=rows-1, j=columns-1 
   totale = array[rows-2][columns-2]+array[rows-2][columns-1]+array[rows-2][0]+array[rows-1][columns-2]+array[rows-1][columns-1]+array[rows-1][0]+array[0][columns-2]+array[0][columns-1]+array[0][0]
   if    array[rows-1][columns-1] == 0:
      if totale == 3:
         array2[rows-1][columns-1]=1
      else:
         array2[rows-1][columns-1]=0
   if array[rows-1][columns-1] == 1:
      if totale <= 2:
         array2[rows-1][columns-1]=0
      elif totale <= 4:
         array2[rows-1][columns-1]=1
      else:
         array2[rows-1][columns-1]=0

# i=0
   for j in range( 1, columns-2 ):
      totale = array[rows-1][j-1]+array[rows-1][j]+array[rows-1][j+1]+array[0][j-1]+array[0][j]+array[0][j+1]+array[1][j-1]+array[1][j]+array[1][j+1]
      #print( totale )
      if    array[0][j] == 0:
         if totale == 3:
            array2[0][j]=1
         else:
            array2[0][j]=0
      if array[0][j] == 1:
         if totale <= 2:
            array2[0][j]=0
         elif totale <= 4:
            array2[0][j]=1
         else:
            array2[0][j]=0

# i=rows-1
   for j in range( 1, columns-2 ):
      totale = array[rows-2][j-1]+array[rows-2][j]+array[rows-2][j+1]+array[rows-1][j-1]+array[rows-1][j]+array[rows-1][j+1]+array[0][j-1]+array[0][j]+array[0][j+1]
      #print( totale )
      if    array[rows-1][j] == 0:
         if totale == 3:
            array2[rows-1][j]=1
         else:
            array2[rows-1][j]=0
      if array[rows-1][j] == 1:
         if totale <= 2:
            array2[rows-1][j]=0
         elif totale <= 4:
            array2[rows-1][j]=1
         else:
            array2[rows-1][j]=0

# j=0
   for i in range( 1, rows-2 ):
      totale = array[i-1][columns-1]+array[i-1][0]+array[i-1][1]+array[i][columns-1]+array[i][0]+array[i][1]+array[i+1][columns-1]+array[i+1][0]+array[i+1][1]
      #print( totale )
      if    array[i][0] == 0:
         if totale == 3:
            array2[i][0]=1
         else:
            array2[i][0]=0
      if array[i][0] == 1:
         if totale <= 2:
            array2[i][0]=0
         elif totale <= 4:
            array2[i][0]=1
         else:
            array2[i][0]=0

# j=columns-1
   for i in range( 1, rows-2 ):
      totale = array[i-1][columns-2]+array[i-1][columns-1]+array[i-1][0]+array[i][columns-2]+array[i][columns-1]+array[i][0]+array[i+1][columns-2]+array[i+1][columns-1]+array[i+1][0]
      #print( totale )
      if    array[i][columns-2] == 0:
         if totale == 3:
            array2[i][columns-2]=1
         else:
            array2[i][columns-2]=0
      if array[i][columns-2] == 1:
         if totale <= 2:
            array2[i][columns-2]=0
         elif totale <= 4:
            array2[i][columns-2]=1
         else:
            array2[i][columns-2]=0

# other cases
   for i in range( 1, rows-2 ):
      for j in range( 1, columns-2 ):
         totale = array[i-1][j-1]+array[i-1][j]+array[i-1][j+1]+array[i][j-1]+array[i][j]+array[i][j+1]+array[i+1][j-1]+array[i+1][j]+array[i+1][j+1]
         #print( totale )
         if    array[i][j] == 0:
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
board = start_configuration( 6 )
      
for i,v in enumerate(board):
   print(board[i])

print("\n")

while True:
   ok = input()
   board = evolve( board )
   for i,v in enumerate(board):
      print(board[i])


### History:
### 0.6 - fixed evolve calculation
### 0.5 - aggiungo configurazione iniziale random
### 0.4 - completed loop for progressing evolution
### 0.3 - move the loop to function evolve
### 0.2 - develop basic loop to calculate next generation
### 0.1 - how to print a List of list?
