#!/usr/bin/python3
from collections import deque
from icecream import ic
import re
import sys

# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
DIR_NUMBER = '>v<^'
TURN={'L': -1, 'R': 1}
MOVEDIR = {'>': (0,1), '<': (0,-1), '^': (-1,0), 'v': (1,0)}
HEIGHT = WIDTH = 50
FACE_ORIGINS = [(50,0), (100,0), (50, 50), (0, 100), (50, 100), (0, 150)]

class Grid:
  def __init__(self, grid_data):
    self.grid_source = []
    for line in grid_data.splitlines():
        line = (line + " "*150)[:150]
        print(line+"|")
        self.grid_source.append(list(line))
    self.face = []
    for cx, cy in FACE_ORIGINS:
      f = []
      for y in range(50):
        f.append(self.grid_source[cy+y][cx:cx+50+1])
      self.face.append(f)
    self.cur_face = 0


  def get(self, x, y, f=None):
    if f == None:
      f = self.cur_face
    return self.face[f][y][x]

  def set(self, x, y, v):
    self.face[self.cur_face][y][x] = v

  def set_pos(self, x, y):
    self.x = x
    self.y = y

  def get_pos(self, x=None, y=None):
    if x == None:
      x = self.x
    if y == None:
      y = self.y
    ox, oy = FACE_ORIGINS[self.cur_face]
    return x + ox, y + oy

  def set_dir(self, dir):
    self.dir = dir

  def find_start(self):
    x = 0
    y = 0
    while self.get(x, y) != ".":
      x += 1
    return x, y

  def cubemap(self, dir):
    self.set_dir(DIR_NUMBER.index(dir))
                #     R       D       L       U
    facemap = {1: [(2, 0), (3, 0), (2, 0), (5, 0)],
               2: [(1, 0), (2, 0), (1, 0), (2, 0)],
               3: [(3, 0), (5, 0), (3, 0), (1, 0)],
               4: [(5, 0), (6, 0), (5, 0), (6, 0)],
               5: [(4, 0), (1, 0), (4, 0), (3, 0)],
               6: [(6, 0), (4, 0), (6, 0), (4, 0)]
              }
    face, rot = facemap[self.cur_face+1][self.dir]
    return face-1, rot

  def move_forward(self):
    (dy, dx) = MOVEDIR[DIR_NUMBER[self.dir]]
    ny = self.y + dy
    nx = self.x + dx
    updated = False
    next_face = self.cur_face
    if nx < 0:
      updated = True
      next_face, rot = self.cubemap('<')
    elif nx >= WIDTH:
      updated = True
      next_face, rot = self.cubemap('>')
    if ny < 0:
      updated = True
      next_face, rot = self.cubemap('^')
    elif ny >= HEIGHT:
      updated = True
      next_face, rot = self.cubemap('v')
    if updated:
      ny %= WIDTH
      nx %= HEIGHT
    if self.get(nx, ny, next_face) == "#":
      print(f'wall {self.get_pos()}')
      return False
    self.x = nx
    self.y = ny
    self.cur_face = next_face
    return True

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

  grid.set_pos(*grid.find_start())
  grid.set_dir(0)

  while follow:
    move = follow.popleft()
    s += 1
    print(f'[{s}]')
    x, y = grid.get_pos()
    print(f'{x},{y} move {move}')
    if move in ["L","R"]:
      grid.set_dir((grid.dir + TURN[move]) % len(DIR_NUMBER))
      print(f'turn {move} grid.dir {DIR_NUMBER[grid.dir]} {MOVEDIR[DIR_NUMBER[grid.dir]]}')
      continue
    #print(f'grid[{x},{y}]={grid[ny][nx]}')

    for n in range(int(move)):
      if not grid.move_forward():
        break
    #draw(grid, y)

  print(x, y, DIR_NUMBER[grid.dir])
  #  The final password is the sum of 1000 times the row, 4 times the column, and the facing.
  pw = (y+1)*1000 + (x+1)*4 + grid.dir
  print(f'password: {pw}')
  return pw



if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
