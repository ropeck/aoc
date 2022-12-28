#!/usr/bin/python3
import sys

def compare(l, r, d=0):
  print(" "*d + "compare",l, r)
  if type(l) == int and type(r) == int:
    return l <= r
  if type(l) == list and type(r) == list:
    for a,b in zip(l, r):
      if not compare(a, b, d+2):
        print(" "*d + "<false>")
        return False
    return len(l) <= len(r)
  if type(l) == int:
    l = [l]
  else:
    r = [r]
  return compare(l,r, d+ 2)

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
      print("ok", i+1)
    print("")

  print("")
  print("total", sum)


if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
