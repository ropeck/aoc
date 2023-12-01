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
      rec = a - b
    else:
      rec = compare(a, b)
    if rec:
      #print("compare",l,r, rec)
      return rec
  #print("compare",l,r, len(l)-len(r))
  return len(l) - len(r) 

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
    if compare(l, r) < 0:
      sum += (i+1)

  print("part1 total", sum)

  all_signals = [[[i]] for i in [2, 6]]
  for l, r in signals:
    all_signals.append(l.copy())
    all_signals.append(r.copy())

  all_signals = sorted(all_signals, key=functools.cmp_to_key(compare))

  loc = []
  for div in [2, 6]:
    loc.append(all_signals.index([[div]])+1)
  ans = loc[0] * loc[1]
  print("part2 decoder key", ans)



if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)
