#!/usr/bin/python3
from collections import deque
from math import lcm
import sys

WALL = "#"
SPACE = "."
STORM = {"<": (0,-1), ">": (0,1), "^": (-1,0), "v": (1,0)}
DIR = STORM

class Board:
  def __init__(self, path):
    self.storms = []
    with open(path, "r") as fh:
      self.board = fh.read().splitlines()
      for y, line in enumerate(self.board):
        row = list(line.strip())
        for x, mark in enumerate(row):
          if mark in STORM.keys():
            self.storms.append((x, y, mark))
    self.height = len(self.board)
    self.width = len(self.board[0])
    for x, v in enumerate(self.board[0]):
      if v == SPACE:
        self.start = (x, 0)
    for x, v in enumerate(self.board[-1]):
      if v == SPACE:
        self.finish = (x, self.height-1)
    self.state = []
    self.lcm = lcm(self.width - 2, self.height - 2)
    for t in range(self.lcm):
      b = [[SPACE for x in range(self.width)] for y in range(self.height)]
      for (x, y, dir) in self.storms:
        (dy, dx) = DIR[dir]
        fx = 1 + ((x + t * dx - 1) % (self.width - 2))
        fy = 1 + ((y + t * dy - 1) % (self.height - 2))
        v = b[fy][fx]
        if v != SPACE:
          if v in DIR.keys():
            v = '2'
          else:
            v = str(int(v) + 1)
        else:
          v = dir
        b[fy][fx] = v
      self.state.append(b)

  def find_path(self):
    visited = set()
    q = deque([(1, self.start, []),])
    while q:
      t, (x, y), p = q.popleft()
      tt = (t+1)%self.lcm
      if (tt, x, y) in visited:
        continue
      visited.add((tt, x, y))
      if self.state[tt][y][x] == SPACE:
        q.append((t+1, (x,y), p.copy() + [((x,y), "W")]))
      for dir, (dy, dx) in DIR.items():
        ny = (dy + y) % self.height
        nx = (dx + x) % self.width
        if (nx, ny) == self.finish:
          return t, p
        if (0 >= nx or nx >= self.width-1):
          continue
        if (0 >= ny or ny >= self.height-1):
          continue
        if self.state[tt][ny][nx] == SPACE:
          q.append((t+1,(nx, ny),  p.copy() + [((x,y), dir)]))
    print ("not found")


def main(path):
  v = Board(path)
  res = v.find_path()
  print ("time", res)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
