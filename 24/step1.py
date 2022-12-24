#!/usr/bin/python3
from collections import deque
import sys

WALL = "#"
SPACE = "."
STORM = {"<": (0,-1), ">": (0,1), "^": (-1,0), "v": (1,0)}
DIR = STORM

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

  def draw(self, coord=None, mark=None):
    b = [r.copy() for r in self.board]
    if coord:
      y,x=coord
      b[y][x] = mark
    for l in b:
      print("".join(l))
    print("")

  def move_storms(self):
    for s in self.storms:
      s.move()

  def find_path(self):
    t = 1
    path = []
    queue = deque()
    for x, v in enumerate(self.board[0]):
      if self.board[0][x] == SPACE:
        queue.append((0,x))
    move_dir = ""
    while queue:
      self.move_storms()
      ey, ex = queue.pop()
      path.append((ey, ex))
      for dir, (dy, dx) in DIR.items():
        ny = ey + dy
        nx = ex + dx
        if self.board[ny][nx] == SPACE and ((ey, ex) != (ny, nx) or move_dir == "wait"):
          queue.append((ny,nx))
          move_dir = dir
      if not queue:
        move_dir = "wait"
        queue.append(path[-1])
      # loop around position looking for open spaces, put them on the queue
      # save current location to path
      # choose the move and mark it
      print(queue)
      print("Minute", t, "move", move_dir)
      self.draw((ny,nx), "E")
      t += 1
      if t>10:
        break
      if ey == len(self.board):
        break
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
