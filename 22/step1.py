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
    follow = deque(re.findall("(\d+|[LR])",fh.read().strip()))

  (x,y) = (0,0)
  while grid[y][x] != ".":
    x += 1
  dir = 0  # face right

  print(follow)
  while follow:
    move = follow.popleft()
    if move in ["L","R"]:
      dir = (dir + TURN[move]) % len(FACE)
      print(f'turn {move} dir {FACE[dir]} {MOVEDIR[FACE[dir]]}')
      continue
    (dy, dx) = MOVEDIR[FACE[dir]]
    for n in range(int(move)):
      ny = (y + dy) % len(grid)
      nx = (x + dx) % len(grid[ny])
      print(f'grid[{x},{y}]={grid[ny][nx]}')
      g = grid[ny][nx]
      if g == " ":
        while grid[ny][nx] == " ":
          ny = (ny + dy) % len(grid)
          nx = (nx + dx) % len(grid[ny])
      g = grid[ny][nx]
      grid[y][x] = FACE[dir]

      if g == "#":
        break
      # mark old grid pos with direction here
      x = nx
      y = ny
      print(f'{FACE[dir]} {x},{y}')
    # draw(grid)
    #import pdb; pdb.set_trace()

  print(x,y,FACE[dir])
  #  The final password is the sum of 1000 times the row, 4 times the column, and the facing.
  pw = (y+1)*1000 + (x+1)*4 + dir
  print(f'password: {pw}')

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
