#!/usr/bin/python3
import aocd
import re
import sys
import numpy

_DAY = 13

def is_mirrored_row(n, d):
  u = n
  l = n + 1
  if l >= len(d) or u < 0:
    return False
  while d[u] == d[l]:
    if u == 0 or l == len(d) - 1:
      return True
    u -= 1
    l += 1
  return False

def find_mirror_row(d):
  for n in range(len(d)):
    if is_mirrored_row(n, d):
      return n+1
  return 0
    
def compare_col(a, b, d):
  for r in d:
    try:
      if r[a] != r[b]:
        return False
    except IndexError:
      return True
  return True

def is_mirrored_col(n, d):
  l = n
  r = n + 1
  while compare_col(l, r, d):
    if l == 0 or r == len(d[0]) - 1:
      return True
    l -= 1
    r += 1
  return False

def find_mirror_col(d):
  for n in range(len(d[0])):
    if is_mirrored_col(n, d):
      return n+1
  return 0



def mirror_check(d):
  m = (100*find_mirror_row(d) + find_mirror_col(d)) 
  print(m)
  if m == 0:
    print ("\n".join(d))
  return m

def main(test):

  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  d = []
  total = 0
  for line in data:
    if not line:
      total += mirror_check(d)
      d = []
    else:
      d.append(line)
  if line:
    total += mirror_check(d)
  print("total", total)
  if not test:
      aocd.submit(total, part="a", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
