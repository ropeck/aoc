#!/usr/bin/python3
from collections import deque
import sys

WALL = "#"
SPACE = "."
STORM = {"<": (0,-1), ">": (0,1), "^": (-1,0), "v": (1,0)}
DIR = STORM

class Storm:
  def __init__(self, x, y, dir):
    self.x_init = x
    self.y_init = y
    self.dir = dir

  def move(self, t):
    self.x = (self.x_init + t) % self.width
    self.y = (self.y_init + t) % self.height


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

  def find_path(self):
    t = 1
    path = []
    queue = deque()
    for x, v in enumerate(self.board[0]):
      if self.board[0][x] == SPACE:
        queue.append((0,x))
    print("initial state")
    self.draw((0,x), "E")
    move_dir = ""
    prev = None
    while queue:
      self.move_storms()
      ey, ex = queue.pop()
      if (ey, ex) not in path:
        path.append((ey, ex))
      for dir, (dy, dx) in DIR.items():
        ny = (ey + dy) % self.height
        nx = (ex + dx) % self.width
        if self.board[ny][nx] == SPACE and (ny, nx) not in path:
          queue.append((ny,nx))
          move_dir = dir
          break
      val = self.board[ey][ex]
      if move_dir == "wait" and len(queue) == 0:
        queue.append(prev)
        (ny, nx) = prev
        move_dir = None
      elif not queue:
        move_dir = "wait"
        queue.append((ey, ex))
      prev = (ey, ex)
      # loop around position looking for open spaces, put them on the queue
      # save current location to path
      # choose the move and mark it
      print(queue)
      print("Minute", t, "move", move_dir)
      self.draw((ny,nx), "E")
      t += 1
      if t>30:
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
