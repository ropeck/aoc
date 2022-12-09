#!/usr/bin/python3
import sys
from math import sqrt

def main(path):
  total = []
  head = [0,0]
  tail = head.copy()
  with open(path, "r") as fh:
    step_data = fh.read()
  for line in step_data.splitlines():
    if tail not in total:
      total.append(tail.copy())
    (m, n) = line.strip().split()
    print(m, n)
    for i in range(int(n)):
      if tail not in total:
        total.append(tail.copy())
      print(f'h:{head} t:{tail}')
      match m:
        case 'U':
          head[1] += 1
        case 'D':
          head[1] -= 1
        case 'L':
          head[0] -= 1
        case 'R':
          head[0] += 1

      d = sqrt(abs(head[0]-tail[0])**2 + abs(head[1]-tail[1])**2)
      if d > sqrt(2):
        n = abs(head[0] - tail[0])
        if n:
          tail[0] += int(n/abs(n))
        n = abs(head[1] - tail[1])
        if n:
          tail[1] += int(n/abs(n))



  print(total)
  print(f'total: {len(total)}')
  return(total)

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)