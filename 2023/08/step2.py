#!/usr/bin/python3
import aocd
import re
import sys

_DAY = 8



def main(test):
  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=_DAY)
  if not test:
    data = mod.input_data.splitlines()
  else:
    data = mod.example_data.splitlines()

  directions = data.pop(0)
  data.pop(0)

  map = {}
  for line in data:
    m = re.match(r'(.+) = \((.+), (.+)\)', line)
    key, l, r = m.groups()
    map[key] = (l, r)
  
  
  count = 0
  cur = [x for x in map.keys() if x[2] == 'A']
  while [x for x in cur if x[2] != 'Z']:
    for n in range(len(cur)):
      if directions[count%len(directions)] == 'L':
        cur[n] = map[cur[n]][0]
      else:
        cur[n] = map[cur[n]][1]
    if count % 1000000 == 0:
      print ("state", count, [x for x in cur if x[2] != 'Z'])
      print("VGG", map['VGG'])
      print(len(map))
    count += 1

  if not test:
      aocd.submit(count, part="b", day=_DAY, year=2023)

if __name__ == '__main__':
  main(len(sys.argv) > 1)
