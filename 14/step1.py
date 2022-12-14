#!/usr/bin/python3
from functools import reduce
import sys

class Drawing:
  def __init__(self, path):
    drawing = []
    with open(path,"r") as fh:
      for line in fh:
        drawing.append([tuple([int(x) for x in p.split(",")]) for p in line.strip().split(" -> ")])
    for l in drawing:
      print(l)
    self.d = drawing
    flat = reduce(lambda a, b: a+b, self.d)
    self.min_x = min([x for (x,y) in flat])
    self.max_x = max([x for (x,y) in flat])
    self.min_y = min([y for (x,y) in flat])
    self.max_y = max([y for (x,y) in flat])
    self.width = self.max_x - self.min_x
    self.height = self.max_y - self.min_y

    self.grid = [[" " for x in range(self.width)] for y in range(self.height)]

    for l in drawing:
      c = l[-1]
      for m in l[:-1]:
        if c[0] == m[0]:
          # vertical line
          vl = [m[1], c[1]]
          vl.sort()
          for y in range(vl[0], vl[1]):
            self.grid[y-self.min_y-1][c[0]-self.min_x-1] = '#'
        else:
          # horizontal line
          hl = [m[0], c[0]]
          hl.sort()
          for x in range(hl[0], hl[1]):
            self.grid[c[1]-self.min_y-1][x-self.min_x-1] = '#'
    self.print()

  def print(self):
    print("\n".join(["".join(l) for l in self.grid]))


def main(path):
  d = Drawing(path)
  # d.print()
  return d.d

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
