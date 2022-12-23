#!/usr/bin/python3
import sys

moves = [[(0,-1),(-1,-1),(1,-1)],
         [(0,1),(-1,1),(1,1)],
         [(-1,0),(-1,-1),(-1,1)],
         [(1,0)],(1,-1),(1,1)]

def elf_loc(b):
  e=[]
  for y in range(len(b)):
    for x in range(len(b[y])):
      if b[y][x] == "#":
        e.append((y,x))
  return e

def has_neighbor(b, y, x):
  n = []
  for dy in range(y-1,y+2):
    for dx in range(x-1,x+2):
      if dx==x and dy==y:
        continue
      if (dx < 0 or dx > len(b[0])-1 or
          dy < 0 or dy > len(b)-1):
           continue
      if b[dy][dx] == "#":
        n.append((dy,dx))
  return n

def move_elves(b):
  p = []
  for elf in elf_loc(b):
    print("elf", elf, has_neighbor(b, *elf))
  return b

def main(path):
  b = []
  with open(path,"r") as fh:
    for line in fh:
      b.append(list(line.strip()))

  for i in range(10):
    b = move_elves(b)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
