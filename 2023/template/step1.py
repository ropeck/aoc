#!/usr/bin/python3
import aocd
import sys

def main(test):
  total = 0
  # with open(path, "r") as fh:
  #   line = fh.readline().strip()
  #   while True:

  
  mod = aocd.models.Puzzle(year=2023, day= )
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
    pass
  

if __name__ == '__main__':
  main(len(sys.argv) > 1)
