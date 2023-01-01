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
    self.grid = []
    for line in grid_data.splitlines():
        line = (line + " "*150)[:150]
        print(line+"|")
        self.grid.append(list(line))

  def get(self, x, y):
    return self.grid[y][x]

  def set(self, x, y, v):
    self.grid[y][x] = v

  def find_start(self):
    x = 0
    y = 0
    while self.get(x, y) != ".":
      x += 1
    return x, y

  def move_forward(self, x, y, dx, dy):
    ny = (y + dy) % len(self.grid)
    nx = (x + dx) % len(self.grid[ny])
    while self.get(nx,ny) == " ":
      ny = (ny + dy) % len(self.grid)
      nx = (nx + dx) % len(self.grid[ny])
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
  s = 0

  (x,y) =grid.find_start()
  dir = 0  # face right

  while follow:
    move = follow.popleft()
    s += 1
    print(f'[{s}]')
    print(f'{x},{y} move {move}')
    if move in ["L","R"]:
      dir = (dir + TURN[move]) % len(FACE)
      print(f'turn {move} dir {FACE[dir]} {MOVEDIR[FACE[dir]]}')
      continue
    (dy, dx) = MOVEDIR[FACE[dir]]
    #print(f'grid[{x},{y}]={grid[ny][nx]}')

    for n in range(int(move)):
      nx, ny = grid.move_forward(x, y, dx, dy)
      x_mod = nx % WIDTH
      y_mod = ny % HEIGHT
      grid.set(x,y, FACE[dir])
      if grid.get(nx, ny) == "#":
        print (f'wall {(x,y)}')
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
