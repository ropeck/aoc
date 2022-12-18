#!/usr/bin/python3
import numpy as np
from pprint import pprint
import sys


def main(path):
  p = []
  c = {}
  with open(path, "r") as fh:
    for l in fh:
      print(l.strip())
      p.append(tuple([int(x) for x in l.strip().split(",")]))

  total = 0
  for (x, y, z) in p:
    s = 0
    for xd in range(-1, 2):
      for yd in range(-1, 2):
        for zd in range(-1, 2):
          if ((sum([abs(n) for n in [xd, yd, zd]]) > 1)):
            #print(f'big  {xd} {yd} {zd}  ({x+xd}, {y+yd}, {z+zd})')
            pass
          else:
            if (x+xd, y+yd, z+zd) not in p:
              c[(x+xd,y+yd,z+zd)] = -1
              s += 1
            else:
              c[(x+xd,y+yd,z+zd)] = c.get((x+xd,y+yd,z+zd),0) +1
              print(f'  {xd} {yd} {zd}  ({x+xd}, {y+yd}, {z+zd}) {s}')
      if s == 0:
        s == -1
    print(f'({x}, {y}, {z}) {s}')
    total += s

  print(f'total: {total}')
  pprint(c)

  for q in c:
    if c[q] > 0:
      continue
    s = 0
    (x,y,z) = q
    for xd in range(-1, 2):
      for yd in range(-1, 2):
        for zd in range(-1, 2):
          if ((sum([abs(n) for n in [xd, yd, zd]]) > 1)):
            continue
          if (x+xd, y+yd, z+zd) in p:
            s += 1
    if s == 6:
      print(f'{q} {s}')
      total -= s
  print(f'total: {total}')

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
