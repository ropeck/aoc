#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 8



def main(test):
  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  directions = data.pop(0)
  data.pop(0)

  map = {}
  for line in data:
    m = re.match(r'(.+) = \((.+), (.+)\)', line)
    key, l, r = m.groups()
    map[key] = (l, r)
  
  count = 0
  cur = 'AAA'
  while cur != 'ZZZ':
    if directions[count%len(directions)] == 'L':
      cur = map[cur][0]
    else:
      cur = map[cur][1]
    count += 1

  if not test:
      aocd.submit(count, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
