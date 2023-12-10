#!/usr/bin/python3
import aocd
import re
import sys
import numpy

_DAY = 10

dir = {
  '-': [(-1,0), (1,0)],
  'L': [(0,-1), (1,0)],
  'F': [(1,0), (0,1)],
  'J': [(0,-1), (-1,0)],
  '7': [(-1,0), (0,1)],
  '|': [(0,-1), (0,1)],
}


def main(test):

  def connected(cur, prev):
    x,y=cur
    c = data[y][x]
    for dx, dy in dir[c]:
      con = (x+dx, y+dy)
      if con != prev:
        return con
    raise ValueError('next not found')


  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  start = None
  for y, line in enumerate(data):
    try:
      x = line.index('S')
      start = (x,y)
      break
    except ValueError:
      pass
  if not start:
    print("no start found")
    sys.exit(1)

  x, y = start
  cur = None
  prev = start
  # look at the four next places to find the first step
  if data[y][x-1] in '-LF':
    cur = x-1, y
  elif data[y][x+1] in '-J7':
    cur = x+1, y
  elif data[y-1][x] in '|7F':
    cur = x, y-1
  elif data[y+1][x] in '|LJ':
    cur = x, y+1
  if not cur:
    print("can not find the next step from {x, y}")
    sys.exit(1)

  path = [prev, cur]
  while True:
    next = connected(cur, prev)
    if next in path:
      break
    path.append(next)
    prev = cur
    cur = next

  mid = int(len(path)/2)
  print("mid", mid)

  if not test:
      aocd.submit(mid, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
