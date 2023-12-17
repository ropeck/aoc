#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 17

class Beam:
  def __init__(self, x, y, dx, dy):
      self.x = x
      self.y = y
      self.dx = dx
      self.dy = dy

def main(test):

  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()
  
  d = [[int(c) for c in list(row)] for row in data]
  p = []
  s = {}
  x, y = 0, 0
  w = len(d[0])
  h = len(d)
  
  print(d)


  print("total", total)
  # if not test:
  #     aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
