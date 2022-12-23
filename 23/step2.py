#!/usr/bin/python3
import sys

class Board:
  def __init__(self, path=None):
    self.moves = [
             [(-1,0),(-1,-1),(-1,1)],
             [(1,0),(1,-1),(1,1)],
             [(0,-1),(-1,-1),(1,-1)],
             [(0,1),(-1,1),(1,1)],
            ]
    self.b = []
    if path:
      self.read_board(path)


  def elf_loc(self):
    e=[]
    for y in range(len(self.b)):
      for x in range(len(self.b[y])):
        if self.b[y][x] == "#":
          e.append((y,x))
    return e

  def neighbors(self, y, x):
    n = []
    b = self.b
    for dy in range(y-1,y+2):
      for dx in range(x-1,x+2):
        if dx==x and dy==y:
          continue
        if (dx < 0 or dx > len(b[0])-1 or
            dy < 0 or dy > len(b)-1):
             continue
        if b[dy][dx] == "#":
          n.append((dy,dx))
    return n

  def rotate_moves(self):
    moves = self.moves
    m = moves[0]
    moves = moves[1:]
    moves.append(m)
    self.moves = moves

  def move_elves(self):
    p = []
    t = {}
    self.enlarge_board()
    for ey,ex in self.elf_loc():
      if not self.neighbors(ey, ex):
        continue
      space_found = False
      #print("elf",ey,ex)
      for m in self.moves:
        #print(m)
        #for y,x in m:
          #print(f'{y},{x} {b[y+ey][x+ex]}')
        if all([self.b[y+ey][x+ex]!="#" for y,x in m]):
          space_found = True
          y, x = m[0]
          target_space = (ey+y, ex+x)
          break
      if not space_found:
        continue
      ty = y + ey
      tx = x + ex
      #print(f'move {ey},{ex} to {ty},{tx}')
      p.append([(ey, ex), target_space])
      t[target_space] = t.get(target_space, 0) + 1
    for move in p:
      y,x = move[1]
      if t.get((y,x), 0) == 1:
        #print("move", move)
        oy, ox = move[0]
        self.b[oy][ox] = "."
        self.b[y][x] = "#"
    self.rotate_moves()
    return p

  def enlarge_board(self):
    b = self.b
    if "#" in b[0]:
      b = [["." for x in b[0]]] + b
    if "#" in b[-1]:
      b = b + [["." for x in b[0]]]
    if any([b[y][0] == "#" for y in range(len(b))]):
      c = [["."] + l for l in b]
      b = c
    if any([b[y][-1] == "#" for y in range(len(b))]):
      c = [l + ["."] for l in b]
      b = c
    self.b = b
    return b

  def draw(self):
    for l in self.b:
      print("".join(l))
    print("")

  def read_board(self, path):
    b = []
    with open(path, "r") as fh:
      for line in fh:
        b.append(list(line.strip()))
    self.b = b

  def find_moves(self):
    i = 1
    while self.move_elves():
      print(i)
      self.draw()
      i += 1
    return i


def main(path):
  b = Board(path)
  i = b.find_moves()

  print("rounds", i)
  return i




if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
