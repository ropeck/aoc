#!/usr/bin/python3
import aocd
import re
import sys
from copy import deepcopy

_DAY = 22

class Brick:

  def __init__(self, str=None):
    #  '1,0,1~1,2,1'
    self.str = str
    self.d = []
    if str:
      for st in str.split("~"):
        e = [int(x) for x in st.split(",")]
        self.d.append(tuple(e))

  def __repr__(self):
    s = " - ".join([str(i) for i in self.d])
    return re.sub(" ", "", f"<{s}>")

  def val(self, n):
    return [d[n] for d in self.d]
  
  def val_overlap(self, other, n):
    return (min(self.val(n)) <= max(other.val(n)) and
            max(self.val(n)) >= min(other.val(n)))
  
    #   self   other
    #   [3, 5] [4, 7] yes
    #   [3, 5] [5, 7] yes
    #   [3, 5] [6, 8] no
  
  
  def overlap(self, other):
    if str(self) == str(other):
      return False 
    for n in range(3):
      if not self.val_overlap(other, n):
        return False
    return True
    
  def key(self):
    return self.min_z()

  def min_z(self):
    return min(self.val(2))  # Z
  
  def move_z(self, dz=-1):
    nd = []
    for x, y, z in self.d:
      nd.append((x, y, z+dz))
    self.d = nd

  def drop(self):
    if self.min_z() == 1:
      return False
    self.move_z(-1)
    return True
  
  def xy(self):
    x,y,z = self.d[0]
    return (x, y)

def main(test):
  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  d = [Brick(line) for line in data]
  d = sorted(d, key=lambda x: x.key())

  for i in range(len(d)):
    br = d[i]
    o = False
    while not o and br.drop():
      for b in d:
        if br.overlap(b):
          br.move_z(1)  # move it back up
          o = True
          break
    d[i] = br
  
  print(d)

  p = []   # list of bricks that can be removed
  for n in range(len(d)):
    dd = deepcopy(d)
    del dd[n]
    dropped = False
    for i in range(len(dd)):
      br = dd[i]
      ov = False
      if not br.drop():
        ov = True
        continue
      for b in dd:
        if br.overlap(b):
          br.move_z(1)
          ov = True
          break
      if ov:
        break
    if not ov:
      p.append(n)

  print("dropped", len(p), p)
  if not test:
    aocd.submit(len(p), part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
