#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 6

def travel(t):
  ret = []
  for wait in range(t):
    trav = wait * (t - wait)
    ret.append(trav)
  return ret

def main(test):
  total = 0
  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()
    pass

  (t, nums) = data.pop(0).split(':')
  nums = re.sub(' ','', nums)
  times = [int(x) for x in nums.split()]

  (t, nums) = data.pop(0).split(':')
  nums = re.sub(' ','', nums)
  dist = [int(x) for x in nums.split()]

  winners = []
  ans = 1
  for i in range(len(times)):
    win = [x for x in travel(times[i]) if x > dist[i]]
    winners.append(len(win))
    ans = ans * len(win)
  pass
  print(ans)
  if not test:
      aocd.submit(ans, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
