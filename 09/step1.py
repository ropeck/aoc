#!/usr/bin/python3
import math
import sys

ROOT2 = math.sqrt(2)

def span(r, n):
 low = min([eval(x)[n] for x in r])
 high = max([eval(x)[n] for x in r])
 return high - low

def draw(r, t):
  def mark(n, m):
    b[h - r[n][1] - 1 + ymin][r[n][0] - xmin] = m

  tx=[]
  ty=[]
  for s in r:
    tx.append(s[0])
    ty.append(s[1])
  for s in t:
    (x,y) = eval(s)
    tx.append(x)
    ty.append(y)
  xmin = min(tx)
  ymin = min(ty)
  w = span(t, 0)+1-xmin
  h = span(t, 1)+1-ymin
  b = [['.' for x in range(w)] for y in range(h)]
  for s in t:
    (x, y) = eval(s)
    a = h-1-y+ymin
    b2 = x-xmin
    b[h-1-y+ymin][x-xmin-1] = '#'

  mark(0, "H")
  mark(1, "T")
  for l in b:
    print(''.join(l))

def move_tail(h, t):
  d = [h[i] - t[i] for i in range(len(h))]
  if math.sqrt(sum([n**2 for n in d])) > ROOT2:
    for n in range(len(h)):
      if d[n]:
        t[n] += int(math.copysign(1, d[n]))
  return t

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
      tail = move_tail(rope[0], rope[1])
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
