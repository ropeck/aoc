#!/usr/bin/python3
import sys

moves = [
         [(-1,0),(-1,-1),(-1,1)],
         [(1,0),(1,-1),(1,1)],
         [(0,-1),(-1,-1),(1,-1)],
         [(0,1),(-1,1),(1,1)],
        ]


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
  t = {}
  for ey,ex in elf_loc(b):
    n = has_neighbor(b, ey, ex)
    if not n:
      continue
    clear = False
    #print("elf",ey,ex)
    for m in moves:
      #print(m)
      #for y,x in m:
        #print(f'{y},{x} {b[y+ey][x+ex]}')
      if all([b[y+ey][x+ex]!="#" for y,x in m]):
        clear = True
        break
    if not clear:
      continue
    y,x = m[0]
    ty = y + ey
    tx = x + ex
    #print(f'move {ey},{ex} to {ty},{tx}')
    p.append([(ey, ex), (ey+y, ex+x)])
    t[(ey+y, ex+x)] = t.get((ey+y, ex+x), 0) + 1
  for move in p:
    y,x = move[1]
    if t.get((y,x), 0) == 1:
      #print("move", move)
      oy, ox = move[0]
      b[oy][ox] = "."
      b[y][x] = "#"
  return b, p

def enlarge_board(b):
  if "#" in b[0]:
    b = [["." for x in b[0]]] + b
  if "#" in b[-1]:
    b = b + [["." for x in b[0]]]
  if any([b[y][0] == "#" for y in range(len(b))]):
    c = [["."] + l for l in b]
    b = c
  if any([b[y][-1] == "#" for y in range(len(b))]):
    c = [l + ["."] for l in b]
    b = c
  return b

def draw(b):
  for l in b:
    print("".join(l))
  print("")

def main(path):
  global moves

  b = []
  with open(path,"r") as fh:
    for line in fh:
      b.append(list(line.strip()))

  i = 0
  while True:
    b = enlarge_board(b)
    b, p = move_elves(b)
    print(i)
    draw(b)
    i += 1

    if not p:
      break

    m = moves[0]
    moves = moves[1:]
    moves.append(m)

  print("rounds", i)
  return i



if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
