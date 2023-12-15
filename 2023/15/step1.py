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
  for w in data[0].split(","):
    print (w, hash(w))
    total += hash(w)
  print("total", total)
  if not test:
      aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
