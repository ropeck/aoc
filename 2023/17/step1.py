#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 17

class Move:
  def __init__(self, x, y, dx, dy):
    self.x, self.y = x, y
    self.dx, self.dy = dx, dy
    self.count = 3
  def __repr__(self):
    return f"<Move {self.count} ({self.x},{self.y}) {self.dx},{self.dy}>"
  def position(self):
    return (self.x, self.y)
  def left(self):
    nx, ny = {(1,0):(0,-1), (-1,0):(0,1),
              (0,1):(-1,0), (0,-1):(1,0)}[(self.dx, self.dy)]
    return Move(self.dx+nx, self.dy+ny, nx, ny)
  def right(self):
    nx, ny = {(1,0):(0, 1), (-1,0):(0,-1),
              (0,1):(1,0), (0,-1):(-1,0)}[(self.dx, self.dy)]
    return Move(self.dx+nx, self.dy+ny, nx, ny)
  
def main(test):

  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()
  
  d = [[int(c) for c in list(row)] for row in data]
  p = []
  seen = {}
  x, y = 0, 0
  w = len(d[0])
  h = len(d)
  cur = Move(0,0,1,0)
  q = [(cur, [])]
  found = False
  while q and not found:
    print(q)
    print(p)
    cur, p = q.pop(0)
    if cur.x < 0 or cur.x > w or cur.y < 0 or cur.y > h:
      continue
    seen[cur] = True
    p.append(cur.position())
    #left
      #depending on which direction, add left offset
    q.append((cur.left(), p+[cur.position()]))
    #right
    q.append((cur.right(), p+[cur.position()]))
    # append if not seen already
    while cur.count != 0:
      cur.count -= 1
      if cur.position() in seen: continue
      p.append(cur.position())
      seen[cur] = True
      cur.x += cur.dx
      cur.y += cur.dy
      if cur.x < 0 or cur.x > w or cur.y < 0 or cur.y > h:
        break
      if cur == (w,h):
        Found = True
        break

  print(d)


  print("total", total)
  # if not test:
  #     aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
