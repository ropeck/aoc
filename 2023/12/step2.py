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

@lru_cache(maxsize=None)
def combinations(st):
  l = len(st)
  if l == 1:
    if st == "?":
      return [".", "#"]
    else:
      return [st]
  else:
    mid = int(l/2)
    left = combinations(st[:mid])
    right = combinations(st[mid:])
    cmb = [''.join(a) for a in product(left, right)]
    return cmb

@lru_cache(maxsize=None)
def count_combo(sp, exp):
  # print("count combo", sp, exp)
  match_len = 0
  exp = list(exp)
  combo = combinations(sp)
  m = []
  for i in combo:
    groups = [len(n) for n in list(filter(None, i.split(".")))]
    if groups == exp:
      match_len += 1
      m.append(i)
  # print(m)
  return match_len, m

def main(test):

  # test = 1
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
    # print(line)
    sp, num = line.split(" ")
    exp = [int(n) for n in num.split(",")]
    # print(exp, sp)
    a, ac = count_combo(sp, tuple(exp))
    b, bc = count_combo("?"+sp, tuple(exp))
    if sp[-1] == "#":
      bc = [n for n in bc if n[0] != "#"]
      b = len(bc)
    c, cc = count_combo(sp+"?", tuple(exp))
    if sp[0] == "#":
      cc = [n for n in cc if n[-1] != "#"]
      c = len(cc)

      # figure how to combine them in pairs but match double the exp
    if c > a:
      count = (c ** 4) * a
    else:
      count = (b ** 4) * a
    print(count, sp, num)
    total += count
  print("total", total)
  # if not test:
  #     aocd.submit(total, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
