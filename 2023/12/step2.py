#!/usr/bin/python3
import aocd
import re
import sys
import numpy
from functools import lru_cache
from itertools import product

_DAY = 12

def combinations_orig(sp):
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

@lru_cache(maxsize=1024)
def combinations(st):
  l = len(st)
  if l == 1:
    if st == "?":
      return [".", "#"]
    else:
      return [st]
  if l < 10:  
    mid = int(l/2)
    left = combinations(st[:mid])
    right = combinations(st[mid:])
    cmb = [''.join(a) for a in product(left, right)]
    return cmb
  else:
  # split into 5 parts
    split = int((l+1)/5)
    left = combinations(st[:split])
    for i in range(5):
      right = combinations(st[i*split:(i+1)*split])
      left = [''.join(a) for a in product(left, right)]
    return left

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
        match_len += 1
    print(match_len)
    total += match_len

  print("total", total)
  if not test:
      aocd.submit(total, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
