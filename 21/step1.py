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

  for n in d.copy():
    i = d.index(n)
    d.pop(i)
    v = n[1]
    new_i = (i + v) % len(d)
    d.insert(new_i, n)
    #print(n, d)

  for x in d:
    if x[1] == 0:
      i = x
      break

  res = [d[(n + d.index(i)) % len(d)][1] for n in [1000, 2000, 3000]]
  print(res)
  print(sum(res))


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
