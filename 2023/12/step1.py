#!/usr/bin/python3
import aocd
import re
import sys
import numpy

_DAY = 12

def combinations(sp):
  # loop through all combinations of ? in the string as "." or "#"
  n = sp.count("?")
  comb = []
  for i in range(2**n):
    nn = n
    st = ""
    for b, d in enumerate(sp):
      if d == "?":
        if 2**(nn-1) & i:
          ch = "#"
        else:
          ch = "."
        nn -= 1
      else:
        ch = d
      st = st + ch
    # print(sp, i, st, n)
    comb.append(st)


  return comb

def main(test):

  test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()
  if test:
    data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".splitlines()

  for line in data:
    sp, num = line.split(" ")
    print(combinations(sp))
    print("---------")


  if not test:
      aocd.submit(mid, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
