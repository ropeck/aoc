#!/usr/bin/python3
import aocd
import re
import sys

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
    return f"<{s}>"

  def val(self, n):
    return [d[n] for d in self.d]
  
  def val_overlap(self, other, n):
    return (min(self.val(n)) >= max(other.val(n)) and
            max(self.val(n)) <= min(other.val(n)))
    
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

def main(test):
  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  d = [Brick(line) for line in data]
  d = sorted(d, key=lambda x: x.key())

  for br in d:
    print(br)
    while br.drop():
      print(br)
    print("---")

  if not test:
    aocd.submit(len(p), part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
