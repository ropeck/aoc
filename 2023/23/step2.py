#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 23

def main(test):

  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  print("total", total)
  # if not test:
  #     aocd.submit(total, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
