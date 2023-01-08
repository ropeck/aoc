#!/usr/bin/python3
from icecream import ic
import step1
import sys

def main(path):
  try:
    with open("tower-output.new", "r") as fh:
      t = []
      for l in fh:
        r = l.strip().split()
        t.append((int(r[0]), eval(" ".join(r[1:]))))
  except IOError:
    step1.main(path, 30_000)
    with open("tower-output.new", "r") as fh:
      t = []
      for l in fh:
        r = l.strip().split()
        t.append((int(r[0]), eval(" ".join(r[1:]))))
  print(f'tower is {len(t)} tall')
  match = None
  stop_loop = False
  for a in range(len(t)):
    if match and a == match[1]:
      print("caught middle")
      continue

    for b in range(a+1, len(t)):
      if stop_loop:
        stop_loop = False
        break
      if t[a][0] == t[b][0]:
        for i in range(len(t) - b):
          if t[a + i][0] != t[b + i][0]:
            break
          if match and a + i > match[1]:
            # print(f'middle overlap: {a} {a+i}')
            stop_loop = True
            break
        if not match or (i > match[2]):
          match = (a, b, i, t[a][1], t[a + i][1])
          print(match)
  print(match)

  print("checking repeat to confirm the match for the rest of the list")
  st = match[0]
  strock = match[3][-1]
  pd = match[2]
  rock = match[4][-1]
  rockmod = rock - strock
  print(f'after {st} rows (rock {strock}), the pattern repeats every {pd} rows.')
  print(f'At {st + pd} is rock {rock} and rock repeats every {rockmod} rocks')

  mismatch = 0
  for i in range(st+1,len(t)):
    rep = (i - st) % pd
    off = st + rep
    if t[i][0] != t[off][0]:
      print(f'mismatch:')
      ic(i,off)
      exit(1)
      mismatch +=1
  print(f'checked {i} rows and found {mismatch} not matching the repeat pattern')

  n = 10**12
  # find row for a given rock number
  rem = (n - strock) % rockmod
  rep = int((n - strock) / rockmod)

  row = st + pd * rep
  # rk = t[row][1][-1] + rem
  print(f'for {n} rocks, rem {rem}, {rep} times is {row}')

  pass
if __name__ == '__main__':
  if len(sys.argv) > 1:
    path = sys.argv[1]
  else:
    path = "input"
  main(path)


