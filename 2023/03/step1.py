#!/usr/bin/python3
import aocd
import sys

def main(test):
  total = 0
  mod = aocd.models.Puzzle(year=2023, day=3)
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
    pass


  # print(total)
  # if not test:
  #     aocd.submit(total, part="a", day=3, year=2023)


if __name__ == '__main__':
  main(len(sys.argv) > 1)
