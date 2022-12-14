#!/usr/bin/python3
from functools import reduce
import sys

class Drawing:
  def __init__(self, path):
    drawing = []
    with open(path,"r") as fh:
      for line in fh:
        drawing.append([tuple(p.split(",")) for p in line.strip().split(" -> ")])
    for l in drawing:
      print(l)
    self.d = drawing
    flat = reduce(lambda a, b: a+b, self.d)
    self.min_x = min([x for (x,y) in flat])
    self.max_x = max([x for (x,y) in flat])
    self.min_y = min([y for (x,y) in flat])
    self.max_y = max([y for (x,y) in flat])


def main(path):
  d = Drawing(path)
  return d.d

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
