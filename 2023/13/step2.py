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
      
  def count_row(self, n, over=None):
    d = self.board
    u = n
    l = n + 1
    c = []
    while l < len(d) and u >= 0:
      for i in range(len(d[u])):
        if d[u][i] != d[l][i] and over != (i,u):
          c.append((i,u))
      u -= 1
      l += 1
    return c

  def find_mirror_row(self):
    # find any row that has just one mismatch
    d = self.board
    for n in range(len(d)):
      c = self.count_row(n)
      if len(c) == 1:
        cc = self.count_row(n, over=c[0])
        if not cc:
          return n+1
    return None

  def count_col(self, n, over=None):
    d = self.board
    u = n
    l = n + 1
    c = []
    while l < len(d[0]) and u >= 0:
      for i in range(len(d)):
        if d[i][u] != d[i][l] and over != (i,u):
          c.append((i,u))
      u -= 1
      l += 1
    return c

  def find_mirror_col(self):
    # find any row that has just one mismatch
    d = self.board
    for n in range(len(d[0])-1):
      c = self.count_col(n)
      if len(c) == 1:
        cc = self.count_col(n, over=c[0])
        if not cc:
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
      aocd.submit(total, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
