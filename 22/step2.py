#!/usr/bin/python3
from icecream import ic
import re
import sys
from collections import deque

# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
DIR_NUMBER = '>v<^'
TURN={'L': -1, 'R': 1}
MOVEDIR = {'>': (0,1), '<': (0,-1), '^': (-1,0), 'v': (1,0)}
HEIGHT = WIDTH = 50
FACE_ORIGINS = [(50,0), (100,0), (50, 50), (0, 100), (50, 100), (0, 150)]

class Grid:
  def __init__(self, path):
    with open(path, "r") as fh:
      (griddata, followdata) = fh.read().split("\n\n")
    self.follow = deque(re.findall("(\d+|[LR])", followdata))
    self.grid_source = []
    for line in griddata.splitlines():
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

    self.set_pos(*self.find_start())
    self.set_dir(0)
                   #      R       D       L       U
    self.facemap = {1: [(2, 0), (3, 0), (2, 0), (5, 0)],
                    2: [(1, 0), (2, 0), (1, 0), (2, 0)],
                    3: [(3, 0), (5, 0), (3, 0), (1, 0)],
                    4: [(5, 0), (6, 0), (5, 0), (6, 0)],
                    5: [(4, 0), (1, 0), (4, 0), (3, 0)],
                    6: [(6, 0), (4, 0), (6, 0), (4, 0)]
                    }


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
    face, rot = self.facemap[self.cur_face+1][self.dir]
    return face-1, rot

  def move_forward(self, n=1):
    (dy, dx) = MOVEDIR[DIR_NUMBER[self.dir]]
    for i in range(n):
      ny = self.y + dy
      nx = self.x + dx
      updated = False
      next_face = self.cur_face
      rot = 0
      if nx < 0:
        updated = True
        next_face, rot = self.cubemap('<')
        # U and D can have rot==1 or 0
        # L and R can have rot==2 or -1 or 0
        if rot == -1:
          z = ny
          ny = nx
          nx = z
      elif nx >= WIDTH:
        updated = True
        next_face, rot = self.cubemap('>')
        if rot == -1:
          z = ny
          ny = nx
          nx = z
      if ny < 0:
        updated = True
        next_face, rot = self.cubemap('^')
        if rot:
          z = ny
          ny = nx
          nx = z
      elif ny >= HEIGHT:
        updated = True
        next_face, rot = self.cubemap('v')
        if rot:
          z = ny
          ny = nx
          nx = z
      new_dir = self.dir
      if updated:
        new_dir = self.turn(rot)
        ny %= WIDTH
        nx %= HEIGHT
      if self.get(nx, ny, next_face) == "#":
        print(f'wall {(next_face+1,ny,nx)}')
        return False
      self.x = nx
      self.y = ny
      self.set_dir(new_dir)
      self.cur_face = next_face
    return True

  def process_follow(self):
    follow = self.follow.copy()
    s=0
    while follow:
      move = follow.popleft()
      s += 1
      print(f'[{s}]')
      x, y = self.get_pos()
      print(f'{x},{y} move {move}')
      if move in ["L","R"]:
        self.set_dir(self.turn(TURN[move]))
        print(f'turn {move} dir {DIR_NUMBER[self.dir]} {MOVEDIR[DIR_NUMBER[self.dir]]}')
        continue
      #print(f'grid[{x},{y}]={grid[ny][nx]}')
      else:
        self.move_forward(int(move))

    print(x, y, DIR_NUMBER[self.dir])
    #  The final password is the sum of 1000 times the row, 4 times the column, and the facing.
    pw = (y+1)*1000 + (x+1)*4 + self.dir
    return pw

  def turn(self, quarters):
    return (self.dir + quarters) % len(DIR_NUMBER)


def draw(b, y=None):
  b = [["{:3d}".format(i)] + s for i,s in enumerate(b)]
  if y:
    b = b[y-5:y+5]
  for l in b:
    print("".join(l).rstrip())
  print("")

class Grid3d(Grid):

  def __init__(self, data):
    super(Grid3d, self).__init__(data)
                   #      R       D       L       U
    self.facemap = {1: [(2, 0), (3, 0), (4, 2), (6, 1)],
                    2: [(5, 2), (3, 1), (1, 0), (6, 0)],
                    3: [(2, -1), (5, 0), (4, -1), (1, 0)],
                    4: [(5, 0), (6, 0), (1, 2), (3, 1)],
                    5: [(2, 2), (6, 1), (4, 0), (3, 0)],
                    6: [(5, -1), (2, 0), (1, -1), (4, 0)]
                    }

def main(path):
  grid = Grid(path)
  pw1 = grid.process_follow()
  print(f'part1 password: {pw1}')

  grid3d = Grid3d(path)
  pw = grid3d.process_follow()
  print(f'part1 password: {pw1}')
  print(f'part2 password: {pw}')

  return pw



if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
