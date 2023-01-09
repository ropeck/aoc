#!/usr/bin/python3
import reprlib

from icecream import ic
import step1
import sys

def main(path):
  t = step1.main(path, 2022)
  st = t.hoff
  strock = t.roff
  pd = t.hrep
  rock = t.rrep + t.roff
  rockmod = t.rrep
  print(f'after {t.hoff} rows (rock {t.roff}), the pattern repeats every {t.hlen} rows.')
  print(f'At {t.hrep} is rock {t.rrep} and rock repeats every {t.rocklen} rocks')

  n = 10**12
  # find row for a given rock number
  rem = (n - t.roff) % t.rocklen
  rep = int((n - t.roff) / t.rocklen)

  row = t.hoff + t.hlen * rep

  # how many rows for the remaining rocks?
  # find the history for start + rem and subtract hoff to find the diff
  n = t.roff + rem
  for h in t.history.values():
    for r, height in h:
      if r == n:
        delta = height - t.hoff
        break
  if not delta:
    raise ValueError
  final_height = t.hoff + t.hlen * rep + delta

  print(f'final height {final_height}')
  m = [x for x in t.history.values() if x[0] == n]
  print(m)
  print(f'for {n} rocks, rem {rem}, {rep} times is {row}')

  pass
if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)


