#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 24

def main(test):
  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  height = len(data)
  width = len(data[0])


  import pdb; pdb.set_trace()
  
  if not test:
    aocd.submit(len(p), part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
