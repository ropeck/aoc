#!/usr/bin/python3
import aocd
import re
import snoop
import sys
from functools import lru_cache

_DAY = 14

def print_board(b):
  print("\n".join([i.decode() for i in b]))

ROUND = ord("O")
CUBE = ord("#")
EMPTY = ord(".")

def score(b):
  total = 0
  for y, row in enumerate(b):
    for x, v in enumerate(row):
      if v == ROUND:
        total+= len(b)-y
  return total


def tilt_board(b):
  for y, row in enumerate(b):
    if y == 0:
        continue
    for x, v in enumerate(row):
      if v == ROUND:
        yy = y
        ny = yy - 1
        while b[ny][x] == EMPTY and ny >= 0:
          b[yy][x] = EMPTY
          b[ny][x] = ROUND
          ny -= 1
          yy -= 1
  #print_board(b)
  #print (" -")
  return b

def rotate_board(b):
    nb = []
    h = len(b[0])
    w = len(b)
    for y in range(len(b[0])):
      st = [b[w-i-1][y] for i in range(len(b))]
      nb.append(bytearray(st))
    return nb

def find_repeating(nums):
  """Finds the repeating pattern in a list of integers.

  Args:
    nums: A list of integers.

  Returns:
    A list of the repeating pattern.
  """

  # Find the length of the repeating pattern.
  length = 2
  while length <= len(nums) // 2:
    if nums[:length] == nums[length:2 * length]:
      return nums[:length]
    length += 1

  # If no repeating pattern is found, return None.
  return None
  
def main(test):
  #test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  b = [bytearray(line, "utf-8") for line in data]

  n = 0 
  runs = []
  while len(runs) < 300:
    runs.append(score(b))
    b = tilt_board(tuple(b))  # N
  
    b = rotate_board(tuple(b)) 
    b = tilt_board(tuple(b))   # W 
    b = rotate_board(tuple(b))
    b = tilt_board(tuple(b))  # S 
  
  
    b = rotate_board(tuple(b)) 
    b = tilt_board(tuple(b)) # E
    b = rotate_board(tuple(b)) 

    #print("score", n, score(b))
    n += 1
    if True:
      print("n", n)
      print_board(b)
      print("  ")
    
  print(runs)
  off = 0
  pre = []
  pattern = find_repeating(runs)
  while not pattern:
      pre.append(runs.pop(0))
      off += 1
      pattern = find_repeating(runs)

  print ("pre", pre)
  print ("pattern", pattern)
  print ("len", len(pattern))

  t = 1000000000
  t -= off
  r = t % len(pattern)
  total = pattern[r]

  print("total", total)
  if not test:
    aocd.submit(total, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
