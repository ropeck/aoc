#!/usr/bin/python3
import aocd
import re
import sys

def main(test):
  total = 0
  # with open(path, "r") as fh:
  #   line = fh.readline().strip()
  #   while True:

  
  mod = aocd.models.Puzzle(year=2023, day=1)
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
    pass
  
  t = 0
  for line in data.splitlines():
      # add first and last digit in string
      print(line)
      m = re.search("(\d).*(\d)", line)
      if m:
          n = int(m.group(1)) * 10  + int(m.group(2))
          if test:
            print(n, line)
          t += n
          continue
      m = re.search("(\d)", line)
      if not m:
          if test:
            print ("bad line: " + line)
          sys.exit(1)
      n = 11 * int(m.group(1))
      if test:
          print(n, line)
      t += n


  print(t)
  if not test:
      aocd.submit(t, part="a", day=1, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
