#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 20

def main(test):
  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  node = {}

  for line in data:
    # broadcaster -> a, b, c
    # %a -> b
    # %b -> c
    # %c -> inv
    # &inv -> a
    m = re.match("(.*) -> (.*)",line)
    name, sec = m.groups()
    outputs = sec.split(",")
    if name[0] in "%&":
      op = name[0]
      name = name[1:]
    else:
      op = name
    node[name] = (op, 0, outputs)
  initial = node.copy()
  del initial['broadcast']

  q = [('broadcast', 0)]
  while q:
    n, v = q.pop(0)
    for nx in node[n][1]:
      op, val, out = node[nx]
      



  print("total", total)
  if not test:
    aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
