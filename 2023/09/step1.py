#!/usr/bin/python3
import aocd
import re
import sys
import numpy

_DAY = 9



def main(test):
  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  count = 0
  for line in data:
    rr = []
    cur = [int(n) for n in line.split(" ")]
    while [n for n in cur if n]:
      rr.append(cur)
      cur = list(numpy.diff(cur))
    rr.append(cur)
    # print(rr)
    rows = rr.copy()
    rows.reverse()
    total = rows.pop(0)[-1]
    for r in rows:
      total += r[-1]
    print("total", total)
    count += total

  count = int(count)
  print("answer", count)

  if not test:
      aocd.submit(count, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
