#!/usr/bin/python3
from collections import defaultdict
import sys

WALL = "#"
SPACE = "."
STORM = {"<": (-1,0), ">": (1,0), "^": (0,-1), "v": (0,1)}

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
            self.storms.append([(y,x), mark])
        self.board.append(list(line.strip()))
        y += 1

def main(path):
  v = Valley(path)
  print("\n".join(["".join(r) for r in v.board]))
  print(v.storms)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
