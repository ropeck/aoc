#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 23

def draw(data):
  print("----")
  print("\n".join(data))

def main(test):
  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  height = len(data)
  width = len(data[0])

  # find start
  for y, line in enumerate(data):
    x = line.find("S")
    if x >= 0:
      break
  if not x:
    raise ValueError
  
  print("start", (x, y))

  # while the queue is not empty, reduce count and add neighbors
  s = {}
  q = [(x,y, 64)]
  p = []
  while q:
    x, y, c = q.pop(0)
    if c == 0:
      p.append((x,y))
      continue
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx = x + dx
      ny = y + dy
      if nx < 0 or nx >= width or ny < 0 or ny >= height:
        continue
      if data[ny][nx] not in "S.":
        continue
      if c and (nx, ny, c - 1) not in q:
        q.append((nx, ny, c - 1))
  






  if not test:
    aocd.submit(len(p), part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
