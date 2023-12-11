#!/usr/bin/python3
import aocd
import re
import sys
import numpy

_DAY = 11

def main(test):

  #test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  d = []
  width = len(data[0])
  height = len(data)
  for y, line in enumerate(data):
    d.append(list(line))
    if '#' not in line:
      d.append(list(line))  # double empty rows

  nd = [[] for y in range(len(d))]
  for x in range(width):
    c = [d[y][x] for y in range(len(d)) if d[y][x] is not '.']
    for y in range(len(d)):
      nd[y].append(d[y][x])
      if not c:
        nd[y].append('.')

  print("d")
  for l in d:
    print(''.join(l))

  print("nd")
  for l in nd:
    print(''.join(l))

  g = []
  for y in range(len(nd)):
    for x in range(len(nd[0])):
      if nd[y][x] != '.':
        g.append((x,y))
  print(g)

  dist = []
  c = 1
  for n, (x,y) in enumerate(g):
    for i, (x2, y2) in enumerate(g[n+1:]):
      print(c, n, x, y, i, x2, y2)
      dist.append(abs(x2-x)+abs(y2-y))
      c += 1
  print("dist", sum(dist))


  if not test:
      aocd.submit(sum(dist), part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
