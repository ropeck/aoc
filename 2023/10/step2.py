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
# 0x2500 ─
# 0x2502 │
# 0x250C ┌
# 0x2510 ┐
# 0x2518 ┘
# 0x2514 └

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

#   data = """..........
# .S------7.
# .|F----7|.
# .||OOOO||.
# .||OOOO||.
# .|L-7F-J|.
# .|II||II|.
# .L--JL--J.
# ..........
# """.splitlines()
  
  data = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
""".splitlines()
  
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
  for p in path:
    path_d[p] = True

  def reduce_list(l):
    newlist = []
    start = 0
    end = 0
    for index,value in enumerate(l):
        if index < len(l)-1:
            if l[index+1]> value+1:
                end = index +1
                newlist.append(l[start:end])
                start = end
        else:
                newlist.append(l[start: len(l)])
    return newlist

  def is_inside(cx,cy):
    if (cx, cy) in path_d:
      return False
    lh = 0
    intersect = []
    for x in range(0,cx):
      if (x, cy) in path_d:
        intersect.append(x)
    lh = len(reduce_list(intersect))%2

    intersect = []
    for x in range(cx+1,len(data[0])+1):
      if (x, cy) in path_d:
        intersect.append(x)
    rh = len(reduce_list(intersect))%2

    intersect = []
    for y in range(0, cy):
      if (cx, y) in path_d:
        intersect.append(x)
    up = len(reduce_list(intersect))%2

    intersect = []
    for y in range(cy+1,len(data)+1):
      if (cx, y) in path_d:
        intersect.append(x)
    dn = len(reduce_list(intersect))%2

    return lh == rh and up == dn
    # return all([lh, rh, up, dn])   # odd number of intersects 

  group = []
  inside = 0
  for y, line in enumerate(data):
    l = list(line)
    for x in range(len(line)):
      if is_inside(x,y):
        inside += 1
        group.append((x,y))
        l[x] = '*'
    data[y] = ''.join(l)
  print("group", group)
  group = []
  print("\n".join(data))
  print("inside", inside)
 

  # if not test:
  #     aocd.submit(inside, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
