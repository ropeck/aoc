#!/usr/bin/python3
import aocd
import re
import sys
from containers import Counter

_DAY = 8



def main(test):

  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()


  if not test:
      aocd.submit(ans, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
