#!/usr/bin/python3
from collections import deque
import re
import sys

# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
FACE = '>v<^'
TURN={'L': -1, 'R': 1}
MOVEDIR = {'>': (0,1), '<': (0,-1), '^': (-1,0), 'v': (1,0)}
HEIGHT = WIDTH = 50

class Grid:
  def __init__(self, grid_data):
    self.grid_source = []
    for line in grid_data.splitlines():
        line = (line + " "*150)[:150]
        print(line+"|")
        self.grid_source.append(list(line))
    self.face = []
    for cx, cy in [(50,0), (100,0), (50, 50), (0, 100), (50, 100), (0, 150)]:
      f = []
      for y in range(50):
        f.append(self.grid_source[cy+y][cx:cx+50+1])
      self.face.append(f)
    self.cur_face = 0


  def get(self, x, y):
    return self.face[self.cur_face][y][x]

  def set(self, x, y, v):
    self.face[self.cur_face][y][x] = v

  def set_pos(self, x, y):
    self.x = x
    self.y = y

  def get_pos(self):
    return self.x, self.y

  def set_dir(self, dir):
    self.dir = dir

  def find_start(self):
    x = 0
    y = 0
    while self.get(x, y) != ".":
      x += 1
    return x, y

  def cubemap(self, dir):
    facemap = {(0, 'L'): (4, 2)}
    try:
      face, rot = facemap[(self.cur_face, self.dir)]
      return face, rot
    except KeyError:
      return self.cur_face, 0

  def move_forward(self):
    (dy, dx) = MOVEDIR[FACE[self.dir]]
    grid = self.face[self.cur_face]
    ny = self.y + dy
    nx = self.x + dx
    new_face = None
    if nx < 0:
      new_face, rot = self.cubemap('L')
    elif nx > WIDTH:
      new_face, rot = self.cubemap('R')
    if ny < 0:
      new_face, rot = self.cubemap('D')
    elif ny > WIDTH:
      new_face, rot = self.cubemap('U')
    if new_face:
      ny %= WIDTH
      nx %= HEIGHT
    return nx, ny

def draw(b, y=None):
  b = [["{:3d}".format(i)] + s for i,s in enumerate(b)]
  if y:
    b = b[y-5:y+5]
  for l in b:
    print("".join(l).rstrip())
  print("")

def main(path):
  with open(path, "r") as fh:
    (griddata, followdata) = fh.read().split("\n\n")
  grid = Grid(griddata)
  follow = deque(re.findall("(\d+|[LR])", followdata))

  grid.set_pos(*grid.find_start())
  grid.set_dir(0)

  while follow:
    move = follow.popleft()
    x, y = grid.get_pos()
    print(f'{x},{y} move {move}')
    if move in ["L","R"]:
      grid.set_dir((grid.dir + TURN[move]) % len(FACE))
      print(f'turn {move} grid.dir {FACE[grid.dir]} {MOVEDIR[FACE[grid.dir]]}')
      continue
    #print(f'grid[{x},{y}]={grid[ny][nx]}')

    for n in range(int(move)):
      nx, ny = grid.move_forward()
      grid.set(x,y, FACE[grid.dir])
      if grid.get(nx, ny) == "#":
        break
      x = nx
      y = ny
    #draw(grid, y)

  print(x,y,FACE[dir])
  #  The final password is the sum of 1000 times the row, 4 times the column, and the facing.
  pw = (y+1)*1000 + (x+1)*4 + dir
  print(f'password: {pw}')
  return pw



if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
