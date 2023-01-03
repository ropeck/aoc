#!/usr/bin/python3
from collections import deque
import re
import sys
import tkinter

# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
DIR_NUMBER = '>v<^'
TURN = {'L': -1, 'R': 1}
MOVEDIR = {'>': (0, 1), '<': (0, -1), '^': (-1, 0), 'v': (1, 0)}
FACE_ORIGINS = [(1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (0, 3)]


class Grid:
  def __init__(self, path, size=50):
    with open(path, "r") as fh:
      (griddata, followdata) = fh.read().split("\n\n")
    self.follow = deque(re.findall('(\d+|[LR])', followdata))
    self.grid_source = []
    for line in griddata.splitlines():
        line = (line + " "*150)[:150]
        # print(line+"|")
        self.grid_source.append(list(line))
    self.face = []
    self.width = size
    self.height = size
    for cx, cy in FACE_ORIGINS:
      cx *= self.width
      cy *= self.height
      f = []
      for y in range(50):
        f.append(self.grid_source[cy+y][cx:cx+50+1])
      self.face.append(f)
    self.cur_face = 0
    self.x, self.y = self.find_start()
    self.set_dir(0)
                   #      R       D       L       U
    self.facemap = {1: [(2, 0), (3, 0), (2, 0), (5, 0)],
                    2: [(1, 0), (2, 0), (1, 0), (2, 0)],
                    3: [(3, 0), (5, 0), (3, 0), (1, 0)],
                    4: [(5, 0), (6, 0), (5, 0), (6, 0)],
                    5: [(4, 0), (1, 0), (4, 0), (3, 0)],
                    6: [(6, 0), (4, 0), (6, 0), (4, 0)]
                    }
    self.screen = tkinter.Tk()
    self.screen.geometry("1200x1250")
    self.canvas = tkinter.Canvas(self.screen, width=170*5, height=220*5)
    for fx, fy in FACE_ORIGINS:
      x = fx*self.width*5 + 10
      y = fy*self.height*5 + 10
      self.canvas.create_rectangle(x, y, x+self.width*5, y+self.height*5)
    self.canvas.pack()

    self.screen.update_idletasks()
    self.screen.update()


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
    if x is None:
      x = self.x
    if y is None:
      y = self.y
    ox, oy = FACE_ORIGINS[self.cur_face]
    ox *= self.width
    oy *= self.height
    return x + ox, y + oy

  def set_dir(self, direction):
    self.dir = direction

  def find_start(self):
    x = 0
    y = 0
    while self.get(x, y) != ".":
      x += 1
    return x, y

  def cubemap(self, dir):
    face, rot = self.facemap[self.cur_face+1][DIR_NUMBER.index(dir)]
    return face-1, rot

  def draw_circle(self, x, y):
    pass

  def draw_triangle(self, x, y):
    pass

  #@snoop
  def move_forward(self, n=1, check_wall=True):
    for i in range(n):
      self.draw_circle(self.x, self.y)
      (dy, dx) = MOVEDIR[DIR_NUMBER[self.dir]]
      ny = self.y + dy
      nx = self.x + dx
      self.draw_triangle(ny, nx)
      updated = False
      next_face = self.cur_face
      rot = 0
      print(f'{self.cur_face+1} {(self.x, self.y)} {dx},{dy} {DIR_NUMBER[self.dir]}')
      if nx < 0:
        updated = True
        next_face, rot = self.cubemap('<')
        # U and D can have rot==1 or 0
        # L and R can have rot==2 or -1 or 0
        if rot == -1:
          z = ny
          ny = nx
          nx = z
        if rot == 2:
          nx = self.width - nx - 1
          ny = self.height - ny - 1
      elif nx >= self.width:
        updated = True
        next_face, rot = self.cubemap('>')
        if rot == -1:
          nx = ny
          ny = self.height -1
        if rot == 2:
          nx = self.width - nx - 1
          ny = self.height - ny - 1
      if ny < 0:
        updated = True
        next_face, rot = self.cubemap('^')
        if rot:
          ny = nx
          nx = 0
      elif ny >= self.height:
        updated = True
        next_face, rot = self.cubemap('v')
        if rot:
          ny = nx
          nx = self.width - 1
      new_dir = self.dir
      if updated:
        new_dir = self.turn(rot)
        ny %= self.width
        nx %= self.height

      if self.get(nx, ny, next_face) == "#" and check_wall:
        print(f'wall {next_face+1} {(ny,nx)}')
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
      print(f''
            f'{self.cur_face+1} {self.x},{self.y} move {move}')
      if move in ["L","R"]:
        self.set_dir(self.turn(TURN[move]))
        print(f'turn {move} dir {DIR_NUMBER[self.dir]} {MOVEDIR[DIR_NUMBER[self.dir]]}')
        continue
      #print(f'grid[{x},{y}]={grid[ny][nx]}')
      else:
        self.move_forward(int(move))

    x, y = self.get_pos()
    print(x, y, DIR_NUMBER[self.dir])
    #  The final password is the sum of 1000 times the row, 4 times the column, and the facing.
    pw = (y+1)*1000 + (x+1)*4 + self.dir
    return pw

  def turn(self, quarters):
    return (self.dir + quarters) % len(DIR_NUMBER)

# use pygame or graphics library to draw a visualization of the movement around the board
# the whole board might fit on the screen or just show the current cube face
# mark the # spaces with an X or color, and show the cursor as it moves around the faces
# ... should be able to see it move around the map as expected

def draw(b, y=None):
  b = [["{:3d}".format(i)] + s for i,s in enumerate(b)]
  if y:
    b = b[y-5:y+5]
  for l in b:
    print("".join(l).rstrip())
  print("")

class Grid3d(Grid):

  def __init__(self, data, size=50):
    super(Grid3d, self).__init__(data, size)
                   #      R       D       L       U
    self.facemap = {1: [(2, 0), (3, 0), (4, 2), (6, 1)],
                    2: [(5, 2), (3, 1), (1, 0), (6, 0)],
                    3: [(2, -1), (5, 0), (4, -1), (1, 0)],
                    4: [(5, 0), (6, 0), (1, 2), (3, 1)],
                    5: [(2, 2), (6, 1), (4, 0), (3, 0)],
                    6: [(5, -1), (2, 0), (1, -1), (4, 0)]
                    }

def main(path):
  # grid = Grid(path)
  # pw1 = grid.process_follow()
  # print(f'part1 password: {pw1}')

  grid3d = Grid3d(path)
  # grid3d.set_dir(2)
  # grid3d.cur_face = 5
  # grid3d.move_forward(grid3d.width*4+5, check_wall=False)
  pw = grid3d.process_follow()
  # print(f'part1 password: {pw1}')
  print(f'part2 password: {pw}')
  grid3d.screen.mainloop()
  return pw



if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)


