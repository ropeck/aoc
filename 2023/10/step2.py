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

# map letters to unicode line drawing chars
# 0x2500 ─ -
# 0x2502 │ |
# 0x250C ┌ F
# 0x2510 ┐ 7
# 0x2518 ┘ J
# 0x2514 └ L

draw = {'-': "\u2500", 'L': "\u2514", 'F': "\u250C",
        'J': "\u2518", '7': "\u2510", '|': "\u2502"}

inside = 0
group = []

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

  data = """..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
..........
""".splitlines()
  
#   data = """.F----7F7F7F7F-7....
# .|F--7||||||||FJ....
# .||.FJ||||||||L7....
# FJL7L7LJLJ||LJ.L-7..
# L--J.L7...LJS7F-7L7.
# ....F-J..F7FJ|L7L7L7
# ....L7.F7||L7|.L7L7|
# .....|FJLJ|FJ|F7|.LJ
# ....FJL-7.||.||||...
# ....L---J.LJ.LJLJ...
# """.splitlines()
  
#   data="""FF7FSF7F7F7F7F7F---7
# L|LJ||||||||||||F--J
# FL-7LJLJ||||||LJL-77
# F--JF--7||LJLJ7F7FJ-
# L---JF-JLJ.||-FJLJJ7
# |F|F-JF---7F7-L7L|7|
# |FFJF7L7F-JF7|JL---7
# 7-L-JL7||F7|L7F-7F7|
# L.L7LFJ|||||FJL7||LJ
# L7JLJL-JLJLJL--JLJ.L
# """.splitlines()

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
  elif data[y+1][x] in '|7F':
    cur = x, y-1
  elif data[y-1][x] in '|LJ':
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

  path_d = {}
  for x,y in path:
    x += 1
    y += 1
    path_d[x,y] = True

  # add border and flood fill to remove outside area
  frame = [" "*(len(data[0])+2)]
  mid = [" " + line + " " for line in data]
  box = frame + mid + frame

  # flood fill from zero corner
  q = [(0,0)]
  outside = {}
  seen = {}
  while q:
    x, y = cur = q.pop(0)
    seen[cur] = True
    ch = box[y][x]
    b = box.copy()
    line = list(b[y])
    line[x] = "@"
    b[y] = ''.join(line)
    for line in box:
      print(''.join(line))
    print("")
    box = b
    if (x, y) in path_d and ch in "-|":
      continue
    if (x, y) not in path_d:
      outside[x, y] = True
      line = list(box[y])
      line[x] = "*"
      box[y] = ''.join(line)
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx = x + dx
      ny = y + dy
      if nx == 5 and ny == 7:
        print("hey")
      if nx < 0 or ny < 0 or nx >= len(box[0]) or ny >= len(box):
        continue
      if (nx, ny) in outside:
        continue
      if (nx, ny) in q or (nx, ny) in seen:
        continue
      if (nx, ny) not in path_d:
        q.append((nx, ny))
        continue
      nc = box[ny][nx]
      # if ((nx, ny) not in path_d or nc not in "-|" or
      #     (dx and nc == "-") or (dy and nc == "|")):
      if  ((ch in dir.keys() and ch not in "-|") or
           (ch == "-" and dx) or (ch == "|" and dy)):
        q.append((nx,ny))

  pass

  # draw data
  for line in box:
    print(''.join(line))

  if not test:
      aocd.submit(len(inside), part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
