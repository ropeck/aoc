#!/usr/bin/python3
import aocd
import re
import sys
from copy import deepcopy

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

  def z(self, t=0):
    return self.pos[2] + t * self.delta[2]
  
  def xy(self, t):
    n = [self.pos[i] + t * self.delta[i] for i in range(2)]
    return tuple(n)

  def xyz(self, t):
    r = list(self.xy(t))
    r.append(self.z(t))
    return tuple(r)
  
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
  total = 0

  # list of lines x, y, x @ dx, dy, dz
  # '19, 13, 30 @ -2,  1, -2'
  lines = [Line(str) for str in data if str]
  
  t = 1
  n = 0
  initpos = None
  initdelta = None

  lines = sorted(lines, key=lambda l: l.z(t))
  first = lines[0]

  for t in range(2,10):
    lines = sorted(lines, key=lambda l: l.z(t))
    print(t, [l.xyz(t) for l in lines[:6]])
    if not initpos:
      p = lines[n]
      dx = p.pos[0] - first.pos[0]
      dy = p.pos[1] - first.pos[1]
      dz = p.pos[2] - first.pos[2]

      initpos = (first.pos[0] - dx, first.pos[1] - dy, first.pos[2] - dz)
      initdelta = (dx*(t-1), dy*(t-1), dz*(t-1))
    else:
      nx, ny, nz = [initpos[i]+initdelta[i]*t for i in range(3)]
      if lines[n].xyz(t) == (nx, ny, nz):
        n += 1
        print("match", n, lines[n].xyz())
      else:
        initpos = None


  if not test and False:
    aocd.submit(total, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
