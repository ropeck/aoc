#!/usr/bin/python3
import numpy as np
import aocd
import sys

def count_faces(p):
  c = {}
  total = 0
  for (x, y, z) in p:
    s = 0
    for xd in range(-1, 2):
      for yd in range(-1, 2):
        for zd in range(-1, 2):
          if ((sum([abs(n) for n in [xd, yd, zd]]) not in [1, 2])):
            #print(f'big  {xd} {yd} {zd}  ({x+xd}, {y+yd}, {z+zd})')
            continue
#          if is_inside((x, y, z), p):
#            print(f'{x},{y},{x} inside')
            continue
          else:
            if (x+xd, y+yd, z+zd) not in p:
              c[(x+xd,y+yd,z+zd)] = -1
              s += 1
            else:
              c[(x+xd,y+yd,z+zd)] = c.get((x+xd,y+yd,z+zd),0) +1
              print(f'  {xd} {yd} {zd}  ({x+xd}, {y+yd}, {z+zd}) {s}')
    print(f'({x}, {y}, {z}) {s}')
    total += s
  return total, c

def is_inside(q, p):
  (x,y,z) = q
  xx = [x1 for (x1,y1,z1) in p if z==z1 and y==y1]
  if len(xx) < 2 or len(xx) % 2:
    return False
  xx.sort()
  if xx[0] > x or xx[-1] < x:
    return False
  yy = [y1 for (x1,y1,z1) in p if x==x1 and z==z1]
  if len(yy) < 2 or len(yy) % 2:
    return False
  yy.sort()
  if yy[0] > y or yy[-1] < y:
    return False
  zz = [z1 for (x1,y1,z1) in p if x==x1 and y==y1]
  zz.sort()
  if len(zz) < 2 or len(zz) % 2:
    return False
  if zz[0] > z or zz[-1] < z:
    return False
  print(f'is inside {q}')
  return True

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

  total, c = count_faces(p)
  print(f'total: {total}')
  return total

if __name__ == '__main__':
  main(len(sys.argv) > 1)
