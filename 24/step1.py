#!/usr/bin/python3
from collections import deque
import sys

WALL = "#"
SPACE = "."
STORM = {"<": (0,-1), ">": (0,1), "^": (-1,0), "v": (1,0)}
DIR = STORM

class Storm:
  def __init__(self, valley, x, y, dir):
    self.x_init = x
    self.x = x
    self.y_init = y
    self.y = y
    self.dir = dir
    self.valley = valley

  def __repr__(self):
    return f'<Storm ({self.x_init},{self.y_init}) {self.dir}>'
  def width(self):
    return self.valley.width
  def height(self):
    return self.valley.height

  def move(self, t):
    (dy, dx) = DIR[self.dir]
    # adjust to edges here..
    self.x = 1 + ((self.x_init + t*dx - 1) % (self.width()-2))
    self.y = 1 + ((self.y_init + t*dy - 1) % (self.height()-2))
    return self.position()
  def position(self):
    return (self.x, self.y)


class Valley:
  def __init__(self, path):
    self.board = []
    self.storms = []
    h = 0
    with open(path, "r") as fh:
      self.board = fh.read().splitlines()
      for line in self.board:
        row = list(line.strip())
        for x, mark in enumerate(row):
          if mark in STORM.keys():
            self.storms.append(Storm(self, x, h, mark))
        h += 1
    self.height = len(self.board)
    self.width = len(self.board[0])
    for x, v in enumerate(self.board[0]):
      if v == SPACE:
        self.start = (x, 0)
    for x, v in enumerate(self.board[-1]):
      if v == SPACE:
        self.finish = (x, self.height-1)

  def draw(self, coord=None, mark=None):
    b = [r.copy() for r in self.board]
    if coord:
      y,x=coord
      b[y][x] = mark
    for l in b:
      print("".join(l))
    print("")

  def find_path(self):
    found=[]
    queue = deque([(1, self.start, []),])
    while queue:
      if found:
        break
      print(len(queue))

      (t, (x, y), p) = queue.popleft()
      orig_p = p.copy()
      for s in self.storms:
        s.move(t)
      b=[s.position() for s in self.storms]
      b.sort()
      moved = False
      for dir, (dy, dx) in DIR.items():
        new_loc = (x + dx, y + dy)
        if new_loc == self.finish:
          found.append((t, p.copy()))
        if ((x + dx <= 0 or x + dx >= self.width-1) or
            (y + dy <= 0 or y + dy >= self.height-1)):
          continue
        if self.board[y+dy][x+dx] == WALL:
          continue
        if new_loc not in b:
          queue.append((t + 1, new_loc, p + [(x, y, dir)]))
          moved = True
      if (x,y) not in b and moved:
        queue.append((t+1, (x, y), p+ [(x, y, "W")]))



    return found

def main(path):
  v = Valley(path)
  res = v.find_path()
  print(v.finish)
  print("len", len(res))
  for l in res[:10]:
    print(l)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
