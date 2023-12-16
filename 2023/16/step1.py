#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 16

def main(test):

  def in_bounds(x, y):
    return x >= 0 and x < width and y >= 0 and y < height
  
  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  width = len(data[0])
  height = len(data)
  active = [[0 for x in range(width)] for y in range(height)]
  beams = [(0,0,1,0)]
  seen = {}

  while beams:
    x, y, dx, dy = beams.pop(0)
    while in_bounds(x,y):
      print(f"{(x,y)} {beams}")
      if seen.get((x,y), False):
        break
      seen[(x,y)] = True
      active[y][x] = 1
      ch = data[y][x]
      if ch == '.':
        pass
      elif ch == '/':
        (dx, dy) = {(-1,0): (0,1),
                    (1,0): (0, -1),
                    (0,-1): (1, 0),
                    (0,1): (-1, 0)}[(dx, dy)]
        
      elif ch == '\\':
        (dx, dy) = {(-1,0): (0,-1),
                    (1,0): (0, 1),
                    (0,-1): (-1, 0),
                    (0,1): (1, 0)}[(dx, dy)]
        
      elif ch == '|':
        if dy == 0:
          beams.extend([(x, y-1, 0, -1), (x, y+1, 0, 1)])
          break
      elif ch == '-':
        if dx == 0:
          beams.extend([(x-1, y, -1, 0), (x+1, y, 1, 0)])
          break
      x += dx
      y += dy

      

  total = 0
  for row in active:
    total += sum(row)

  active = [[False for x in range(width)] for y in range(height)]

  print("total", total)
  # if not test:
  #     aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
