#!/usr/bin/python3
from functools import reduce
import os
import sys

class Drawing:
  START = (500, 0)
  def __init__(self, path):
    drawing = []
    with open(path,"r") as fh:
      for line in fh:
        drawing.append([tuple([int(x) for x in p.split(",")]) for p in line.strip().split(" -> ")])
    for l in drawing:
      print(l)
    self.d = drawing
    flat = reduce(lambda a, b: a+b, self.d)
    flat.append(Drawing.START)
    self.min_x = min([x for (x,y) in flat]) - 5
    self.max_x = max([x for (x,y) in flat]) + 5
    self.min_y = min([y for (x,y) in flat])
    self.max_y = max([y for (x,y) in flat])
    self.width = self.max_x - self.min_x
    self.height = self.max_y - self.min_y
    self.sand = 0

    self.grid = [[" " for x in range(self.width+1)] for y in range(self.height+4)]

    for l in drawing:
      c = l[0]
      for m in l[1:]:
        if c[0] == m[0]:
          # vertical line
          vl = [m[1], c[1]]
          vl.sort()
          for y in range(vl[0], vl[1]+1):
            self.set(c[0], y)
        else:
          # horizontal line
          hl = [m[0], c[0]]
          hl.sort()
          for x in range(hl[0], hl[1]+1):
            self.set(x, c[1])
        c = m
    self.set(*Drawing.START, '*')
    self.print()
    self.set(*Drawing.START, ' ')

  def set(self, x, y, m='#'):
    # print(f'g({x},{y})=#  g({x-self.min_x},{y-self.min_y})=#')
    self.grid[y - self.min_y][x - self.min_x] = m

  def make_bigger(self):
    padding = [' ' for n in range(int((self.max_x - self.min_x) / 2))]
    g = [ padding + row + padding for row in self.grid]
    self.grid = g
    self.min_x -= len(padding)
    self.max_x += len(padding)

  def get(self, x, y):
    if x > self.max_x or x < self.min_x:
      self.make_bigger()
    return  self.grid[y - self.min_y][x - self.min_x]
  def empty(self, x, y):
    return self.get(x, y) == ' ' and y < self.max_y + 3

  def print(self):
    os.system("clear")
    print("\n".join(["".join(l) for l in self.grid]))
    print(f'sand: {self.sand}')

  def mark_sand(self, x, y):
    # print(f'[{x},{y}] = *')
    self.set(x, y, '*')

  def drop_sand(self):
    (x, y) = Drawing.START
    while self.empty(*Drawing.START) :
      if self.empty(x, y+1):
        y = y + 1
        continue
      if self.empty(x-1, y+1):
        x = x - 1
        y = y + 1
        continue
      if self.empty(x+1, y+1):
        x = x + 1
        y = y + 1
        continue
      self.mark_sand(x, y)
      (x, y) = Drawing.START
      self.sand += 1
      # if self.sand % 10 == 0:
      #   self.print()
    self.print()


def main(path):
  d = Drawing(path)
  d.drop_sand()
  # d.print()
  return d.d

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
