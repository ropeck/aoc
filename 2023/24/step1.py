#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 24

class Line:
  def __init__(self, str):
    m = re.match(r"[- 0-9]+,[- 0-9]+,[- 0-9]+ @ [- 0-9]+,[- 0-9]+,[- 0-9]+", str)
    if not m:
      raise ValueError(m)
    a, b = str.split("@")
    x, y, z = [int(n) for n in a.split(",")]
    dx, dy, dz = [int(n) for n in b.split(",")]
    self.m = float(dy) / float(dx)
    self.pos = (x, y, z)
    self.delta = (dx, dy, dz)
    self.b = self.pos[1] - self.pos[0] * self.m

  def __repr__(self):
    return f"<Line {self.pos} @ {self.delta}>"
  
  def intersect(self, other):
    # return intersection of this line and other, or None
    # y = mx + b
    # m1 * x + b1 = m2 * x + b2
    # x * (m1 - m2) = b2 - b1
    # x = (b2 - b1) / (m1 - m2)

    if self.m == other.m:
      return None
    
    x = (other.b - self.b) / (self.m - other.m)
    y = self.m * x + self.b
    ta = (x - self.pos[0]) / (self.delta[0])
    tb = (x - other.pos[0]) / (other.delta[0])
    if ta < 0 or tb < 0:
      return None
    return (x, y)

def main(test):
  test = 1
  MIN = 7
  MAX = 27

  # MIN = 200000000000000
  # MAX = 400000000000000
  # test = 0

  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  # list of lines x, y, x @ dx, dy, dz
  # '19, 13, 30 @ -2,  1, -2'
  lines = [Line(str) for str in data if str]
  

  total = 0
  for i, s in enumerate(lines):
    for o in lines[i+1:]:
      x = s.intersect(o)
      if x and x[0] > MIN and x[0] < MAX:
        print(s, o, s.intersect(o))
        total += 1
  print("total", total)

  if not test:
    aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
