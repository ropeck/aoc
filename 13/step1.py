#!/usr/bin/python3
import functools
import sys

def compare(l, r):
  if not type(l) == list:
    l = [l]
  if not type(r) == list:
    r = [r]
  for a,b in zip(l, r):
    if type(a) == int and type(b) == int:
      rec = b - a
    else:
      rec = compare(a, b)
    if rec:
      return rec
  return len(r) - len(l)

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
    if compare(l, r) > 0:
      sum += (i+1)

  print("part1 total", sum)

  sorted(signals, key=functools.cmp_to_key(compare))

if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
