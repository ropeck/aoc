#!/usr/bin/python3
from pprint import pprint
import re
import sys

class Tower:
  def __init__(self):
    self.t = [0]   # each row is a byte
    self.rocks = self.read_rocks()
    self.pending_rocks = self.rocks.copy()

    self.rock_n = 0
    self.jet = self.read_jets()
    self.read_jets()

  def height(self):
    return len(self.t)

  def next_rock(self):
    if not self.pending_rocks:
      self.pending_rocks = self.rocks.copy()
      self.pending_rocks.reverse()
    return self.pending_rocks.pop()

  def read_jets(self):
    with open(path, "r") as fh:
      return fh.read()

  def drop(self):
    # start at top + 3, then apply jets and move down until stopped
    # self.t + [0, 0, 0]
    # loop from top down, check to see if the rock overlaps
    # use binary AND of the tower with the rock - if (rock & tower top ) != 0 then it's colliding
    r = self.next_rock()
    tower = self.t + [0, 0, 0] + [0 for i in r[1]]
    tower.reverse()
    overlap = 0
    for i, row in enumerate(tower):
      if row & r[1][0]:
        overlap = -1
        break
    i += overlap
    for n, rock in enumerate(r[1]):
      tower[i-n] = tower[i-n] | rock
    tower.reverse()
    self.t = [row for row in tower if row]
    print(self.t)
    print(self.height())
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
          rock_list.reverse()
          return rock_list
        rock_list.append((w, r))


def main(path, max_height):
  t = Tower()
  while t.height() < max_height:
    t.drop()
  print(f'hegiht: {t.height()}')


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path, 2022)
