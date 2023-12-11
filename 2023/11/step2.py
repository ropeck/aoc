#!/usr/bin/python3
import aocd
import re
import sys
import numpy

_DAY = 11

_SCALE = 1000000

def main(test):

  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  d = []
  width = len(data[0])
  height = len(data)
  scaley = []
  scalex = []
  for y, line in enumerate(data):
    d.append(list(line))
    if '#' not in line:
      scaley.append(_SCALE)
    else:
      scaley.append(1)

  nd = [[] for y in range(len(d))]
  for x in range(width):
    c = [d[y][x] for y in range(len(d)) if d[y][x] is not '.']
    if not c:
      scalex.append(_SCALE)
    else:
      scalex.append(1)
    for y in range(len(d)):
      nd[y].append(d[y][x])

  g = []
  for y in range(len(nd)):
    for x in range(len(nd[0])):
      if nd[y][x] != '.':
        g.append((x,y))

  def distx(x):
    return sum([scalex[n] for n in range(x+1)])
  def disty(y):
    return sum([scaley[n] for n in range(y+1)])
  dist = []
  c = 1
  for n, (x,y) in enumerate(g):
    for i, (x2, y2) in enumerate(g[n+1:]):
      # print(c, n, x, y, i, x2, y2)
      dist.append(abs(distx(x2)-distx(x))+abs(disty(y2)-disty(y)))
      print(f"{c} {n} -> {i} {dist[-1]}" )
      c += 1
  print("dist", sum(dist))


  if not test:
      aocd.submit(sum(dist), part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
