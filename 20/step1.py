#!/usr/bin/python3
import sys

def main(path):
  d = []
  with open(path, "r") as fh:
    for line in fh:
      d.append(int(line))

  print(d)
  s=[]
  d = enumerate(d)
  for n in d.copy():
    if n in s:
      continue
    s.append(s)
    i = d.index(n)
    d.pop(i)
    d.insert((i+n)%len(d), n)
    #print(n, d)

  res = [d[(n + d.index(0)) % len(d)] for n in [1000, 2000, 3000]]
  print(res)
  print(sum(res))


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
