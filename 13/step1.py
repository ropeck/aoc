#!/usr/bin/python3
import sys

def compare(l, r):
  if type(l) == int and type(r) == int:
    return l <= r
  if type(l) == list and type(r) == list:
    for a,b in zip(l, r):
      if not compare(a, b):
        return False
    return len(l) <= len(r)
  if type(l) == int:
    return r and compare(l,r[0])
  else:
    return l and compare(l[0],r)

def main(path):
  signals = []
  with open(path, "r") as fh:
    while True:
      a = fh.readline()
      if not a:
        break
      b = fh.readline()
      _ = fh.readline()
      signals.append((eval(a),eval(b)))

  sum = 0
  for i, (l, r) in enumerate(signals):
    if compare(l, r):
      sum += (i+1)
      print(i+1, l, r)

  print("")
  print("total", sum)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
