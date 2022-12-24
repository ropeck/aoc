#!/usr/bin/python3
from collections import defaultdict
import sys

WALL = "#"
SPACE = "."
STORM = {"<": (-1,0), ">": (1,0), "^": (0,-1), "v": (0,1)}

class Storm:
  def __init__(self, y, x, dir):
    self.x = x
    self.y = y
    self.dir = dir

  def move(self):
    (dy, dx) = STORM[self.dir]
    # check for wall at new spot and restart

  def mark(self, b):
    v = b.b[self.y][self.x]
    if v in STORM.keys():
      n = "2"
    if v != SPACE:
      n = str(int(v) + 1)
    else:
      n = self.dir
    b.b[self.y][self.x] = n

class Valley:
  def __init__(self, path=None):
    self.moves = [
             [(-1,0),(-1,-1),(-1,1)],
             [(1,0),(1,-1),(1,1)],
             [(0,-1),(-1,-1),(1,-1)],
             [(0,1),(-1,1),(1,1)],
            ]
    if path:
      self.read_board(path)

  def read_board(self, path):
    self.board = []
    self.storms = []
    y = 0
    with open(path, "r") as fh:
      for line in fh:
        for x, mark in enumerate(list(line.strip())):
          st = STORM.get(mark, False)
          if st:
            self.storms.append(Storm(y, x, mark))
        self.board.append(list(line.strip()))
        y += 1

  def move_storms(self):
    for s in self.storms:
      s.move()

  def find_path(self):
    # put start on queue
    while not queue_empty:
      self.move_storms()
      nx, ny = pop_move
      # find possible moves, push them onto the queue to check. save storms too?
      # for each move:
      #   at exit?:
      #      add path score
   sort the paths by score
   return best path

def main(path):
  v = Valley(path)
  return v.find_path()

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
