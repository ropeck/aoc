#!/usr/bin/python3
import sys

def main(path):
  total = []
  head = [0,0]
  tail = head.copy()
  for line in open(path,"r"):
    if tail.copy() not in total:
      total.append(tail.copy())
    (m, n) = line.strip().split()
    print(m, n)
    for i in range(int(n)):
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
      if head == tail:
        continue
      if head[1] == tail[1]:
        d = head[0] - tail[0]
        if abs(d) > 1:
          tail[0] += int(d/abs(d))
          if tail[1] != head[1]:
            tail[1] = head[1]
        continue
      if head[0] == tail[0]:
        d = head[1] - tail[1]
        if abs(d) > 1:
          tail[1] += int(d/abs(d))
          if tail[0] != head[0]:
            tail[0] = head[0]
        continue



  print(f'total: {len(total)}')

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)