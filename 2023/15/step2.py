#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 15


def hash(str):
  cur = 0
  for i, c in enumerate(str):
    cur += ord(c)
    cur = cur * 17
    cur = cur % 256
  return cur

def main(test):

  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  total = 0
  box = [[] for i in range(256)]
  for w in data[0].split(","):
    # print(w)
    m = re.match(r"(.*)([-=])(.?)", w)
    if not m:
      raise ValueError("no match in line: " + w)
    (label, op, value) = m.groups()
    b = hash(label)
    # print("hash",label, b)
    if op == "=":
      found = False
      for i, v in enumerate(box[b]):
        if v[0] == label:
          box[b][i] = (label, value)
          found = True
      if not found:
        box[b].append((label, value))
    if op == "-":
      for i, v in enumerate(box[b]):
        if v[0] == label:
          del box[b][i]

  # print([x for x in box if x])
  total = 0
  for i, b in enumerate(box):
    if not b:
      continue
    for n, s in enumerate(b):
      v = (1+i) * (1+n) * int(s[1])
      total += v
  print("total", total)
  if not test:
      aocd.submit(total, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
