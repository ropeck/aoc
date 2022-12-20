#!/usr/bin/python3
import math
import sys

SECRET_KEY = 811589153

def main(path):
  d = []
  i = 0
  with open(path, "r") as fh:
    for line in fh:
      d.append((i, int(line)))
      i += 1
  rem = SECRET_KEY % len(d)
  modu = int(SECRET_KEY / len(d))
  print(f'r {rem} {modu}')
  d = [(n, i * rem) for (n, i) in d]

  dl=[]
  for i in d:
    if not i[1]:
      continue
    dl.append(math.log2(abs(i[1])))
  print(f'max log {max(dl)}')
  print(d[:5])

  item_order = d.copy()
  for mix in range(10):
    for n in item_order:
      i = d.index(n)
      d.pop(i)
      d.insert((i+n[1])%len(d), n)

  for x in d:
    if x[1] == 0:
      i = x
      break

  res = [rem * d[(n + d.index(i)) % len(d)][1] for n in [1000, 2000, 3000]]
  print(res)
  print(math.log2(sum(res)))
  print(sum(res))
  return(sum(res))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
