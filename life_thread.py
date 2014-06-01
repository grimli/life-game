#!/usr/bin/python3
import random
from tkinter import *
import threading
import queue

class Evolver( threading.Thread ):
   """ this thread calculate next status
   The result is maid available to the shower trough a queue """
   def __init__(self, queue):
      threading.Thread.__init__(self)
      self.queue = queue

   def run(self):
      while True:
         print("time: %d\n" % board.time)
         board.evolve()
         self.queue.put(1)

class CellularAutoma:
   def __init__(self, lenght=6, scale=10):
      """genera la tabella iniziale quadrata e di dimensione iniziale lenght"""
      self.board = [[]]
      self.scale = scale
      line = []
      random.seed()
      self.time = 0
      
      for a in range( lenght ):
         line = []
         for b in range( lenght ):
             tmp = random.randint( -1, 1 )
             if tmp > 0:
                line.append( 1 )
             else:
                line.append( 0 )
         self.board.append( line )
            
      self.board.remove([])

      #init GUI 
      self.master = Tk()
      self.master.title('life game')
      self.w = Canvas(self.master, width=lenght*self.scale, height=lenght*self.scale)
      self.w.pack()

   def evolve( self ):
      """esegue lo step di evoluzione del gioco life su una tabella sferica"""
      rows = len(self.board)
      columns = len(self.board[0])
      board2 = [[0 for j in range(rows)] for i in range(columns)]

      for i in range( 0, rows ):
         for j in range( 0, columns ):
            totale = self.board[(i-1)%(rows)][(j-1)%(columns)]+self.board[(i-1)%(rows)][j%(columns)]+self.board[(i-1)%(rows)][(j+1)%(columns)]+self.board[i%(rows)][(j-1)%(columns)]+self.board[i%(rows)][j%(columns)]+self.board[i%(rows)][(j+1)%(columns)]+self.board[(i+1)%(rows)][(j-1)%(columns)]+self.board[(i+1)%(rows)][j%(columns)]+self.board[(i+1)%(rows)][(j+1)%(columns)]
            if self.board[i][j] == 0:
               if totale == 3:
                  board2[i][j]=1
               else:
                  board2[i][j]=0
            if self.board[i][j] == 1:
               if totale <= 2:
                  board2[i][j]=0
               elif totale <= 4:
                  board2[i][j]=1
               else:
                  board2[i][j]=0

      self.board = board2
      self.time = self.time + 1 

   def show( self ):
      """Gives a graphical representation of the data"""
      self.w.delete(ALL)
      for i,v in enumerate(self.board):
         for j,w in enumerate( self.board[i] ):
            if (self.board[i][j] == 0):
               self.w.create_rectangle(i*self.scale, j*self.scale, i*self.scale+self.scale, j*self.scale+self.scale, fill="blue")
            else:
               self.w.create_rectangle(i*self.scale, j*self.scale, i*self.scale+self.scale, j*self.scale+self.scale, fill="yellow")

if __name__ == '__main__':
   dim = input( "Inserisci la dimensione della board: ") 
   board = CellularAutoma( lenght=int(dim), scale=5)

   queue = queue.Queue( maxsize=1 )
   t1 = Evolver(queue)

   t1.start()

   # Tkinter cannot be executed on a separeted thread
   while True:
      flag = queue.get()
      board2 = board
      queue.task_done()
      board2.show()
      board.master.update()
