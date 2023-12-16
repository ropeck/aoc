#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 16

def main(test):
  global beams 

  def in_bounds(x, y):
    return x >= 0 and x < width and y >= 0 and y < height
  
  def draw():
    for row in active:
      s = []
      for v in row:
        if v:
          s.append("#")
        else:
          s.append(" ")
      print(''.join(s))

  def add_beam(x, y, dx, dy):
    global beams
    global seen
    if (x, y, dx, dy) not in seen and (x, y, dx, dy) not in beams:
      beams.append((x, y, dx, dy))
    return beams
  

  def count_active(start):
    global beams
    global seen
    beams = [start]
    active = [[0 for x in range(width)] for y in range(height)]
    seen = {}

    count = 0
    while beams:
      count += 1
      x, y, dx, dy = beams.pop(0)
      while in_bounds(x,y):
        # draw()
        # print("    ")
        # print(f"{(x,y)} {beams}")
        if seen.get((x,y, dx, dy), False):
          break
        seen[(x,y,dx,dy)] = True
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
            beams = add_beam(x, y-1, 0, -1)
            beams = add_beam(x, y+1, 0, 1)
            break
        elif ch == '-':
          if dx == 0:
            beams = add_beam(x-1, y, -1, 0)
            beams = add_beam(x+1, y, 1, 0)
            break
        x += dx
        y += dy

        
    # draw()

    total = 0
    for row in active:
      total += sum(row)
    return total

  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  width = len(data[0])
  height = len(data)
  total = 0
  for x in range(width):
    total = max([total, count_active((x, 0, 0, 1)), count_active((x, height, 0, -1))])
  for y in range(height):
    total = max([total, count_active((0, y, 1, 0)), count_active((width, y, -1, 0))])
  print("total", total)
  if not test:
      aocd.submit(total, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
