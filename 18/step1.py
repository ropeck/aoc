#!/usr/bin/python3
import aocd
from pprint import pprint
import sys


def main(test=False):
  p = []
  mod = aocd.models.Puzzle(year=2022, day=18)
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
  for l in data.splitlines():
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
              s += 1
            else:
              print(f'  {xd} {yd} {zd}  ({x+xd}, {y+yd}, {z+zd}) {s}')
    print(f'({x}, {y}, {z}) {s}')
    total += s 
  print(f'total: {total}')
  return total

if __name__ == '__main__':
  if len(sys.argv) > 1:
    arg = sys.argv[1]
  else:
    arg = None
  main(arg)
