#!/usr/bin/python3
import aocd
import re
import sys

def main(test):
  total = 0
  
  mod = aocd.models.Puzzle(year=2023, day=2)
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
    pass
 
  limit = {"red": 12, "green": 13, "blue": 14} 

  for line in data.splitlines():
    failed = False
    m = re.match(r"Game (\d+): (.*)", line)
    num = m.group(1)
    v = {}
    p = 1
    for draw in m.group(2).split("; "):
        for color_count in draw.split(", "):
            (n, color) = color_count.split(" ")
            if int(n) > v.get(color, 0):
                v[color] = int(n)
    for n in v.values():
        p = p * n
    total += p
  print(total)
  if not test:
      aocd.submit(total, part="b", day=2, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
