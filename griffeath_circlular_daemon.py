#!/usr/bin/python3
import random
from tkinter import *


class CellularAutoma:
   def __init__(self, lenght=500, scale=1, levels=10):
      """genera la tabella iniziale quadrata e di dimensione iniziale lenght"""
      self.board = [[]]
      self.pantone = []
      self.scale = scale
      self.levels = levels
      self.time = 0
      line = []
      random.seed()
      
      for a in range( lenght ):
         line = []
         for b in range( lenght ):
             line.append( random.randint( 0, self.levels-1 ))
         self.board.append( line )
            
      self.board.remove([])

      #inizializzo ambiente grafico 
      self.master = Tk()
      self.master.title('Griffeath circular cellular automata')
      self.w = Canvas(self.master, width=lenght*self.scale, height=lenght*self.scale)
      self.w.pack()

      #generate pantone
      for a in range( self.levels ):
         self.pantone.append( "#"+str(random.randint( 100000,999999 )))

   def evolve( self ):
      """esegue lo step di evoluzione del gioco life su una tabella sferica"""
      rows = len(self.board)
      columns = len(self.board[0])
      board2 = [[0 for j in range(rows)] for i in range(columns)]
     

      for i in range( 0, rows ):
         for j in range( 0, columns ):
            if (self.board[(i-1)%(rows)][j%(columns)]-1)%self.levels  == self.board[i][j]:
               board2[i][j] = (self.board[i][j]+1)%self.levels
            elif (self.board[i%(rows)][(j-1)%(columns)]-1)%self.levels  == self.board[i][j]:
               board2[i][j] = (self.board[i][j]+1)%self.levels
            elif (self.board[i%(rows)][(j+1)%(columns)]-1)%self.levels  == self.board[i][j]:
               board2[i][j] = (self.board[i][j]+1)%self.levels
            elif (self.board[(i+1)%(rows)][j%(columns)]-1)%self.levels  == self.board[i][j]:
               board2[i][j] = (self.board[i][j]+1)%self.levels
            else:
               board2[i][j] = self.board[i][j]

      self.board = board2
      print("time: %d" %self.time )
      self.time = self.time+1

   def show( self ):
      """Gives a graphical representation of the data"""
      self.w.delete(ALL)
      for i,v in enumerate(self.board):
         for j,w in enumerate( self.board[i] ):
               self.w.create_rectangle(i*self.scale, j*self.scale, i*self.scale+self.scale, j*self.scale+self.scale, fill=self.pantone[self.board[i][j]], outline=self.pantone[self.board[i][j]] )

############
### main ###
############
dim = input( "Inserisci la dimensione della board: ") 
board = CellularAutoma( lenght=int(dim), scale=1)

board.show()

while True:
   board.evolve( )
   board.show()
   board.master.update()
