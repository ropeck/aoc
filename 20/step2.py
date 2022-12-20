#!/usr/bin/python3
import sys

def main(path):
  d = []
  i = 0
  with open(path, "r") as fh:
    for line in fh:
      d.append((i, int(line)))
      i += 1
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

  res = [d[(n + d.index(x)) % len(d)][1] for n in [1000, 2000, 3000]]
  print(res)
  print(sum(res))


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
