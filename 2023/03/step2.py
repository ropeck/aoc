#!/usr/bin/python3
import aocd
import sys

def main(test):
  total = 0
  # test = 1
  mod = aocd.models.Puzzle(year=2023, day=3)
  if not test:
    data = mod.input_data
  else:
    data = mod.example_data
    pass
  
  def get_d(d, x, y):
    try:
      return d[y][x]
    except IndexError:
      return '.'
    
  found_num = []
  stars = {}
  d = data.splitlines()
  for y in range(len(d)):
    line = d[y]
    num = False
    for x in range(len(line)+1):
      if get_d(d, x, y).isdigit() and not num:
        num_start = x
        num = True
        val = 0
      if num:
        if get_d(d, x, y).isdigit():
          val = val * 10 + int(line[x])
        else:
          num_end = x - 1
          # end of number - check around number for parts
          found = False
          for dy in [y - 1, y, y + 1]:
            for dx in range(num_start - 1, num_end + 2):
              ch = get_d(d, dx, dy)
              if ch == "*":
                stars[(dx, dy)] = stars.get((dx, dy), []) + [val]
              if not (ch.isdigit() or ch == "."):
                found = True
                print (f"found {ch} {dx},{dy}")
          if found:
            print(val, y, num_start, num_end)
            found_num.append(val)
          num = False
           
  
  for k, v in stars.items():
    if len(v) == 2:
      total += v[0] * v[1]

  print(total)
  if not test:
      aocd.submit(total, part="b", day=3, year=2023)


if __name__ == '__main__':
  main(len(sys.argv) > 1)
