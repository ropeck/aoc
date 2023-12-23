#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 23

def main(test):
  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  height = len(data)
  width = len(data[0])

  q = [((1,0), [])]
  while q:
    (x, y), p = q.pop()
    p.append((x,y))
    if y == height-1:
      print("end", len(p), p)
      for ns, np in q:
        print(ns, "\n", np)
      continue  # next q
    
    for dx, dy in [(-1, 0), (0,-1), (1, 0), (0, 1)]:
      nx = x + dx
      ny = y + dy
      if nx < 0 or ny < 0 or nx > width-1 or ny > height-1:
        continue
      if data[ny][nx] != "#":
        if (dx,dy) == {"<": (1,0), ">": (-1,0), "^": (0,1), "v": (0, -1)}.get(data[ny][nx], (0,0)):
          continue
        if (nx, ny) not in p:
          q.append(((nx, ny), p))

  if not test:
    aocd.submit(len(p), part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
