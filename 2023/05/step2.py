#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 5

maps = {}
dst_map = {}
src_map = {}

def main(test):
  total = 0
  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()
    pass

  seeds = []

  # get the seeds line
  while not seeds:
    line = data.pop(0)
    m = re.match(r'seeds: (.*)', line)
    if m:
      seeds = [int(x) for x in m.group(1).split()]
      _ = data.pop(0)  # skip the blank line after
    if len(data) == 0:
      print("seeds not found in data")
      sys.exit(1)

  # parse maps
  line = data.pop(0)
  while line:
    m = re.match(r'(.*)-to-(.*) map:', line)
    if m:
      src, dst = m.groups()
      dst_map[src] = dst
      src_map[dst] = src
      r = []
      while line and data:
        line = data.pop(0)
        rr = [int(n) for n in line.split() if n]
        if rr:
          r.append(rr)
      maps[dst] = r   # was src
      if data:
        line = data.pop(0)
      else:
        break

  location = []

  # convert seed ranges to seeds
  seed_range = seeds
  seeds = []
  min_location = None
  while seed_range:
    st = seed_range.pop(0)
    c = seed_range.pop(0)
    seeds.append((st, c))

  test_seed = 0
  while True:
    n = reverse_map(test_seed)
    if in_range(n, seeds):
      min_location = n
      break
    else:
      test_seed += 1

  print("min loc", test_seed)
  if not test:
      aocd.submit(test_seed, part="b", day=_DAY, year=2023)

def in_range(n, s):
  s = sorted(s)
  for (st, c) in s:
    if n >= st and n < st + c:
      return True
    if st > n:
      break
  return False

def reverse_map(n):
    thing = 'location'
    while thing != 'seed':
      src = src_map[thing]
      src_n = range_map(n, maps[thing])
      thing = src
      n = src_n
    return n

def range_map(n, rm_lines):
  for (dst, src, r) in rm_lines:
    if n >= dst and n < dst+r:
      return (n - dst) + src
  return n

if __name__ == '__main__':
  main(len(sys.argv) > 1)
