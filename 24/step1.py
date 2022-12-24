#!/usr/bin/python3
from collections import defaultdict
import sys

WALL = "#"
SPACE = "."
STORM = {"<": (0,-1), ">": (0,1), "^": (-1,0), "v": (1,0)}

class Storm:
  def __init__(self, board, x, y, dir):
    self.x = x
    self.y = y
    self.dir = dir
    self.board = board

  def move(self):
    (dy, dx) = STORM[self.dir]
    ny = (self.y + dy) % self.board.height
    nx = (self.x + dx) % self.board.width
    while self.board.board[ny][nx] == WALL:
      ny = (ny + dy) % self.board.height
      nx = (nx + dx) % self.board.width
    self.unmark()
    self.y = ny
    self.x = nx
    self.mark()

  def unmark(self):
    v = self.board.board[self.y][self.x]
    if v in STORM.keys():
      n = SPACE
    elif v != SPACE:
      n = str(int(v) - 1)
    if n == "1":
      n = self.dir
    self.board.board[self.y][self.x] = n


  def mark(self):
    v = self.board.board[self.y][self.x]
    if v in STORM.keys():
      n = "2"
    elif v != SPACE:
      n = str(int(v) + 1)
    else:
      n = self.dir
    self.board.board[self.y][self.x] = n

class Valley:
  def __init__(self, path):
    self.board = []
    self.storms = []
    y = 0
    with open(path, "r") as fh:
      for line in fh:
        for x, mark in enumerate(list(line.strip())):
          st = STORM.get(mark, False)
          if st:
            self.storms.append(Storm(self, x, y, mark))
        self.board.append(list(line.strip()))
        y += 1
    self.height = len(self.board)
    self.width = len(self.board[0])

  def draw(self):
    for l in self.board:
      print("".join(l))
    print("")

  def move_storms(self):
    for s in self.storms:
      s.move()

  def find_path(self):
    # put start on queue
    t = 1
    while True:
      print("Minute", t)
      self.draw()
      self.move_storms()
      t += 1
      # nx, ny = pop_move
      # find possible moves, push them onto the queue to check. save storms too?
      # for each move:
      #   at exit?:
      #      add path score
   # sort the paths by score
   # return best path

def main(path):
  v = Valley(path)
  return v.find_path()

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
