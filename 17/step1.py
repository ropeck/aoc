#!/usr/bin/python3
from pprint import pprint
import re
import sys

class Tower:
  def __init__(self):
    self.t = [0]   # each row is a byte
    self.rocks = self.read_rocks()
    self.rock_n = 0
    self.jet = self.read_jets()
    self.read_jets()

  def height(self):
    return len(self.t)

  def next_rock(self):
    n = self.rock_n
    if n + 1> len(self.rocks):
      n = 0
      self.rock_n = 0
    else:
      self.rock_n += 1
    return self.rocks[n]

  def read_jets(self):
    with open(path, "r") as fh:
      return fh.read()

  def drop(self, r):
    # start at top + 3, then apply jets and move down until stopped
    # self.t + [0, 0, 0]
    # loop from top down, check to see if the rock overlaps
    # use binary AND of the tower with the rock - if (rock & tower top ) != 0 then it's colliding
    tower = self.t + [0, 0, 0] + [0 for i in r[1]]
    tower.reverse()
    for i, row in enumerate(tower):
      if row & r[1][0]:
        break
    tower[i-1] = tower[i-1] | r[1][0]
    tower.reverse()
    self.t = [row for row in tower if row]
    print(self.t)
    # handle multiple line rocks
      # if overlap(tower, r, i):
      #   mark r
      #   break

  def read_rocks(self):
    rock_list = []
    with open("rocks","r") as fh:
      while True:
        r = []
        while True:
          l = fh.readline().strip()
          if not l:
            break
          w = len(l)
          byte = sum(2 ** i for i, v in enumerate(reversed([ch == "#" for ch in l])) if v)
          r.append(byte)
        if not r:
          return rock_list
        rock_list.append((w, r))


def main(path):
  t = Tower()
  t.drop(t.next_rock())
  t.drop(t.next_rock())

  for i in range(10):
    print(t.next_rock())
    print("")


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
