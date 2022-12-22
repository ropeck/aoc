#!/usr/bin/python3
from collections import deque
import re
import sys

# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)
FACE = '>v<^'
TURN={'L': -1, 'R': 1}
MOVEDIR = {'>': (0,1), '<': (0,-1), '^': (-1,0), 'v': (1,0)}


def draw(b):
  for l in b:
    print("".join(l))
  print("")

def main(path):
  grid = []
  with open(path,"r") as fh:
    while True:
      line = fh.readline().rstrip()
      if not line:
        break
      grid.append(list(line))
    follow = deque(re.findall("(\d+)([LR]?)",fh.read().strip()))

  (x,y) = (0,0)
  while grid[y][x] != ".":
    x += 1
  dir = 0  # face right

  print(follow)
  while follow:
    (count, movedir) = follow.popleft()
    if movedir:
      (dx, dy) = MOVEDIR[FACE[dir]]
    print(f'{count} {movedir} {dx},{dy}')
    for n in range(int(count)):
      import pdb; pdb.set_trace()
      nx = (x + dx) % len(grid)
      ny = (y + dy) % len(grid[0])
      print(f'grid[{x},{y}]={grid[y][x]}')
      if grid[ny][nx] == " ":
        while grid[ny][nx] == " ":
          ny = (ny + dy) % len(grid[0])
          nx = (nx + dx) % len(grid)
      if grid[ny][nx] == "#":
        continue
      grid[y][x] = FACE[dir]
      # mark old grid pos with direction here
      x = nx
      y = ny
      print(f'{FACE[dir]} {x},{y}')
    if movedir:
      dir = (dir + TURN[movedir]) % len(FACE)
    draw(grid)
    #import pdb; pdb.set_trace()

  print(x,y,FACE[dir])

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
