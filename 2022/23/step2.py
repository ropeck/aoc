#!/usr/bin/python3
from collections import defaultdict
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
    if path:
      self.read_board(path)

  def board(self, y, x):
    if self.is_elf(y, x):
      return ELF
    else:
      return SPACE

  def is_elf(self, y, x):
    return self.has_elf.get((y,x))

  def neighbors(self, y, x):
    n = []
    for ex in range(x-1, x+2):
      for ey in range(y-1, y+2):
        if self.is_elf(ey, ex):
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
    for ey,ex in self.has_elf.keys():
      if not self.neighbors(ey, ex):
        continue
      space_found = False
      #print("elf",ey,ex)
      for m in self.moves:
        #print(m)
        #for y,x in m:
          #print(f'{y},{x} {b[y+ey][x+ex]}')
        if all([not self.is_elf(y+ey, x+ex) for y,x in m]):
          space_found = True
          y, x = m[0]
          target_space = (ey+y, ex+x)
          break
      if space_found:
        p.append([(ey, ex), target_space])
        t[target_space] = t.get(target_space, 0) + 1

    moved = False
    for move in p:
      y,x = move[1]
      if t.get((y,x), 0) == 1:
        #print("move", move)
        oy, ox = move[0]
        del(self.has_elf[(oy, ox)])
        self.has_elf[(y, x)] = True
        self.board[y] = None
        moved = True
    self.rotate_moves()
    return moved

  def ys(self):
    return [y for y,x in self.has_elf.keys()]

  def xs(self):
    return [x for x,x in self.has_elf.keys()]

  def draw(self):
    for y in range(min(self.ys()), max(self.ys())+1):
      if not self.board[y]:
        row = [ELF if self.is_elf(y, x) else SPACE for x in range(min(self.xs()), max(self.xs())+1)]
        self.board[y] = "".join(row)
      print(self.board[y])
    print("")

  def read_board(self, path):
    self.has_elf = defaultdict(lambda: False)
    self.board = {}
    y = 0
    with open(path, "r") as fh:
      for line in fh:
        self.board[y] = line.strip()
        for x, mark in enumerate(list(line.strip())):
          if mark == ELF:
            self.has_elf[(y, x)] = True
        y += 1

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
