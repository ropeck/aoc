#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 5

def main(test):
  total = 0
  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
    pass


  print(total)
  if not test:
      aocd.submit(total, part="b", day=_DAY, year=2023)


if __name__ == '__main__':
  main(len(sys.argv) > 1)
