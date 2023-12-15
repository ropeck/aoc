#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 13

class Board:
  def __init__(self):
    self.board = []

  def append(self, line):
    self.board.append(line)
      
  def is_mirrored_row(self, n):
    d = self.board
    u = n
    l = n + 1
    if l >= len(d) or u < 0:
      return False
    while d[u] == d[l]:
      if u == 0 or l == len(d) - 1:
        return True
      u -= 1
      l += 1
    return False

  def find_mirror_row(self):
    d = self.board
    for n in range(len(d)):
      if self.is_mirrored_row(n):
        return n+1
    return None
      
  def compare_col(self, a, b):
    d = self.board
    for r in d:
      try:
        if r[a] != r[b]:
          return False
      except IndexError:
        return True
    return True

  def is_mirrored_col(self, n):
    d = self.board
    l = n
    r = n + 1
    while self.compare_col(l, r):
      if l == 0 or r == len(d[0]) - 1:
        return True
      l -= 1
      r += 1
    return False

  def find_mirror_col(self):
    d = self.board
    for n in range(len(d[0])-1):
      if self.is_mirrored_col(n):
        return n+1
    return None



  def mirror_check(self):
    f = self.find_mirror_col()
    if f:
      m = f
    else:
      f = self.find_mirror_row()
      if f:
        m = f * 100
      else:
        print("nothing found")
    print(m)
    if m == 0:
      print ("\n".join(d))
    return m

def main(test):

  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  b = Board()
  total = 0
  for line in data + [""]:
    if not line:
      total += b.mirror_check()
      b = Board()
    else:
      b.append(line)

  print("total", total)
  if not test:
      aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
