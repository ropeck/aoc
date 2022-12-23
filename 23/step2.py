#!/usr/bin/python3
import sys

ELF = "#"
SPACE = "."

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
    self.update_elf_loc()

  def update_elf_loc(self):
    self.has_elf={}
    for y in range(len(self.b)):
      for x in range(len(self.b[y])):
        if self.is_elf(y, x):
          self.has_elf[(y,x)] = True

  def board(self, y, x):
    b = self.b
    if (x < 0 or x > len(b[0])-1 or
        y < 0 or y > len(b)-1):
         return None
    return b[y][x]

  def cmp(self, y, x, v):
    return self.board(y, x) == v

  def is_elf(self, y, x):
    return self.cmp(y, x, ELF)

  def neighbors(self, y, x):
    n = []
    for ex in range(x-1, x+2):
      for ey in range(y-1, y+2):
        if self.has_elf.get((ey, ex), False):
          n.append((ey,ex))
    n.remove((y,x))
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
    for ey,ex in self.has_elf.keys():
      if not self.neighbors(ey, ex):
        continue
      space_found = False
      #print("elf",ey,ex)
      for m in self.moves:
        #print(m)
        #for y,x in m:
          #print(f'{y},{x} {b[y+ey][x+ex]}')
        if all([not self.has_elf.get((y+ey, x+ex), False) for y,x in m]):
          space_found = True
          y, x = m[0]
          target_space = (ey+y, ex+x)
          break
      if space_found:
        ty = y + ey
        tx = x + ex
        #print(f'move {ey},{ex} to {ty},{tx}')
        p.append([(ey, ex), target_space])
        t[target_space] = t.get(target_space, 0) + 1

    moved = False
    for move in p:
      y,x = move[1]
      if t.get((y,x), 0) == 1:
        #print("move", move)
        oy, ox = move[0]
        self.b[oy][ox] = SPACE
        self.b[y][x] = ELF
        del(self.has_elf[(oy, ox)])
        self.has_elf[(y, x)] = True
        moved = True
    self.rotate_moves()
    return moved

  def enlarge_board(self):
    b = self.b
    update = False
    if ELF in b[0]:
      b = [[SPACE for x in b[0]]] + b
      update = True
    if ELF in b[-1]:
      b = b + [[SPACE for x in b[0]]]
      update = True
    if any([b[y][0] == ELF for y in range(len(b))]):
      c = [[SPACE] + l for l in b]
      b = c
      update = True
    if any([b[y][-1] == ELF for y in range(len(b))]):
      c = [l + [SPACE] for l in b]
      b = c
      update = True
    self.b = b
    if update:
      self.update_elf_loc()

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
