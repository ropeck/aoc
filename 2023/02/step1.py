#!/usr/bin/python3
import sys

def main(test):
  total = 0
  
  mod = aocd.models.Puzzle(year=2023, day=2)
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
    pass
  

if __name__ == '__main__':
  main(len(sys.argv) > 1)
