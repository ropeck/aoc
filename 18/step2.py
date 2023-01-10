#!/usr/bin/python3
from collections import deque
import aocd
import step1
import sys

def center(p):
  d = [[], [], []]
  for i in p:
    for n, v in enumerate(i):
      d[n].append(v)
  l = len(p)
  avg = []
  for n, v in enumerate(d):
    avg.append(int(sum(v)/l))
  return tuple(avg)


def bounding_vol(l):
  p = [[],[],[]]
  for b in bounding_box(l):
    for i, v in enumerate(b):
      p[i].append(v)
  r = 1
  for i in p:
    r *= abs(i[1] - i[0])
  return r

def bounding_box(p):
  d = [[], [], []]
  for i in p:
    for n, v in enumerate(i):
      d[n].append(v)
  min_v = []
  max_v = []
  for dv in d:
    min_v.append(min(dv)-1)
    max_v.append(max(dv)+1)
  return (tuple(min_v), tuple(max_v))

def in_bounds(x, y, z, bounds):
  bx, by, bz = bounds[0]
  if ((x < bx) or (y < by) or (z < bz)):
    return False
  bx, by, bz = bounds[1]
  if ((x > bx) or (y > by) or (z > bz)):
    return False
  return True

def outside_cubes(p):
  bounds = bounding_box(p)
  q = deque([bounds[0]])
  outside = []
  vol = 0
  while len(q):
    # print(list(q), outside)
    x, y, z = q.popleft()
    if not in_bounds(x, y, z, bounds):
      continue
    if (x, y, z) in outside:
      continue
    outside.append((x, y, z))
    for xd in range(-1, 2):
      for yd in range(-1, 2):
        for zd in range(-1, 2):
          nx = x + xd
          ny = y + yd
          nz = z + zd
          if ((sum([abs(n) for n in [xd, yd, zd]]) > 1)):
            continue
          if (nx, ny, nz) in p:
            vol += 1
            continue
          if (nx, ny, nz) in outside:
            continue
          q.append((nx, ny, nz))
  return outside, vol



def count_faces(p):
  c = {}
  counted = []
  outside, vol = outside_cubes(p)
  total = 0
  for (x, y, z) in p:
    s = 0
    for xd in range(-1, 2):
      for yd in range(-1, 2):
        for zd in range(-1, 2):
          nx = x + xd
          ny = y + yd
          nz = z + zd
          if ((sum([abs(n) for n in [xd, yd, zd]]) > 1)):
            continue
          # print(f'  {xd} {yd} {zd}  ({x + xd}, {y + yd}, {z + zd})')
          if (nx, ny, nz) in p + counted:
            continue
          if (nx, ny, nz) not in outside:
            s += 1
            # counted.append((nx, ny, nz))
          else:
            print(f'in {nx, ny, nz}')
    print(f'({x}, {y}, {z}) {s}')
    total += s
  return total, c, vol

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

  total, c, x = count_faces(p)
  print(f'total: {x} outside, {total} inside, {x + total} in total')
  return x

if __name__ == '__main__':
  main(len(sys.argv) > 1)
