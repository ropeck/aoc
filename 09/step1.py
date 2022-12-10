#!/usr/bin/python3
import math
import sys
from math import sqrt, copysign

def move(h, t):
  dx = h[0] - t[0]
  dy = h[1] - t[1]
  d = sqrt(dx ** 2 + dy ** 2)
  if d > sqrt(2):
    if dx:
      t[0] += int(math.copysign(1, dx))
    if dy:
      t[1] += int(math.copysign(1, dy))
  return t

def span(r, n):
 low = min([eval(x)[n] for x in r])
 high = max([eval(x)[n] for x in r])
 return high - low

def draw(r, t):
  w = span(t, 0)
  h = span(t, 1)
  w = 20
  h = 20
  b = [['.' for x in range(w)] for y in range(h)]
  for s in t:
    (x,y) = eval(s)
    y = h - y -1
    b[y][x] = '#'

  def mark(n, m):
    b[h - r[n][1] - 1][r[n][0]] = m

  x=r[0][0]
  y=h - r[0][1] - 1
  mark(0, "H")
  mark(1, "T")
  for l in b:
    print(''.join(l))


def main(path):
  rope = []
  rope.append([0,0])
  rope.append([0,0])
  total = [str(rope[-1])]

  with open(path, "r") as fh:
    step_data = fh.read()
  for line in step_data.splitlines():
    (m, n) = line.strip().split()
    print(f'== {m} {n} ==')
    print('')
    for i in range(int(n)):
      head = rope[0]
      match m:
        case 'U':
          head[1] += 1
        case 'D':
          head[1] -= 1
        case 'L':
          head[0] -= 1
        case 'R':
          head[0] += 1
      rope[0] = head
      tail = move(rope[0], rope[1])
      rope[1] = tail
      total.append(str(rope[-1]))
      # print(f'   h:{head} t:{tail}')
      draw(rope, total)
      print('')
  print(set(total))
  path_len = len(set(total))
  print(f'total: {path_len}')
  return(path_len)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
