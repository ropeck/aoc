#!/usr/bin/python3
import re
import sys
from collections import deque

# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
DIR_NUMBER = '>v<^'
TURN={'L': -1, 'R': 1}
MOVEDIR = {'>': 1, '<': -1, '^': -1j, 'v': 1j}
HEIGHT = WIDTH = 50
FACE_ORIGINS = [50, 100, 50 + 50j, 100j, 50 +100j, 150j]

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
    for c in FACE_ORIGINS:
      cx = int(c.real)
      cy = int(c.imag)
      f = []
      for y in range(50):
        f.append(self.grid_source[cy+y][cx:cx+50+1])
      self.face.append(f)
    self.cur_face = 0

    self.set_pos(self.find_start())
    self.set_dir(0)
                   #      R       D       L       U
    self.facemap = {1: [(2, 0), (3, 0), (2, 0), (5, 0)],
                    2: [(1, 0), (2, 0), (1, 0), (2, 0)],
                    3: [(3, 0), (5, 0), (3, 0), (1, 0)],
                    4: [(5, 0), (6, 0), (5, 0), (6, 0)],
                    5: [(4, 0), (1, 0), (4, 0), (3, 0)],
                    6: [(6, 0), (4, 0), (6, 0), (4, 0)]
                    }


  def get(self, p, f=None):
    if f == None:
      f = self.cur_face
    x = int(p.real)
    y = int(p.real)
    return self.face[f][y][x]

  def set(self, p, v):
    x = int(p.real)
    y = int(p.real)
    self.face[self.cur_face][y][x] = v

  def set_pos(self, p):
    self.p = p

  def get_pos(self, p=None):
    if p == None:
      p = self.p
    o = FACE_ORIGINS[self.cur_face]
    return o + p

  def set_dir(self, dir):
    self.dir = dir

  def find_start(self):
    p = complex(0,0)
    while self.get(p) != ".":
      p += 1
    return p

  def cubemap(self, dir):
    self.set_dir(DIR_NUMBER.index(dir))
    face, rot = self.facemap[self.cur_face+1][self.dir]
    return face-1, rot

  def move_forward(self, n=1):
    d = MOVEDIR[DIR_NUMBER[self.dir]]
    for i in range(n):
      np = self.get_pos() + d
      updated = False
      next_face = self.cur_face
      if np.real < 0:
        updated = True
        next_face, rot = self.cubemap('<')
      elif np.real >= WIDTH:
        updated = True
        next_face, rot = self.cubemap('>')
      if np.imag < 0:
        updated = True
        next_face, rot = self.cubemap('^')
      elif np.imag >= HEIGHT:
        updated = True
        next_face, rot = self.cubemap('v')
      if updated:
        self.turn(rot)
        if rot in [1, -1]:
          np = np * (rot * 1j)
        if rot == 2:
          np = np * (1j**2)
        nx = int(np.real)
        ny = int(np.imag)
        ny %= WIDTH
        nx %= HEIGHT
        np = complex(nx, ny)
        # rotate the current position on the face here?
        # use complex numbers and multiply by 1j to rotate?
      if self.get(np, next_face) == "#":
        print(f'wall {self.get_pos()}')
        return False
      self.p = np
      self.cur_face = next_face
    return True

  def process_follow(self):
    follow = self.follow.copy()
    s=0
    while follow:
      move = follow.popleft()
      s += 1
      print(f'[{s}]')
      p = self.get_pos()
      print(f'{p} move {move}')
      if move in ["L","R"]:
        self.turn(TURN[move])
        print(f'turn {move} dir {DIR_NUMBER[self.dir]} {MOVEDIR[DIR_NUMBER[self.dir]]}')
        continue
      #print(f'grid[{x},{y}]={grid[ny][nx]}')
      else:
        self.move_forward(int(move))

    x = int(p.real)
    y = int(p.real)
    print(x, y, DIR_NUMBER[self.dir])
    #  The final password is the sum of 1000 times the row, 4 times the column, and the facing.
    pw = (y+1)*1000 + (x+1)*4 + self.dir
    return pw

  def turn(self, quarters):
    self.set_dir((self.dir + quarters) % len(DIR_NUMBER))


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
    self.facemap = {1: [(2, 0), (3, 0), (3, 0), (6, 1)],
                    2: [(5, 2), (2, 0), (3, 1), (6, 0)],
                    3: [(2, -1), (3, 1), (5, 0), (1, 0)],
                    4: [(5, 0), (6, 0), (6, 0), (3, 1)],
                    5: [(2, 2), (6, 1), (6, 1), (3, 0)],
                    6: [(5, -1), (2, 0), (2, 0), (4, 0)]
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
