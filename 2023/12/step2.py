#!/usr/bin/python3
import aocd
import re
import sys
import numpy

_DAY = 12

def combinations(sp):
  # loop through all combinations of ? in the string as "." or "#"
  n = sp.count("?")
  # print(sp)
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

  #test = 1
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
  total = 0
  for line in data:
    print(line)
    match = []
    sp, num = line.split(" ")
    sp = (sp+"?")*5
    exp = [int(n) for n in num.split(",")]
    exp = exp * 5
    print(exp, sp)
    combo = combinations(sp)
    for i in combo:
      groups = [len(n) for n in list(filter(None, i.split(".")))]
      if groups == exp:
        match.append((i, groups))

    print(len(match), match)
    total += len(match)

  print("total", total)
  if not test:
      aocd.submit(total, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
