#!/usr/bin/python3
from pprint import pprint
import re
import sys

class Tower:
  def __init__(self):
    self.t = [["." for x in range(7)] for y in range(4)]
    self.top = 0
    self.rocks = self.read_rocks()
    self.rock_n = 0
    self.jet = self.read_jets()
    self.read_jets()

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
    #
    pass

  def read_rocks(self):
    rock_list = []
    with open("rocks","r") as fh:
      while True:
        r = []
        while True:
          l = fh.readline().strip()
          if not l:
            break
          r.append(l)
        if not r:
          return rock_list
        rock_list.append(r)


def main(path):
  t = Tower()
  for i in range(10):
    print(i, t.rock_n)
    print("\n".join(t.next_rock()))
    print("")

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
