#!/usr/bin/python3
import sys

def main(path):
  d = []
  with open(path, "r") as fh:
    for line in fh:
      d.append(int(line))

  print(d)
  for n in d.copy():
    if n == 0:
      print(n, d)
      continue
    i = d.index(n)
    d.pop(i)
    if i+n == 0:
      d.append(n)
    else:
      d.insert((i+n)%len(d), n)
    print(n, d)

  i = d.index(0)
  l = len(d)
  o = l - i

  res = [d[((n-o)%l)] for n in [1000, 2000, 3000]]
  print(res)
  print(sum(res))


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
