#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 5

# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70
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
  maps = {}
  dst_map = {}

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
      r = []
      while line and data:
        line = data.pop(0)
        rr = [int(n) for n in line.split() if n]
        if rr:
          r.append(rr)
      maps[src] = r
      if data:
        line = data.pop(0)
      else:
        break

  print(seeds)
  location = []
  for s in seeds:
    thing = 'seed'
    n = s
    print (thing, n)
    while thing != 'location':
      dst = dst_map[thing]
      dst_n = range_map(n, maps[thing])
      print (dst, dst_n)
      thing = dst
      n = dst_n
    location.append(n)
    print("--")

  print("location", location)
  print("min loc", min(location))

  if not test:
      aocd.submit(min(location), part="a", day=_DAY, year=2023)

def range_map(n, rm_lines):
  print("rm_lines", rm_lines)
  for (dst, src, r) in rm_lines:
    if n >= src and n < src+r:
      return (n - src) + dst
  return n

if __name__ == '__main__':
  main(len(sys.argv) > 1)
