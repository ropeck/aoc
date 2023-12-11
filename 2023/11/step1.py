#!/usr/bin/python3
import aocd
import re
import sys
import numpy

_DAY = 11

def main(test):

  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  # expand empty parts
  # find empty columns, double them
  width = len(data[0])
  height = len(data)
  newdata = [[] for i in range(height)]
  nx = 0
  for x in range(width):
    c = 0
    nd = ""
    for y in range(height):
      newdata[nx].append(data[y][x])
      if data[y][x] != '.':
        c += 1
      nx += 1
    if not c:
      for y in range(height):
        newdata[nx].append('.')
      nx += 1
  data = [''.join(l) for l in newdata]
  newdata = []
  for y in range(height):
    c = 0
    for x in range(width):
      if data[y][x] != '.':
        c += 1
    newdata.append(data[y])
    if not c:
      newdata.append(data[y])
  data = newdata




  if not test:
      aocd.submit(mid, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
